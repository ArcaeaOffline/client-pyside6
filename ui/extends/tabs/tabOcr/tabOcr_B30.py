import logging

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Score
from arcaea_offline_ocr.b30.chieri.v4.ocr import ChieriBotV4Ocr
from arcaea_offline_ocr.b30.shared import B30OcrResultItem
from PySide6.QtGui import QImage

logger = logging.getLogger(__name__)

from ui.extends.components.ocrQueue import OcrRunnable


class ChieriV4OcrRunnable(OcrRunnable):
    def __init__(self, ocr: ChieriBotV4Ocr, component):
        super().__init__()
        self.ocr = ocr
        self.component = component.copy()

    def run(self):
        try:
            result = self.ocr.ocr_component(self.component)
            self.signals.resultReady.emit(result)
        except Exception:
            logger.exception("ChieriV4 ocr component error")
        finally:
            self.signals.finished.emit()


def b30ResultToScoreInsert(_, qImage: QImage, result: B30OcrResultItem):
    if not result.song_id and not result.title:
        raise ValueError("no title or song_id")

    db = Database()
    if not result.song_id:
        song_id = db.fuzzy_search_song_id(result.title)[0][0]
    else:
        song_id = result.song_id

    chart = Chart.from_db_row(db.get_chart(song_id, result.rating_class))
    score = ScoreInsert(
        song_id=song_id,
        rating_class=result.rating_class,
        score=result.score,
        time=1485014400,
        pure=result.pure,
        far=result.far,
        lost=result.lost,
    )

    return (chart, score)
