import logging
import re
from enum import IntEnum

from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from PySide6.QtCore import QModelIndex, QSignalMapper, Qt, Signal, Slot
from PySide6.QtWidgets import QCompleter, QWidget

from ui.designer.components.songIdSelector_ui import Ui_SongIdSelector
from ui.extends.components.songIdSelector import SearchCompleterModel
from ui.extends.shared.database import databaseUpdateSignals
from ui.extends.shared.delegates.descriptionDelegate import DescriptionDelegate
from ui.extends.shared.language import LanguageChangeEventFilter

logger = logging.getLogger(__name__)


class SongIdSelectorMode(IntEnum):
    SongId = 0
    Chart = 1


class SongIdSelector(Ui_SongIdSelector, QWidget):
    valueChanged = Signal()
    quickSearchActivated = Signal(Chart)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        # quick switch bindings
        self.quickSwitchSignalMapper = QSignalMapper(self)
        self.previousPackageButton.clicked.connect(self.quickSwitchSignalMapper.map)
        self.quickSwitchSignalMapper.setMapping(
            self.previousPackageButton, "package||previous"
        )
        self.nextPackageButton.clicked.connect(self.quickSwitchSignalMapper.map)
        self.quickSwitchSignalMapper.setMapping(self.nextPackageButton, "package||next")
        self.previousSongIdButton.clicked.connect(self.quickSwitchSignalMapper.map)
        self.quickSwitchSignalMapper.setMapping(
            self.previousSongIdButton, "songId||previous"
        )
        self.nextSongIdButton.clicked.connect(self.quickSwitchSignalMapper.map)
        self.quickSwitchSignalMapper.setMapping(self.nextSongIdButton, "songId||next")

        self.quickSwitchSignalMapper.mappedString.connect(self.quickSwitchSlot)

        self.mode = SongIdSelectorMode.SongId

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

        self.updateDatabase()
        databaseUpdateSignals.songAddOrDelete.connect(self.updateDatabase)

    def setMode(self, mode: SongIdSelectorMode):
        self.mode = mode

    @Slot(str)
    def quickSwitchSlot(self, action: str):
        model, direction = action.split("||")

        minIndex = -1
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

    def updateDatabase(self):
        self.searchCompleterModel.updateSearcherSongs()

        # remember selection and restore later
        pack = self.packComboBox.currentData()
        songId = self.songIdComboBox.currentData()

        self.fillPackComboBox()

        if pack:
            self.selectPack(pack)
        if songId:
            self.selectSongId(songId)

    def fillPackComboBox(self):
        self.packComboBox.clear()
        packs = self.db.get_packs()
        for pack in packs:
            if isAppendPack := re.search(r"_append_.*$", pack.id):
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
        if packId := self.packComboBox.currentData():
            if self.mode == SongIdSelectorMode.SongId:
                items = self.db.get_songs_by_pack_id(packId)
            elif self.mode == SongIdSelectorMode.Chart:
                items = self.db.get_charts_by_pack_id(packId)
            else:
                raise ValueError("Unknown SongIdSelectorMode.")
            insertedSongIds = []
            for item in items:
                if self.mode == SongIdSelectorMode.SongId:
                    itemId = item.id
                elif self.mode == SongIdSelectorMode.Chart:
                    itemId = item.song_id
                else:
                    continue

                if itemId not in insertedSongIds:
                    self.songIdComboBox.addItem(f"{item.title} ({itemId})", itemId)
                    insertedSongIds.append(itemId)
                    row = self.songIdComboBox.count() - 1
                    self.songIdComboBox.setItemData(
                        row, item.title, DescriptionDelegate.MainTextRole
                    )
                    self.songIdComboBox.setItemData(
                        row, itemId, DescriptionDelegate.DescriptionTextRole
                    )
        self.songIdComboBox.setCurrentIndex(-1)

    @Slot()
    def on_packComboBox_currentIndexChanged(self):
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
        packSelected = self.selectPack(chart.set)
        songIdSelected = self.selectSongId(chart.song_id)
        return packSelected and songIdSelected

    @Slot(QModelIndex)
    def searchCompleterSetSelection(self, index: QModelIndex):
        chart: Chart = index.data(Qt.ItemDataRole.UserRole + 10)
        self.selectChart(chart)
        self.quickSearchActivated.emit(chart)

        self.searchLineEdit.clear()
        self.searchLineEdit.clearFocus()
