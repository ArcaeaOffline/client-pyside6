import re
from typing import Any

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, ScoreBest
from arcaea_offline.utils.rating import rating_class_to_text
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui.extends.shared.delegates.chartDelegate import ChartDelegate
from ui.extends.shared.delegates.scoreDelegate import ScoreDelegate


class ChartsModel(QAbstractListModel):
    ChartRole = Qt.ItemDataRole.UserRole

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__data: list[dict[int, Any]] = []

    def rowCount(self, *args) -> int:
        return len(self.__data)

    def columnCount(self, *args) -> int:
        return 1

    def headerData(self, *args):
        return None

    def data(self, index: QModelIndex, role: int):
        if not self.checkIndex(index):
            return None

        return self.__data[index.row()].get(role, None)

    def clear(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
        self.__data.clear()
        self.endRemoveRows()
        self.endResetModel()

    def setCharts(self, charts: list[Chart]):
        self.clear()

        db = Database()
        self.beginInsertRows(QModelIndex(), 0, len(charts))
        for chart in charts:
            pack = db.get_pack(chart.set)
            if re.search(r"_append_.*$", pack.id):
                basePackId = re.sub(r"_append_.*$", "", pack.id)
                basePackName = db.get_pack(basePackId).name
                packName = f"{basePackName} - {pack.name}"
            else:
                packName = pack.name

            tooltip = (
                f"{chart.title}@{packName} [{rating_class_to_text(chart.rating_class)}]"
            )
            self.__data.append(
                {
                    Qt.ItemDataRole.ToolTipRole: tooltip,
                    self.ChartRole: chart,
                }
            )
        self.endInsertRows()


class CustomChartDelegate(ChartDelegate):
    def getChart(self, index: QModelIndex) -> Chart | None:
        return index.data(ChartsModel.ChartRole)


class ChartsWithScoreBestModel(QStandardItemModel):
    ChartRole = Qt.ItemDataRole.UserRole
    ScoreBestRole = Qt.ItemDataRole.UserRole + 10

    def columnCount(self, *args) -> int:
        return 3

    def headerData(self, *args):
        return None

    def setChartAndScore(self, charts: list[Chart], scoreBests: list[ScoreBest]):
        self.clear()

        db = Database()
        self.beginInsertRows(QModelIndex(), 0, len(charts))
        for chart, scoreBest in zip(charts, scoreBests):
            pack = db.get_pack(chart.set)
            if re.search(r"_append_.*$", pack.id):
                basePackId = re.sub(r"_append_.*$", "", pack.id)
                basePackName = db.get_pack(basePackId).name
                packName = f"{basePackName} - {pack.name}"
            else:
                packName = pack.name

            tooltip = (
                f"{chart.title}@{packName} [{rating_class_to_text(chart.rating_class)}]\n"
                f"{scoreBest.score} > {scoreBest.potential}"
            )

            chartItem = QStandardItem()
            chartItem.setData(tooltip, Qt.ItemDataRole.ToolTipRole)
            chartItem.setData(chart, self.ChartRole)

            scoreBestItem = QStandardItem()
            scoreBestItem.setData(tooltip, Qt.ItemDataRole.ToolTipRole)
            scoreBestItem.setData(scoreBest, self.ScoreBestRole)

            potentialTextItem = QStandardItem()
            potentialTextItem.setText(f"{scoreBest.potential}")

            self.appendRow([chartItem, scoreBestItem, potentialTextItem])


class CustomScoreBestDelegate(ScoreDelegate):
    def getScore(self, index: QModelIndex):
        return index.data(ChartsWithScoreBestModel.ScoreBestRole)
