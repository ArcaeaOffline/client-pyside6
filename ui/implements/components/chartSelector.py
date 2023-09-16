import logging

from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from arcaea_offline.utils.rating import rating_class_to_text
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from ui.designer.components.chartSelector_ui import Ui_ChartSelector
from ui.extends.shared.database import databaseUpdateSignals
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.implements.components.songIdSelector import SongIdSelectorMode

logger = logging.getLogger(__name__)


class ChartSelector(Ui_ChartSelector, QWidget):
    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.valueChanged.connect(self.updateResultLabel)
        self.songIdSelector.valueChanged.connect(self.updateRatingClassEnabled)

        self.songIdSelector.valueChanged.connect(self.valueChanged)
        self.ratingClassSelector.valueChanged.connect(self.valueChanged)

        # handle `songIdSelector.updateDatabase` by this component
        databaseUpdateSignals.songDataUpdated.disconnect(
            self.songIdSelector.updateDatabase
        )
        databaseUpdateSignals.songDataUpdated.connect(self.updateDatabase)

    def setSongIdSelectorMode(self, mode: SongIdSelectorMode):
        self.songIdSelector.setMode(mode)

    def value(self):
        songId = self.songIdSelector.songId()
        ratingClass = self.ratingClassSelector.value()

        if songId and isinstance(ratingClass, int):
            result = self.db.get_chart(songId, ratingClass)
            if result is None and self.songIdSelector.mode == SongIdSelectorMode.SongId:
                return Chart(
                    song_id=songId,
                    rating_class=ratingClass,
                    set=self.songIdSelector.packId(),
                )
            return result
        return None

    def updateDatabase(self):
        # remember selection and restore later
        ratingClass = self.ratingClassSelector.value()

        # wait `songIdSelector` finish
        self.songIdSelector.updateDatabase()

        if ratingClass is not None:
            self.ratingClassSelector.select(ratingClass)

    @Slot()
    def updateResultLabel(self):
        chart = self.value()
        if isinstance(chart, Chart):
            if chart.constant is not None:
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
            else:
                text = f'No chart data<br><font color="gray">{chart.set} | {chart.song_id} | {chart.rating_class}</font>'
            self.resultLabel.setText(text)
        else:
            self.resultLabel.setText("...")

    def updateRatingClassEnabled(self):
        ratingClasses = []
        songId = self.songIdSelector.songId()
        if songId:
            if self.songIdSelector.mode == SongIdSelectorMode.Chart:
                items = self.db.get_charts_by_song_id(songId)
            else:
                items = self.db.get_difficulties_by_song_id(songId)
            ratingClasses = [item.rating_class for item in items]
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
