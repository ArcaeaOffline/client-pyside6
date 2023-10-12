import contextlib
import logging
from typing import Tuple, Type

import cv2
import exif
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Score
from arcaea_offline.utils.partner import KanaeDayNight, kanae_day_night
from arcaea_offline_ocr.device import DeviceOcr, DeviceOcrResult
from arcaea_offline_ocr.device.rois import (
    DeviceRois,
    DeviceRoisAuto,
    DeviceRoisExtractor,
    DeviceRoisMasker,
)
from arcaea_offline_ocr.phash_db import ImagePhashDatabase
from arcaea_offline_ocr.utils import imread_unicode
from PySide6.QtCore import QDateTime, QFileInfo

from ui.extends.components.ocrQueue import OcrRunnable
from ui.extends.shared.data import Data

logger = logging.getLogger(__name__)


class TabDeviceOcrRunnable(OcrRunnable):
    def __init__(
        self,
        imagePath: str,
        rois: DeviceRois | Type[DeviceRoisAuto],
        masker: DeviceRoisMasker,
        knnModel: cv2.ml.KNearest,
        phashDb: ImagePhashDatabase,
    ):
        super().__init__()
        self.imagePath = imagePath
        self.rois = rois
        self.masker = masker
        self.knnModel = knnModel
        self.phashDb = phashDb

    def run(self):
        try:
            img = imread_unicode(self.imagePath, cv2.IMREAD_COLOR)
            if isinstance(self.rois, type) and issubclass(self.rois, DeviceRoisAuto):
                rois = self.rois(img.shape[1], img.shape[0])
            else:
                rois = self.rois
            extractor = DeviceRoisExtractor(img, rois)
            ocr = DeviceOcr(extractor, self.masker, self.knnModel, self.phashDb)
            result = ocr.ocr()
            self.signals.resultReady.emit(result)
        except Exception:
            logger.exception("DeviceOcr error:")
        finally:
            self.signals.finished.emit()


def getImageDate(imagePath: str) -> QDateTime:
    datetime = None
    with contextlib.suppress(Exception):
        with open(imagePath, "rb") as imgf:
            exifImage = exif.Image(imgf.read())
        if exifImage.has_exif and exifImage.get("datetime_original"):
            datetimeStr = exifImage.get("datetime_original")
            datetime = QDateTime.fromString(datetimeStr, "yyyy:MM:dd hh:mm:ss")
    if not isinstance(datetime, QDateTime):
        datetime = QFileInfo(imagePath).birthTime()
    return datetime


class ScoreConverter:
    @staticmethod
    def device(imagePath: str, _, result: DeviceOcrResult) -> Tuple[Chart, Score]:
        partnerModifiers = Data().partnerModifiers
        imageDate = getImageDate(imagePath)

        # calculate clear type
        if result.partner_id == "50":
            dayNight = kanae_day_night(imageDate)
            modifier = 1 if dayNight == KanaeDayNight.Day else 2
        else:
            modifier = partnerModifiers.get(result.partner_id, 0)

        if result.clear_status == 1 and modifier == 1:
            clearType = 4
        elif result.clear_status == 1 and modifier == 2:
            clearType = 5
        else:
            clearType = result.clear_status

        db = Database()
        score = Score(
            song_id=result.song_id,
            rating_class=result.rating_class,
            score=result.score,
            pure=result.pure,
            far=result.far,
            lost=result.lost,
            date=imageDate.toSecsSinceEpoch(),
            max_recall=result.max_recall,
            modifier=modifier,
            clear_type=clearType,
            comment=f"OCR {QFileInfo(imagePath).fileName()}",
        )
        chart = db.get_chart(score.song_id, score.rating_class) or Chart(
            song_id=result.song_id,
            rating_class=result.rating_class,
            title=result.song_id,
            constant=0.0,
        )
        return (chart, score)
