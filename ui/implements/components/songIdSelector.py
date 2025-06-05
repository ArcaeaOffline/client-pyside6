import dataclasses
import logging
import re
from enum import IntEnum
from typing import Any

from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from arcaea_offline.searcher import Searcher
from arcaea_offline.utils.rating import rating_class_to_short_text
from PySide6.QtCore import QModelIndex, QObject, QSignalMapper, Qt, Signal, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QComboBox, QCompleter, QWidget

from ui.designer.components.songIdSelector_ui import Ui_SongIdSelector
from ui.extends.shared.database import databaseUpdateSignals
from ui.extends.shared.delegates.descriptionDelegate import DescriptionDelegate
from ui.extends.shared.language import LanguageChangeEventFilter

logger = logging.getLogger(__name__)


class SongIdSelectorMode(IntEnum):
    SongId = 0
    Chart = 1


# region logics


@dataclasses.dataclass
class _ComboBoxItem:
    text: str
    userData: Any
    additionalData: dict[int, Any]

    def apply(self, comboBox: QComboBox):
        comboBox.addItem(self.text, self.userData)

        index = comboBox.findText(self.text)
        if index > -1:
            for role, value in self.additionalData.items():
                comboBox.setItemData(index, value, role)


class SearchCompleterModel(QStandardItemModel):
    ChartRole = Qt.ItemDataRole.UserRole + 10

    def __init__(self, parent=None):
        super().__init__(parent)
        self.searcher = Searcher()
        self.db = Database()

    def updateSearcherSongs(self):
        with self.db.sessionmaker() as session:
            self.searcher.import_songs(session)

    def getSearchResult(self, kw: str):
        self.clear()

        songIds = self.searcher.search(kw)

        charts: list[Chart] = []
        for songId in songIds:
            _charts = self.db.get_charts_by_song_id(songId)
            _charts = sorted(_charts, key=lambda c: c.rating_class, reverse=True)
            charts += _charts

        for chart in charts:
            displayText = (
                f"{chart.title} [{rating_class_to_short_text(chart.rating_class)}]"
            )
            item = QStandardItem(kw)
            item.setData(kw)
            item.setData(displayText, DescriptionDelegate.MainTextRole)
            item.setData(
                f"{chart.song_id}, {chart.set}", DescriptionDelegate.DescriptionTextRole
            )
            item.setData(chart, self.ChartRole)
            self.appendRow(item)


class SongIdSelectorViewModel(QObject):
    packComboBoxItemsReady = Signal()
    songIdComboBoxItemsReady = Signal()

    def __init__(self, parent=None, *, db: Database):
        super().__init__(parent)

        if not isinstance(db, Database):
            raise TypeError(
                "`db` should be an instance of arcaea_offline.database.Database"
            )

        self.__db: Database = None  # type: ignore
        self.__mode = SongIdSelectorMode.SongId

        self.__packComboBoxItems: list[_ComboBoxItem] = []
        self.__songIdComboBoxItems: list[_ComboBoxItem] = []

        self.setDatabase(db)

    @property
    def packComboBoxItems(self):
        return self.__packComboBoxItems

    @property
    def songIdComboBoxItems(self):
        return self.__songIdComboBoxItems

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        if not isinstance(value, SongIdSelectorMode):
            raise TypeError("value is not SongIdSelectorMode")
        self.__mode = value

    def setDatabase(self, db: Database):
        self.__db = db

    def updatePackComboBoxItems(self):
        packs = self.__db.get_packs()

        self.__packComboBoxItems.clear()
        for pack in packs:
            if re.search(r"_append_.*$", pack.id):
                basePackId = re.sub(r"_append_.*$", "", pack.id)
                basePackName = self.__db.get_pack(basePackId).name  # type: ignore
                packName = f"{basePackName} - {pack.name}"
            else:
                packName = pack.name

            self.__packComboBoxItems.append(
                _ComboBoxItem(
                    text=f"{packName} ({pack.id})",
                    userData=pack.id,
                    additionalData={
                        DescriptionDelegate.MainTextRole: packName,
                        DescriptionDelegate.DescriptionTextRole: pack.id,
                    },
                )
            )

        self.packComboBoxItemsReady.emit()

    def updateSongIdComboBoxItems(self, packId: str):
        self.__songIdComboBoxItems.clear()

        items = []
        if self.mode == SongIdSelectorMode.SongId:
            items = self.__db.get_songs_by_pack_id(packId)
        elif self.mode == SongIdSelectorMode.Chart:
            items = self.__db.get_charts_by_pack_id(packId)
        else:
            assert not "reachable"

        insertedSongIds = []

        for item in items:
            if self.mode == SongIdSelectorMode.SongId:
                itemId = item.id  # type: ignore
            elif self.mode == SongIdSelectorMode.Chart:
                itemId = item.song_id  # type: ignore
            else:
                continue

            if itemId not in insertedSongIds:
                self.__songIdComboBoxItems.append(
                    _ComboBoxItem(
                        text=f"{item.title} ({itemId})",
                        userData=itemId,
                        additionalData={
                            DescriptionDelegate.MainTextRole: item.title,
                            DescriptionDelegate.DescriptionTextRole: itemId,
                        },
                    )
                )

                insertedSongIds.append(itemId)

        self.songIdComboBoxItemsReady.emit()


# endregion


class SongIdSelector(Ui_SongIdSelector, QWidget):
    valueChanged = Signal()
    quickSearchActivated = Signal(Chart)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.vm = SongIdSelectorViewModel(self, db=self.db)
        self.vm.packComboBoxItemsReady.connect(self.fillPackComboBox)
        self.vm.songIdComboBoxItemsReady.connect(self.fillSongIdComboBox)

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
        self.vm.mode = mode
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

        self.vm.updatePackComboBoxItems()

        if pack:
            self.selectPack(pack)
        if songId:
            self.selectSongId(songId)

    def fillPackComboBox(self):
        self.packComboBox.clear()

        for item in self.vm.packComboBoxItems:
            item.apply(self.packComboBox)

        self.packComboBox.setCurrentIndex(-1)

    def fillSongIdComboBox(self):
        self.songIdComboBox.clear()

        for item in self.vm.songIdComboBoxItems:
            item.apply(self.songIdComboBox)

        self.songIdComboBox.setCurrentIndex(-1)

    @Slot()
    def on_packComboBox_currentIndexChanged(self):
        if packId := self.packComboBox.currentData():
            self.vm.updateSongIdComboBoxItems(packId)

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
            self.vm.updateSongIdComboBoxItems(packId)
            return True
        else:
            logger.warning("Attempting to select an unknown pack [%s]", packId)
            return False

    def selectSongId(self, songId: str) -> bool:
        songIdIndex = self.songIdComboBox.findData(songId)
        if songIdIndex > -1:
            self.songIdComboBox.setCurrentIndex(songIdIndex)
            return True
        else:
            logger.warning(
                "Attempting to select an unknown song [%s], maybe try selecting a pack first?",
                songId,
            )
            return False

    def selectChart(self, chart: Chart):
        packSelected = self.selectPack(chart.set)
        songIdSelected = self.selectSongId(chart.song_id)
        return packSelected and songIdSelected

    @Slot(QModelIndex)
    def searchCompleterSetSelection(self, index: QModelIndex):
        chart: Chart = index.data(SearchCompleterModel.ChartRole)
        self.selectChart(chart)
        self.quickSearchActivated.emit(chart)

        self.searchLineEdit.clear()
        self.searchLineEdit.clearFocus()
