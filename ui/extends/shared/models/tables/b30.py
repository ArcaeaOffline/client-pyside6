from arcaea_offline.models import Chart, Score, ScoreBest
from PySide6.QtCore import QCoreApplication, QModelIndex, QSortFilterProxyModel, Qt

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
            QCoreApplication.translate("DbB30TableModel", "horizontalHeader.id"),
            QCoreApplication.translate("DbB30TableModel", "horizontalHeader.chart"),
            QCoreApplication.translate("DbB30TableModel", "horizontalHeader.score"),
            QCoreApplication.translate("DbB30TableModel", "horizontalHeader.potential"),
            # fmt: on
        ]

    def syncDb(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
        self.__items.clear()
        self.endRemoveRows()
        self.endResetModel()

        with self._db.sessionmaker() as session:
            results = (
                session.query(ScoreBest, Chart)
                .join(
                    Chart,
                    (ScoreBest.song_id == Chart.song_id)
                    & (ScoreBest.rating_class == Chart.rating_class),
                )
                .order_by(ScoreBest.potential.desc())
                .limit(50)
                .all()
            )

            self.beginInsertRows(QModelIndex(), 0, len(results) - 1)
            for scoreBest, chart in results:
                self.__items.append(
                    {
                        self.IdRole: scoreBest.id,
                        self.ChartRole: chart,
                        self.ScoreRole: scoreBest,
                        self.PttRole: scoreBest.potential,
                    }
                )
            self.endInsertRows()

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

    def lessThan(self, sourceLeft: QModelIndex, sourceRight: QModelIndex) -> bool:
        if sourceLeft.column() != sourceRight.column():
            return

        column = sourceLeft.column()
        if column == 0:
            return sourceLeft.data(DbB30TableModel.IdRole) < sourceRight.data(
                DbB30TableModel.IdRole
            )
        elif column == 2:
            scoreLeft = sourceLeft.data(DbB30TableModel.ScoreRole)
            scoreRight = sourceRight.data(DbB30TableModel.ScoreRole)
            if isinstance(scoreLeft, Score) and isinstance(scoreRight, Score):
                if self.sortRole() == self.Sort_C2_ScoreRole:
                    return scoreLeft.score < scoreRight.score
                elif self.sortRole() == self.Sort_C2_TimeRole:
                    if scoreLeft.date and scoreRight.date:
                        return scoreLeft.date < scoreRight.date
                    elif scoreLeft.date:
                        return False
                    else:
                        return True
        elif column == 3:
            pttLeft = sourceLeft.data(DbB30TableModel.PttRole)
            pttRight = sourceRight.data(DbB30TableModel.PttRole)
            if pttLeft and pttRight:
                return pttLeft < pttRight
            elif pttLeft:
                return False
            else:
                return True
        return super().lessThan(sourceLeft, sourceRight)
