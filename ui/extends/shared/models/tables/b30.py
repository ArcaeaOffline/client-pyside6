from arcaea_offline.models import Chart, Score, ScoreBest
from PySide6.QtCore import QCoreApplication, QModelIndex, QSortFilterProxyModel, Qt
from sqlalchemy import select

from .base import DbTableModel


class DbB30TableModel(DbTableModel):
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
            QCoreApplication.translate("DB30TableModel", "horizontalHeader.id"),
            QCoreApplication.translate("DB30TableModel", "horizontalHeader.chart"),
            QCoreApplication.translate("DB30TableModel", "horizontalHeader.score"),
            QCoreApplication.translate("DB30TableModel", "horizontalHeader.potential"),
            # fmt: on
        ]

    def syncDb(self):
        self.__items.clear()

        with self._db.sessionmaker() as session:
            results = list(
                session.scalars(
                    select(ScoreBest).order_by(ScoreBest.potential.desc()).limit(40)
                )
            )

        songIds = [r.id for r in results]
        ptts = [r.potential for r in results]

        for scoreId, ptt in zip(songIds, ptts):
            score = self._db.get_score_by_id(scoreId)
            chart = self._db.get_chart(score.song_id, score.rating_class)

            self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
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
        return False

    def flags(self, index) -> Qt.ItemFlag:
        flags = super().flags(index)
        flags &= ~(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
        return flags

    def _removeRow(self, row: int, syncDb: bool = True):
        return False

    def removeRow(self, row: int, parent=...):
        return False

    def removeRows(self, row: int, count: int, parent=...):
        return False

    def removeRowList(self, rowList: list[int]):
        return False


class DbB30TableSortFilterProxyModel(QSortFilterProxyModel):
    Sort_C2_ScoreRole = Qt.ItemDataRole.UserRole + 75
    Sort_C2_TimeRole = Qt.ItemDataRole.UserRole + 76

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        # always show not sorted row sequence
        if (
            orientation != Qt.Orientation.Vertical
            or role != Qt.ItemDataRole.DisplayRole
        ):
            return super().headerData(section, orientation, role)
        return section + 1

    def lessThan(self, source_left, source_right) -> bool:
        if source_left.column() != source_right.column():
            return

        column = source_left.column()
        if column == 0:
            return source_left.data(DbB30TableModel.IdRole) < source_right.data(
                DbB30TableModel.IdRole
            )
        elif column == 2:
            score_left = source_left.data(DbB30TableModel.ScoreRole)
            score_right = source_right.data(DbB30TableModel.ScoreRole)
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
            return source_left.data(DbB30TableModel.PttRole) < source_right.data(
                DbB30TableModel.PttRole
            )
        return super().lessThan(source_left, source_right)
