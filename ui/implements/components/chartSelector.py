import logging

from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from arcaea_offline.utils.rating import rating_class_to_text
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget

from ui.designer.components.chartSelector_ui import Ui_ChartSelector

logger = logging.getLogger(__name__)


class ChartSelector(Ui_ChartSelector, QWidget):
    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.setupUi(self)

        self.valueChanged.connect(self.updateResultLabel)
        self.songIdSelector.valueChanged.connect(self.updateRatingClassEnabled)

        self.songIdSelector.valueChanged.connect(self.valueChanged)
        self.ratingClassSelector.valueChanged.connect(self.valueChanged)

    def value(self):
        songId = self.songIdSelector.songId()
        ratingClass = self.ratingClassSelector.value()

        if songId and isinstance(ratingClass, int):
            return self.db.get_chart(songId, ratingClass)
        return None

    def showEvent(self, event: QShowEvent):
        # remember selection and restore later
        ratingClass = self.ratingClassSelector.value()

        if ratingClass is not None:
            self.ratingClassSelector.select(ratingClass)
        return super().showEvent(event)

    @Slot()
    def updateResultLabel(self):
        chart = self.value()
        if isinstance(chart, Chart):
            pack = self.db.get_pack(chart.set)
            texts = [
                [
                    pack.name,
                    chart.title,
                    f"{rating_class_to_text(chart.rating_class)} "
                    f"{chart.rating}{'+' if chart.rating_plus else ''}"
                    f"({chart.constant / 10})",
                ],
                [pack.id, chart.song_id, str(chart.rating_class)],
            ]
            texts = [" | ".join(t) for t in texts]
            text = f'{texts[0]}<br><font color="gray">{texts[1]}</font>'
            self.resultLabel.setText(text)
        else:
            self.resultLabel.setText("...")

    def updateRatingClassEnabled(self):
        ratingClasses = []
        songId = self.songIdSelector.songId()
        if songId:
            charts = self.db.get_charts_by_song_id(songId)
            ratingClasses = [chart.rating_class for chart in charts]
        self.ratingClassSelector.setButtonsEnabled(ratingClasses)

    @Slot()
    def on_resetButton_clicked(self):
        self.songIdSelector.reset()

    def selectChart(self, chart: Chart):
        if not self.songIdSelector.selectPack(chart.set):
            return False
        if not self.songIdSelector.selectSongId(chart.song_id):
            return False
        self.ratingClassSelector.select(chart.rating_class)
        return True
