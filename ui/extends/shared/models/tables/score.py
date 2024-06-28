import logging

from arcaea_offline.models import Chart, Difficulty, Score, ScoreCalculated, Song
from PySide6.QtCore import QCoreApplication, QModelIndex, QSortFilterProxyModel, Qt
from sqlalchemy import select

from .base import DbTableModel

logger = logging.getLogger(__name__)


class DbScoreTableModel(DbTableModel):
    IdRole = Qt.ItemDataRole.UserRole + 10
    ChartRole = Qt.ItemDataRole.UserRole + 11
    ScoreRole = Qt.ItemDataRole.UserRole + 12
    PttRole = Qt.ItemDataRole.UserRole + 13
    SongRole = Qt.ItemDataRole.UserRole + 14
    DifficultyRole = Qt.ItemDataRole.UserRole + 15

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__items = []

    def retranslateHeaders(self):
        self._horizontalHeaders = [
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.id"),
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.chart"),
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.score"),
            QCoreApplication.translate("DbScoreTableModel", "horizontalHeader.potential"),
        ]  # fmt: skip

    def syncDb(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
        self.__items.clear()
        self.endRemoveRows()
        self.endResetModel()

        with self._db.sessionmaker() as session:
            stmt = (
                select(Score, Chart, Song, Difficulty, ScoreCalculated.potential)
                .join(
                    ScoreCalculated,
                    (Score.id == ScoreCalculated.id),
                    isouter=True,
                )
                .join(
                    Chart,
                    (Score.song_id == Chart.song_id)
                    & (Score.rating_class == Chart.rating_class),
                    isouter=True,
                )
                .join(
                    Song,
                    (Score.song_id == Song.id),
                    isouter=True,
                )
                .join(
                    Difficulty,
                    (Score.song_id == Difficulty.song_id)
                    & (Score.rating_class == Difficulty.rating_class),
                    isouter=True,
                )
            )
            results = session.execute(stmt).all()

            self.beginInsertRows(QModelIndex(), 0, len(results) - 1)
            for result in results:
                score, chart, song, difficulty, potential = result

                if chart:
                    chartInModel = chart
                elif song and difficulty:
                    chartInModel = Chart(
                        song_id=song.id,
                        rating_class=difficulty.rating_class,
                        title=difficulty.title or song.title,
                        set=song.set,
                    )
                else:
                    chartInModel = Chart(
                        song_id=score.song_id,
                        rating_class=score.rating_class,
                        title=score.song_id,
                        set="unknown",
                    )

                self.__items.append(
                    {
                        self.IdRole: score.id,
                        self.ScoreRole: score,
                        self.ChartRole: chartInModel,
                        self.SongRole: song,
                        self.DifficultyRole: difficulty,
                        self.PttRole: potential,
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
            elif index.column() == 1 and role in [
                self.ChartRole,
                self.SongRole,
                self.DifficultyRole,
            ]:
                return self.__items[index.row()][role]
            elif index.column() == 2 and role in [self.ChartRole, self.ScoreRole]:
                return self.__items[index.row()][role]
            elif index.column() == 3:
                potential = self.__items[index.row()][self.PttRole]
                if role == Qt.ItemDataRole.DisplayRole:
                    return f"{potential:.3f}" if potential is not None else "-"
                elif role == self.PttRole:
                    return potential
        return None

    def setData(self, index, value, role):
        if not (index.isValid() and self.checkIndex(index)):
            return False

        if index.column() == 2 and isinstance(value, Score) and role == self.ScoreRole:
            self._db.update_score(value)
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
            self._db.delete_score(self.__items[row][self.ScoreRole])
            if syncDb:
                self.syncDb()
            return True
        except Exception:
            logger.exception("Table[Score]: Cannot remove row %s", row)
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

    def lessThan(self, sourceLeft: QModelIndex, sourceRight: QModelIndex) -> bool:
        if sourceLeft.column() != sourceRight.column():
            return

        column = sourceLeft.column()
        if column == 0:
            return sourceLeft.data(DbScoreTableModel.IdRole) < sourceRight.data(
                DbScoreTableModel.IdRole
            )
        elif column == 2:
            scoreLeft = sourceLeft.data(DbScoreTableModel.ScoreRole)
            scoreRight = sourceRight.data(DbScoreTableModel.ScoreRole)
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
            pttLeft = sourceLeft.data(DbScoreTableModel.PttRole)
            pttRight = sourceRight.data(DbScoreTableModel.PttRole)
            if pttLeft and pttRight:
                return pttLeft < pttRight
            elif pttLeft:
                return False
            else:
                return True
        return super().lessThan(sourceLeft, sourceRight)
