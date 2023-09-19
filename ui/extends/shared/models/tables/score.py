from arcaea_offline.calculate import calculate_play_rating
from arcaea_offline.models import Chart, Score
from PySide6.QtCore import QCoreApplication, QModelIndex, QSortFilterProxyModel, Qt

from .base import DbTableModel


class DbScoreTableModel(DbTableModel):
    IdRole = Qt.ItemDataRole.UserRole + 10
    ChartRole = Qt.ItemDataRole.UserRole + 11
    ScoreRole = Qt.ItemDataRole.UserRole + 12
    PttRole = Qt.ItemDataRole.UserRole + 13

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__items = []

    def retranslateHeaders(self):
        self._horizontalHeaders = [
            # fmt: off
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.id"),
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.chart"),
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.score"),
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.potential"),
            # fmt: on
        ]

    def syncDb(self):
        newScores = self._db.get_scores()
        newScores = sorted(newScores, key=lambda x: x.id)
        newCharts = [
            self._db.get_chart(score.song_id, score.rating_class) for score in newScores
        ]
        newPtts = []
        for chart, score in zip(newCharts, newScores):
            if isinstance(chart, Chart) and isinstance(score, Score):
                newPtts.append(calculate_play_rating(chart.constant / 10, score.score))
            else:
                newPtts.append(None)

        newScoreIds = [score.id for score in newScores]
        oldScoreIds = [item[self.ScoreRole].id for item in self.__items]

        deleteIds = list(set(oldScoreIds) - set(newScoreIds))
        newIds = list(set(newScoreIds) - set(oldScoreIds))
        deleteRowIndexes = [oldScoreIds.index(deleteId) for deleteId in deleteIds]

        # first delete rows
        for deleteRowIndex in sorted(deleteRowIndexes, reverse=True):
            self.beginRemoveRows(QModelIndex(), deleteRowIndex, deleteRowIndex)
            self.__items.pop(deleteRowIndex)
            self.endRemoveRows()

        # now update existing datas
        for oldItem, newChart, newScore, newPtt in zip(
            self.__items, newCharts, newScores, newPtts
        ):
            oldItem[self.IdRole] = newScore.id
            oldItem[self.ChartRole] = newChart
            oldItem[self.ScoreRole] = newScore
            oldItem[self.PttRole] = newPtt

        # finally insert new rows
        for newId in newIds:
            insertRowIndex = self.rowCount()
            itemListIndex = newScoreIds.index(newId)
            score = newScores[itemListIndex]
            chart = newCharts[itemListIndex]
            ptt = newPtts[itemListIndex]
            self.beginInsertRows(QModelIndex(), insertRowIndex, insertRowIndex)
            self.__items.append(
                {
                    self.IdRole: score.id,
                    self.ChartRole: chart,
                    self.ScoreRole: score,
                    self.PttRole: ptt,
                }
            )
            self.endInsertRows()

        # trigger view update
        topLeft = self.index(0, 0)
        bottomRight = self.index(self.rowCount() - 1, self.columnCount() - 1)
        self.dataChanged.emit(
            topLeft,
            bottomRight,
            [Qt.ItemDataRole.DisplayRole, self.IdRole, self.ChartRole, self.ScoreRole],
        )

    def rowCount(self, *args):
        return len(self.__items)

    def data(self, index, role):
        if index.isValid() and self.checkIndex(index):
            if index.column() == 0 and role in [
                Qt.ItemDataRole.DisplayRole,
                self.IdRole,
            ]:
                return self.__items[index.row()][self.IdRole]
            elif index.column() == 1 and role == self.ChartRole:
                return self.__items[index.row()][self.ChartRole]
            elif index.column() == 2 and role in [self.ChartRole, self.ScoreRole]:
                return self.__items[index.row()][role]
            elif index.column() == 3:
                if role == Qt.ItemDataRole.DisplayRole:
                    return f"{self.__items[index.row()][self.PttRole]:.3f}"
                elif role == self.PttRole:
                    return self.__items[index.row()][self.PttRole]
        return None

    def setData(self, index, value, role):
        if not (index.isValid() and self.checkIndex(index)):
            return False

        if index.column() == 2 and isinstance(value, Score) and role == self.ScoreRole:
            self._db.update_score(self.__items[index.row()][self.IdRole], value)
            self.syncDb()
            return True

        return False

    def flags(self, index) -> Qt.ItemFlag:
        flags = super().flags(index)
        flags |= Qt.ItemFlag.ItemIsSelectable
        if index.column() in [1, 2]:
            flags |= Qt.ItemFlag.ItemIsEditable
        return flags

    def _removeRow(self, row: int, syncDb: bool = True):
        if not 0 <= row < self.rowCount():
            return False

        try:
            self._db.delete_score(self.__items[row][self.IdRole])
            if syncDb:
                self.syncDb()
            return True
        except Exception:
            return False

    def removeRow(self, row: int, parent=...):
        return self._removeRow(row)

    def removeRows(self, row: int, count: int, parent=...):
        maxRow = min(self.rowCount() - 1, row + count - 1)
        if row > maxRow:
            return False

        result = all(
            self._removeRow(row, syncDb=False) for row in range(row, row + count)
        )
        self.syncDb()
        return result

    def removeRowList(self, rowList: list[int]):
        result = all(
            self._removeRow(row, syncDb=False) for row in sorted(rowList, reverse=True)
        )
        self.syncDb()
        return result


class DbScoreTableSortFilterProxyModel(QSortFilterProxyModel):
    Sort_C2_ScoreRole = Qt.ItemDataRole.UserRole + 75
    Sort_C2_TimeRole = Qt.ItemDataRole.UserRole + 76

    def lessThan(self, source_left, source_right) -> bool:
        if source_left.column() != source_right.column():
            return

        column = source_left.column()
        if column == 0:
            return source_left.data(DbScoreTableModel.IdRole) < source_right.data(
                DbScoreTableModel.IdRole
            )
        elif column == 2:
            score_left = source_left.data(DbScoreTableModel.ScoreRole)
            score_right = source_right.data(DbScoreTableModel.ScoreRole)
            if isinstance(score_left, Score) and isinstance(score_right, Score):
                if self.sortRole() == self.Sort_C2_ScoreRole:
                    return score_left.score < score_right.score
                elif self.sortRole() == self.Sort_C2_TimeRole:
                    if score_left.date and score_right.date:
                        return score_left.date < score_right.date
                    elif score_left.date:
                        return False
                    else:
                        return True
        elif column == 3:
            return source_left.data(DbScoreTableModel.PttRole) < source_right.data(
                DbScoreTableModel.PttRole
            )
        return super().lessThan(source_left, source_right)
