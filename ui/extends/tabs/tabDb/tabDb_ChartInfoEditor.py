from arcaea_offline.models import Difficulty, Song
from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui.extends.shared.delegates.chartDelegate import ChartDelegate


class ChartInfoAbsentModel(QStandardItemModel):
    SongRole = Qt.ItemDataRole.UserRole
    DifficultyRole = Qt.ItemDataRole.UserRole + 1

    def setCustomData(self, songs: list[Song], difficulties: list[Difficulty]):
        self.clear()

        for song, difficulty in zip(songs, difficulties):
            item = QStandardItem()
            item.setData(song, self.SongRole)
            item.setData(difficulty, self.DifficultyRole)
            self.appendRow(item)

    def setLoading(self):
        self.clear()

        self.appendRow(QStandardItem("Loading..."))


class ListViewDelegate(ChartDelegate):
    def getSong(self, index: QModelIndex):
        return index.data(ChartInfoAbsentModel.SongRole)

    def getDifficulty(self, index: QModelIndex):
        return index.data(ChartInfoAbsentModel.DifficultyRole)
