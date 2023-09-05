import logging
import re
from typing import Literal

from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from PySide6.QtCore import QModelIndex, Qt, Signal, Slot
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QCompleter, QWidget

from ui.designer.components.songIdSelector_ui import Ui_SongIdSelector
from ui.extends.components.songIdSelector import SearchCompleterModel
from ui.extends.shared.delegates.descriptionDelegate import DescriptionDelegate

logger = logging.getLogger(__name__)


class SongIdSelector(Ui_SongIdSelector, QWidget):
    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.setupUi(self)

        self.previousPackageButton.clicked.connect(
            lambda: self.quickSwitchSelection("previous", "package")
        )
        self.previousSongIdButton.clicked.connect(
            lambda: self.quickSwitchSelection("previous", "songId")
        )
        self.nextSongIdButton.clicked.connect(
            lambda: self.quickSwitchSelection("next", "songId")
        )
        self.nextPackageButton.clicked.connect(
            lambda: self.quickSwitchSelection("next", "package")
        )

        self.fillPackComboBox()
        self.packComboBox.setCurrentIndex(-1)
        self.songIdComboBox.setCurrentIndex(-1)

        self.searchCompleterModel = SearchCompleterModel()
        self.searchCompleter = QCompleter(self.searchCompleterModel)
        self.searchCompleter.popup().setItemDelegate(
            DescriptionDelegate(self.searchCompleter.popup())
        )
        self.searchCompleter.activated[QModelIndex].connect(
            self.searchCompleterSetSelection
        )
        self.searchLineEdit.setCompleter(self.searchCompleter)

        self.packComboBox.setItemDelegate(DescriptionDelegate(self.packComboBox))
        self.songIdComboBox.setItemDelegate(DescriptionDelegate(self.songIdComboBox))

        self.packComboBox.currentIndexChanged.connect(self.valueChanged)
        self.songIdComboBox.currentIndexChanged.connect(self.valueChanged)

    def quickSwitchSelection(
        self,
        direction: Literal["previous", "next"],
        model: Literal["package", "songId"],
    ):
        minIndex = 0
        if model == "package":
            maxIndex = self.packComboBox.count() - 1
            currentIndex = self.packComboBox.currentIndex() + (
                1 if direction == "next" else -1
            )
            currentIndex = max(min(maxIndex, currentIndex), minIndex)
            self.packComboBox.setCurrentIndex(currentIndex)
        elif model == "songId":
            maxIndex = self.songIdComboBox.count() - 1
            currentIndex = self.songIdComboBox.currentIndex() + (
                1 if direction == "next" else -1
            )
            currentIndex = max(min(maxIndex, currentIndex), minIndex)
            self.songIdComboBox.setCurrentIndex(currentIndex)
        else:
            return

    def packId(self):
        return self.packComboBox.currentData()

    def songId(self):
        return self.songIdComboBox.currentData()

    def reset(self):
        self.packComboBox.setCurrentIndex(-1)
        self.songIdComboBox.setCurrentIndex(-1)

    def showEvent(self, event: QShowEvent):
        # update database results when widget visible
        self.searchCompleterModel.updateSearcherSongs()

        # remember selection and restore later
        pack = self.packComboBox.currentData()
        songId = self.songIdComboBox.currentData()

        self.fillPackComboBox()

        if pack:
            self.selectPack(pack)
        if songId:
            self.selectSongId(songId)
        return super().showEvent(event)

    def fillPackComboBox(self):
        self.packComboBox.clear()
        packs = self.db.get_packs()
        for pack in packs:
            isAppendPack = re.search(r"_append_.*$", pack.id)
            if isAppendPack:
                basePackId = re.sub(r"_append_.*$", "", pack.id)
                basePackName = self.db.get_pack(basePackId).name
                packName = f"{basePackName} - {pack.name}"
            else:
                packName = pack.name
            self.packComboBox.addItem(f"{packName} ({pack.id})", pack.id)
            row = self.packComboBox.count() - 1
            self.packComboBox.setItemData(
                row, packName, DescriptionDelegate.MainTextRole
            )
            self.packComboBox.setItemData(
                row, pack.id, DescriptionDelegate.DescriptionTextRole
            )

        self.packComboBox.setCurrentIndex(-1)

    def fillSongIdComboBox(self):
        self.songIdComboBox.clear()
        packId = self.packComboBox.currentData()
        if packId:
            charts = self.db.get_charts_by_pack_id(packId)
            inserted_song_ids = []
            for chart in charts:
                if chart.song_id not in inserted_song_ids:
                    self.songIdComboBox.addItem(
                        f"{chart.title} ({chart.song_id})", chart.song_id
                    )
                    inserted_song_ids.append(chart.song_id)
                    row = self.songIdComboBox.count() - 1
                    self.songIdComboBox.setItemData(
                        row, chart.title, DescriptionDelegate.MainTextRole
                    )
                    self.songIdComboBox.setItemData(
                        row, chart.song_id, DescriptionDelegate.DescriptionTextRole
                    )
        self.songIdComboBox.setCurrentIndex(-1)

    @Slot()
    def on_packComboBox_activated(self):
        self.fillSongIdComboBox()

    @Slot(str)
    def on_searchLineEdit_textChanged(self, text: str):
        if text:
            self.searchCompleterModel.getSearchResult(text)
        else:
            self.searchCompleterModel.clear()

    def selectPack(self, packId: str) -> bool:
        packIdIndex = self.packComboBox.findData(packId)
        if packIdIndex > -1:
            self.packComboBox.setCurrentIndex(packIdIndex)
            self.fillSongIdComboBox()
            return True
        else:
            logger.warning(f'Attempting to select an unknown pack "{packId}"')
            return False

    def selectSongId(self, songId: str) -> bool:
        songIdIndex = self.songIdComboBox.findData(songId)
        if songIdIndex > -1:
            self.songIdComboBox.setCurrentIndex(songIdIndex)
            return True
        else:
            logger.warning(
                f'Attempting to select an unknown song "{songId}", maybe try selecting a pack first?'
            )
            return False

    def selectChart(self, chart: Chart):
        if not self.selectPack(chart.set):
            return False
        return self.selectSongId(chart.song_id)

    @Slot(QModelIndex)
    def searchCompleterSetSelection(self, index: QModelIndex):
        chart = index.data(Qt.ItemDataRole.UserRole + 10)  # type: Chart
        self.selectChart(chart)

        self.searchLineEdit.clear()
        self.searchLineEdit.clearFocus()
