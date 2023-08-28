from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QMessageBox

from ui.extends.shared.delegates.chartDelegate import ChartDelegate
from ui.extends.shared.delegates.scoreDelegate import ScoreDelegate
from ui.extends.shared.models.tables.b30 import (
    DbB30TableModel,
    DbB30TableSortFilterProxyModel,
)
from ui.implements.components.dbTableViewer import DbTableViewer


class TableChartDelegate(ChartDelegate):
    def getChart(self, index):
        return index.data(DbB30TableModel.ChartRole)


class TableScoreDelegate(ScoreDelegate):
    def getChart(self, index):
        return index.data(DbB30TableModel.ChartRole)

    def getScoreInsert(self, index: QModelIndex):
        return super().getScoreInsert(index)

    def getScore(self, index):
        return index.data(DbB30TableModel.ScoreRole)

    def setModelData(self, editor, model, index):
        QMessageBox.information(self, None, "Cannot edit read only table.")
        return False


class DbB30TableViewer(DbTableViewer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tableView.verticalHeader().setVisible(True)

        self.tableModel = DbB30TableModel(self)
        self.tableProxyModel = DbB30TableSortFilterProxyModel(self)
        self.tableProxyModel.setSourceModel(self.tableModel)
        self.tableView.setModel(self.tableProxyModel)
        self.tableView.setItemDelegateForColumn(1, TableChartDelegate(self.tableView))
        self.tableView.setItemDelegateForColumn(2, TableScoreDelegate(self.tableView))

        tableViewPalette = QPalette(self.tableView.palette())
        highlightColor = QColor(tableViewPalette.color(QPalette.ColorRole.Highlight))
        highlightColor.setAlpha(25)
        tableViewPalette.setColor(QPalette.ColorRole.Highlight, highlightColor)
        self.tableView.setPalette(tableViewPalette)
        self.tableModel.dataChanged.connect(self.resizeTableView)

        self.fillSortComboBox()

    def fillSortComboBox(self):
        self.sort_comboBox.addItem("ID", [0, 1])
        self.sort_comboBox.addItem(
            "Score", [3, DbB30TableSortFilterProxyModel.Sort_C2_ScoreRole]
        )
        self.sort_comboBox.addItem(
            "Time", [3, DbB30TableSortFilterProxyModel.Sort_C2_TimeRole]
        )
        self.sort_comboBox.addItem("Potential", [3, 1])
        self.sort_comboBox.setCurrentIndex(0)
        self.on_sort_comboBox_activated()

    @Slot()
    def resizeTableView(self):
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

    @Slot()
    def on_sort_comboBox_activated(self):
        self.sortProxyModel()

    @Slot()
    def on_sort_descendingCheckBox_toggled(self):
        self.sortProxyModel()

    @Slot()
    def sortProxyModel(self):
        if self.sort_comboBox.currentIndex() > -1:
            column, role = self.sort_comboBox.currentData()
            self.tableProxyModel.setSortRole(role)
            self.tableProxyModel.sort(
                column,
                Qt.SortOrder.DescendingOrder
                if self.sort_descendingCheckBox.isChecked()
                else Qt.SortOrder.AscendingOrder,
            )

    @Slot()
    def on_action_removeSelectedButton_clicked(self):
        QMessageBox.information(self, None, "Cannot edit read only table.")

    @Slot()
    def on_refreshButton_clicked(self):
        self.tableModel.syncDb()
        self.resizeTableView()
