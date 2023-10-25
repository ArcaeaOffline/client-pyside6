from enum import IntEnum

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Difficulty, Score, Song
from PySide6.QtCore import QCoreApplication, QModelIndex, Qt, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMessageBox, QStyledItemDelegate, QWidget
from sqlalchemy import delete, func, select
from sqlalchemy.orm import InstrumentedAttribute, Session

from ui.designer.tabs.tabDb.tabDb_RemoveDuplicateScores_ui import (
    Ui_TabDb_RemoveDuplicateScores,
)
from ui.extends.shared.delegates.chartDelegate import ChartDelegate
from ui.extends.shared.delegates.scoreDelegate import ScoreDelegate
from ui.extends.shared.language import LanguageChangeEventFilter


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
            .first()
        )
        song = session.query(Song).where(Song.id == songId).first()
        difficulty = (
            session.query(Difficulty)
            .where(
                (Difficulty.song_id == songId)
                & (Difficulty.rating_class == ratingClass)
            )
            .first()
        )

        if chart is None and song is None and difficulty is None:
            chart = Chart(song_id=songId, rating_class=ratingClass, set="unknown")

        item.setData(chart, self.ChartRole)
        item.setData(song, self.SongRole)
        item.setData(difficulty, self.DifficultyRole)

    def getGroupKey(self, score: Score, columns: list[InstrumentedAttribute]) -> str:
        baseKeys = [score.song_id, str(score.rating_class)]
        for column in columns:
            key = f"{column.key}{getattr(score,column.key)}"
            baseKeys.append(key)
        return "||".join(baseKeys)

    def setScores(self, scores: list[Score], columns: list[InstrumentedAttribute]):
        self.clear()

        scoreKeyMap: dict[str, list[Score]] = {}
        for score in scores:
            key = self.getGroupKey(score, columns)
            if scoreKeyMap.get(key) is None:
                scoreKeyMap[key] = [score]
            else:
                scoreKeyMap[key].append(score)

        db = Database()
        with db.sessionmaker() as session:
            for key, scores in scoreKeyMap.items():
                songId, ratingClass = key.split("||")[:2]
                ratingClass = int(ratingClass)

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


class QuickSelectComboBoxValues(IntEnum):
    ID_EARLIER = 0
    DATE_EARLIER = 1
    COLUMNS_INTEGRAL = 2


class TabDb_RemoveDuplicateScores(Ui_TabDb_RemoveDuplicateScores, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.db = Database()

        self.removeDuplicateScoresModel = RemoveDuplicateScoresModel(self)
        self.treeView.setModel(self.removeDuplicateScoresModel)

        self.treeViewChartDelegate = TreeViewChartDelegate(self.treeView)
        self.treeViewScoreDelegate = TreeViewScoreDelegate(self.treeView)
        self.treeViewProxyDelegate = TreeViewProxyDelegate(
            self.treeViewChartDelegate, self.treeViewScoreDelegate, self.treeView
        )
        self.treeView.setItemDelegateForColumn(1, self.treeViewProxyDelegate)

        self.quickSelect_comboBox.addItem(
            # fmt: off
            QCoreApplication.translate("TabDb_RemoveDuplicateScores", "quickSelectComboBox.idEarlier"),
            # fmt: on
            QuickSelectComboBoxValues.ID_EARLIER
        )
        self.quickSelect_comboBox.addItem(
            # fmt: off
            QCoreApplication.translate("TabDb_RemoveDuplicateScores", "quickSelectComboBox.dateEarlier"),
            # fmt: on
            QuickSelectComboBoxValues.DATE_EARLIER
        )
        self.quickSelect_comboBox.addItem(
            # fmt: off
            QCoreApplication.translate("TabDb_RemoveDuplicateScores", "quickSelectComboBox.columnsIntegral"),
            # fmt: on
            QuickSelectComboBoxValues.COLUMNS_INTEGRAL
        )

    def getQueryColumns(self):
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
        if self.scan_option_dateCheckBox.isChecked():
            columns.append(Score.date)
        if self.scan_option_modifierCheckBox.isChecked():
            columns.append(Score.modifier)
        if self.scan_option_clearTypeCheckBox.isChecked():
            columns.append(Score.clear_type)

        return columns

    def getQueryScores(self):
        columns = self.getQueryColumns()
        with self.db.sessionmaker() as session:
            groupBySubquery = (
                select(*columns).group_by(*columns).having(func.count() > 1).subquery()
            )
            selectInClause = [
                col == getattr(groupBySubquery.c, col.key) for col in columns
            ]
            return session.query(Score).where(*selectInClause).all()

    def scan(self):
        scores = self.getQueryScores()
        self.removeDuplicateScoresModel.setScores(scores, self.getQueryColumns())
        self.treeView.expandAll()

    def deselectAll(self):
        for row in range(self.removeDuplicateScoresModel.rowCount()):
            parentItem = self.removeDuplicateScoresModel.item(row, 0)
            for childRow in range(parentItem.rowCount()):
                childCheckBoxItem = parentItem.child(childRow, 0)
                childCheckBoxItem.setCheckState(Qt.CheckState.Unchecked)

    def quickSelect(self):
        mode = self.quickSelect_comboBox.currentData()

        if mode is None:
            return

        for row in range(self.removeDuplicateScoresModel.rowCount()):
            parentItem = self.removeDuplicateScoresModel.item(row, 0)

            scores: list[Score] = []

            for childRow in range(parentItem.rowCount()):
                childScoreItem = parentItem.child(childRow, 1)
                scores.append(childScoreItem.data(RemoveDuplicateScoresModel.ScoreRole))

            if mode == QuickSelectComboBoxValues.ID_EARLIER:
                chosenRow = min(enumerate(scores), key=lambda i: i[1].id)[0]
            elif mode == QuickSelectComboBoxValues.DATE_EARLIER:
                chosenRow = min(
                    enumerate(scores),
                    key=lambda i: float("inf") if i[1].date is None else i[1].date,
                )[0]
            elif mode == QuickSelectComboBoxValues.COLUMNS_INTEGRAL:
                chosenRow = max(
                    enumerate(scores),
                    key=lambda i: sum(
                        getattr(i[1], col.key) is not None
                        for col in i[1].__table__.columns
                    ),
                )[0]

            for childRow in range(parentItem.rowCount()):
                childCheckBoxItem = parentItem.child(childRow, 0)
                if childRow != chosenRow:
                    childCheckBoxItem.setCheckState(Qt.CheckState.Checked)
                else:
                    childCheckBoxItem.setCheckState(Qt.CheckState.Unchecked)

    def reverseSelection(self):
        for row in range(self.removeDuplicateScoresModel.rowCount()):
            parentItem = self.removeDuplicateScoresModel.item(row, 0)
            # only when there's a checked item in this group, we perform a reversed selection
            # otherwise we ignore this group
            performReverse = any(
                parentItem.child(childRow, 0).checkState() == Qt.CheckState.Checked
                for childRow in range(parentItem.rowCount())
            )
            if not performReverse:
                continue

            for childRow in range(parentItem.rowCount()):
                childCheckBoxItem = parentItem.child(childRow, 0)
                newCheckState = (
                    Qt.CheckState.Unchecked
                    if childCheckBoxItem.checkState() != Qt.CheckState.Unchecked
                    else Qt.CheckState.Checked
                )
                childCheckBoxItem.setCheckState(newCheckState)

    def deleteSelection(self):
        selectedScores: list[Score] = []
        for row in range(self.removeDuplicateScoresModel.rowCount()):
            parentItem = self.removeDuplicateScoresModel.item(row, 0)
            for childRow in range(parentItem.rowCount()):
                childCheckBoxItem = parentItem.child(childRow, 0)
                if childCheckBoxItem.checkState() == Qt.CheckState.Checked:
                    childScoreItem = parentItem.child(childRow, 1)
                    selectedScores.append(
                        childScoreItem.data(RemoveDuplicateScoresModel.ScoreRole)
                    )

        confirm = QMessageBox.warning(
            self,
            None,
            # fmt: off
            QCoreApplication.translate("TabDb_RemoveDuplicateScores", "deleteSelectionDialog.content {}").format(len(selectedScores)),
            # fmt: on
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.No,
        )
        if confirm != QMessageBox.StandardButton.Yes:
            return

        with self.db.sessionmaker() as session:
            ids = [s.id for s in selectedScores]
            session.execute(delete(Score).where(Score.id.in_(ids)))
            session.commit()

        self.scan()

    @Slot()
    def on_scan_scanButton_clicked(self):
        if len(self.getQueryColumns()) <= 2:
            result = QMessageBox.warning(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("TabDb_RemoveDuplicateScores", "scan_noColumnsDialog.content"),
                # fmt: on
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No,
            )
            if result != QMessageBox.StandardButton.Yes:
                return

        self.scan()

    @Slot()
    def on_quickSelect_selectButton_clicked(self):
        self.quickSelect()

    @Slot()
    def on_deselectAllButton_clicked(self):
        self.deselectAll()

    @Slot()
    def on_reverseSelectionButton_clicked(self):
        self.reverseSelection()

    @Slot()
    def on_expandAllButton_clicked(self):
        self.treeView.expandAll()

    @Slot()
    def on_collapseAllButton_clicked(self):
        self.treeView.collapseAll()

    @Slot()
    def on_resetModelButton_clicked(self):
        self.removeDuplicateScoresModel.clear()

    @Slot()
    def on_deleteSelectionButton_clicked(self):
        self.deleteSelection()
