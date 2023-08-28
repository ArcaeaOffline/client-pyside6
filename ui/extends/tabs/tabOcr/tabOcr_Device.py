import contextlib
import logging
from typing import Tuple

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Score
from arcaea_offline_ocr.device.shared import DeviceOcrResult
from arcaea_offline_ocr.device.v2.ocr import DeviceV2Ocr
from arcaea_offline_ocr.device.v2.rois import DeviceV2Rois
from arcaea_offline_ocr.utils import imread_unicode
from PySide6.QtCore import QDateTime, QFileInfo

from ui.extends.components.ocrQueue import OcrRunnable

logger = logging.getLogger(__name__)

import exif


class TabDeviceV2OcrRunnable(OcrRunnable):
    def __init__(self, imagePath, device, knnModel, siftDb):
        super().__init__()
        self.imagePath = imagePath
        self.device = device
        self.knnModel = knnModel
        self.siftDb = siftDb

    def run(self):
        try:
            rois = DeviceV2Rois(self.device, imread_unicode(self.imagePath))
            ocr = DeviceV2Ocr(self.knnModel, self.siftDb)
            result = ocr.ocr(rois)
            self.signals.resultReady.emit(result)
        except Exception:
            logger.exception(f"DeviceV2 ocr {self.imagePath} error")
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


class ScoreInsertConverter:
    @staticmethod
    def deviceV2(imagePath: str, _, result: DeviceOcrResult) -> Tuple[Chart, Score]:
        db = Database()
        scoreInsert = ScoreInsert(
            song_id=result.song_id,
            rating_class=result.rating_class,
            score=result.score,
            pure=result.pure,
            far=result.far,
            lost=result.lost,
            time=getImageDate(imagePath).toSecsSinceEpoch(),
            max_recall=result.max_recall,
            clear_type=None,
        )
        chart = Chart.from_db_row(
            db.get_chart(scoreInsert.song_id, scoreInsert.rating_class)
        )
        return (chart, scoreInsert)
