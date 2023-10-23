from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Difficulty, Score, Song
from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QStyledItemDelegate, QWidget
from sqlalchemy import func, select
from sqlalchemy.orm import InstrumentedAttribute, Session

from ui.designer.tabs.tabDb.tabDb_RemoveDuplicateScores_ui import (
    Ui_TabDb_RemoveDuplicateScores,
)
from ui.extends.shared.delegates.chartDelegate import ChartDelegate
from ui.extends.shared.delegates.scoreDelegate import ScoreDelegate


class RemoveDuplicateScoresModel(QStandardItemModel):
    ScoreRole = Qt.ItemDataRole.UserRole
    ChartRole = Qt.ItemDataRole.UserRole + 10
    SongRole = Qt.ItemDataRole.UserRole + 11
    DifficultyRole = Qt.ItemDataRole.UserRole + 12

    def setChartDelegateDatas(
        self, item: QStandardItem, songId: str, ratingClass: int, session: Session
    ):
        chart = (
            session.query(Chart)
            .where((Chart.song_id == songId) & (Chart.rating_class == ratingClass))
            .one()
        )
        song = session.query(Song).where(Song.id == songId).one()
        difficulty = (
            session.query(Difficulty)
            .where(
                (Difficulty.song_id == songId)
                & (Difficulty.rating_class == ratingClass)
            )
            .one()
        )
        item.setData(chart, self.ChartRole)
        item.setData(song, self.SongRole)
        item.setData(difficulty, self.DifficultyRole)

    def setScores(self, scores: list[Score]):
        self.clear()

        scoreKeyMap: dict[tuple[str, int], list[Score]] = {}
        for score in scores:
            key = (score.song_id, score.rating_class)
            if scoreKeyMap.get(key) is None:
                scoreKeyMap[key] = [score]
            else:
                scoreKeyMap[key].append(score)

        db = Database()
        with db.sessionmaker() as session:
            for key, scores in scoreKeyMap.items():
                songId, ratingClass = key

                parentCheckBoxItem = QStandardItem(f"{len(scores)} items")
                parentChartItem = QStandardItem()
                self.setChartDelegateDatas(
                    parentChartItem, songId, ratingClass, session
                )

                for i, score in enumerate(scores):
                    scoreCheckBoxItem = QStandardItem()
                    scoreCheckBoxItem.setEditable(False)
                    scoreCheckBoxItem.setCheckable(True)
                    scoreCheckBoxItem.setEnabled(True)
                    scoreItem = QStandardItem()
                    scoreItem.setData(score, self.ScoreRole)
                    scoreItem.setEditable(False)
                    scoreItem.setEnabled(True)
                    parentCheckBoxItem.setChild(i, 0, scoreCheckBoxItem)
                    parentCheckBoxItem.setChild(i, 1, scoreItem)

                self.appendRow([parentCheckBoxItem, parentChartItem])


class TreeViewChartDelegate(ChartDelegate):
    def getChart(self, index: QModelIndex):
        return index.data(RemoveDuplicateScoresModel.ChartRole)

    def getSong(self, index: QModelIndex):
        return index.data(RemoveDuplicateScoresModel.SongRole)

    def getDifficulty(self, index: QModelIndex):
        return index.data(RemoveDuplicateScoresModel.DifficultyRole)


class TreeViewScoreDelegate(ScoreDelegate):
    def getScore(self, index: QModelIndex):
        return index.data(RemoveDuplicateScoresModel.ScoreRole)


class TreeViewProxyDelegate(QStyledItemDelegate):
    def __init__(
        self, chartDelegate: ChartDelegate, scoreDelegate: ScoreDelegate, parent=None
    ):
        super().__init__(parent)
        self.chartDelegate = chartDelegate
        self.scoreDelegate = scoreDelegate

    def delegateForIndex(self, index: QModelIndex) -> QStyledItemDelegate:
        return self.scoreDelegate if index.parent().isValid() else self.chartDelegate

    def sizeHint(self, option, index: QModelIndex):
        return self.delegateForIndex(index).sizeHint(option, index)

    def paint(self, painter, option, index: QModelIndex):
        self.delegateForIndex(index).paint(painter, option, index)
        QStyledItemDelegate.paint(self, painter, option, index)


class TabDb_RemoveDuplicateScores(Ui_TabDb_RemoveDuplicateScores, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.db = Database()

        self.scan_scanButton.clicked.connect(self.fillModel)

        self.model = RemoveDuplicateScoresModel(self)
        self.treeView.setModel(self.model)

        self.treeViewChartDelegate = TreeViewChartDelegate(self.treeView)
        self.treeViewScoreDelegate = TreeViewScoreDelegate(self.treeView)
        self.treeViewDelegate = TreeViewProxyDelegate(
            self.treeViewChartDelegate, self.treeViewScoreDelegate, self.treeView
        )
        self.treeView.setItemDelegateForColumn(1, self.treeViewDelegate)

    def getGroupByColumns(self):
        columns: list[InstrumentedAttribute] = [Score.song_id, Score.rating_class]

        if self.scan_option_scoreCheckBox.isChecked():
            columns.append(Score.score)
        if self.scan_option_pureCheckBox.isChecked():
            columns.append(Score.pure)
        if self.scan_option_farCheckBox.isChecked():
            columns.append(Score.far)
        if self.scan_option_lostCheckBox.isChecked():
            columns.append(Score.lost)
        if self.scan_option_maxRecallCheckBox.isChecked():
            columns.append(Score.max_recall)
        if self.scan_option_clearTypeCheckBox.isChecked():
            columns.append(Score.clear_type)
        if self.scan_option_modifierCheckBox.isChecked():
            columns.append(Score.modifier)

        return columns

    def getQueryScores(self):
        columns = self.getGroupByColumns()
        with self.db.sessionmaker() as session:
            groupBySubquery = (
                select(*columns).group_by(*columns).having(func.count() > 1).subquery()
            )
            selectInClause = [
                col == getattr(groupBySubquery.c, col.key) for col in columns
            ]
            return session.query(Score).where(*selectInClause).all()

    def fillModel(self):
        scores = self.getQueryScores()
        self.model.setScores(scores)
        self.treeView.expandAll()

    @Slot()
    def on_expandAllButton_clicked(self):
        self.treeView.expandAll()

    @Slot()
    def on_collapseAllButton_clicked(self):
        self.treeView.collapseAll()
