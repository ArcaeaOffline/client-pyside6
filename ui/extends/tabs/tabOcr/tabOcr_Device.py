import contextlib
import logging
from typing import Tuple

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Score
from arcaea_offline_ocr.device.shared import DeviceOcrResult
from arcaea_offline_ocr.device.v2 import DeviceV2AutoRois, DeviceV2Ocr, DeviceV2Rois
from arcaea_offline_ocr.device.v2.sizes import SizesV1, SizesV2
from arcaea_offline_ocr.utils import imread_unicode
from PySide6.QtCore import QDateTime, QFileInfo

from ui.extends.components.ocrQueue import OcrRunnable

logger = logging.getLogger(__name__)

import exif


class TabDeviceV2OcrRunnable(OcrRunnable):
    def __init__(self, imagePath, device, knnModel, phashDb, *, sizesV2: bool):
        super().__init__()
        self.imagePath = imagePath
        self.device = device
        self.knnModel = knnModel
        self.phashDb = phashDb
        self.sizesV2 = sizesV2

    def run(self):
        try:
            rois = DeviceV2Rois(self.device, imread_unicode(self.imagePath))
            rois.sizes = (
                SizesV2(self.device.factor)
                if self.sizesV2
                else SizesV1(self.device.factor)
            )
            ocr = DeviceV2Ocr(self.knnModel, self.phashDb)
            result = ocr.ocr(rois)
            self.signals.resultReady.emit(result)
        except Exception:
            logger.exception(f"DeviceV2 ocr {self.imagePath} error")
        finally:
            self.signals.finished.emit()


class TabDeviceV2AutoRoisOcrRunnable(OcrRunnable):
    def __init__(self, imagePath, knnModel, phashDb, *, sizesV2: bool):
        super().__init__()
        self.imagePath = imagePath
        self.knnModel = knnModel
        self.phashDb = phashDb
        self.sizesV2 = sizesV2

    def run(self):
        try:
            rois = DeviceV2AutoRois(imread_unicode(self.imagePath))
            factor = rois.sizes.factor
            rois.sizes = SizesV2(factor) if self.sizesV2 else SizesV1(factor)
            ocr = DeviceV2Ocr(self.knnModel, self.phashDb)
            result = ocr.ocr(rois)
            self.signals.resultReady.emit(result)
        except Exception:
            logger.exception(f"DeviceV2AutoRois ocr {self.imagePath} error")
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
    def deviceV2(imagePath: str, _, result: DeviceOcrResult) -> Tuple[Chart, Score]:
        db = Database()
        score = Score(
            song_id=result.song_id,
            rating_class=result.rating_class,
            score=result.score,
            pure=result.pure,
            far=result.far,
            lost=result.lost,
            date=getImageDate(imagePath).toSecsSinceEpoch(),
            max_recall=result.max_recall,
            comment=f"OCR {QFileInfo(imagePath).fileName()}",
        )
        chart = db.get_chart(score.song_id, score.rating_class)
        if not chart:
            chart = Chart(
                song_id=result.song_id,
                rating_class=result.rating_class,
                title=result.song_id,
                constant=0.0,
            )
        return (chart, score)
