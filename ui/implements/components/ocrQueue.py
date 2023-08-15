from typing import Optional

from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

from ui.designer.components.ocrQueue_ui import Ui_OcrQueue
from ui.extends.components.ocrQueue import (
    OcrChartDelegate,
    OcrImageDelegate,
    OcrQueueModel,
    OcrQueueTableProxyModel,
    OcrScoreDelegate,
)


class OcrQueue(Ui_OcrQueue, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__model: Optional[OcrQueueModel] = None
        self.__tableProxyModel: Optional[OcrQueueTableProxyModel] = None

        self.__firstResizeDone = False
        self.resizeTimer = QTimer(self)
        self.resizeTimer.timeout.connect(self.tableView.resizeRowsToContents)
        self.resizeTimer.timeout.connect(self.tableView.resizeColumnsToContents)

        self.tableView.setItemDelegateForColumn(1, OcrImageDelegate(self.tableView))
        self.tableView.setItemDelegateForColumn(2, OcrChartDelegate(self.tableView))
        self.tableView.setItemDelegateForColumn(3, OcrScoreDelegate(self.tableView))

        tableViewPalette = QPalette(self.tableView.palette())
        highlightColor = QColor(tableViewPalette.color(QPalette.ColorRole.Highlight))
        highlightColor.setAlpha(25)
        tableViewPalette.setColor(QPalette.ColorRole.Highlight, highlightColor)
        self.tableView.setPalette(tableViewPalette)

    def model(self):
        return self.__model

    def setModel(self, model: OcrQueueModel):
        model.dataChanged.connect(self.resizeViewWhenDataChanged)
        model.started.connect(self.ocrStarted)
        model.progress.connect(self.ocrProgress)
        model.finished.connect(self.ocrFinished)
        model.rowsInserted.connect(self.updateProgressBarMaximum)
        model.rowsRemoved.connect(self.updateProgressBarMaximum)
        model.modelReset.connect(self.modelReseted)
        proxyModel = OcrQueueTableProxyModel(self)
        proxyModel.setSourceModel(model)
        self.tableView.setModel(proxyModel)

        if self.__model:
            self.__model.dataChanged.disconnect(self.resizeViewWhenDataChanged)
            self.__model.started.disconnect(self.ocrStarted)
            self.__model.progress.disconnect(self.ocrProgress)
            self.__model.finished.disconnect(self.ocrFinished)
            self.__model.rowsInserted.disconnect(self.updateProgressBarMaximum)
            self.__model.rowsRemoved.disconnect(self.updateProgressBarMaximum)
            self.__model.modelReset.disconnect(self.modelReseted)
        if self.__tableProxyModel:
            self.__tableProxyModel.deleteLater()

        self.__model = model
        self.__tableProxyModel = proxyModel

    def tableProxyModel(self):
        return self.__tableProxyModel

    def setOcrButtonsEnabled(self, __bool: bool):
        self.ocr_addImageButton.setEnabled(__bool)
        self.ocr_removeSelectedButton.setEnabled(__bool)
        self.ocr_removeAllButton.setEnabled(__bool)
        self.ocr_startButton.setEnabled(__bool)
        self.ocr_acceptSelectedButton.setEnabled(__bool)
        self.ocr_acceptAllButton.setEnabled(__bool)
        self.ocr_ignoreValidateCheckBox.setEnabled(__bool)

    def resizeTableView(self):
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

    def resizeViewWhenDataChanged(self):
        if not self.__firstResizeDone:
            self.resizeTableView()
            self.__firstResizeDone = True

    def ocrStarted(self):
        self.setOcrButtonsEnabled(False)

    def updateProgressBarMaximum(self):
        self.progressBar.setMaximum(self.model().rowCount())

    @Slot(int)
    def ocrProgress(self, progress: int):
        self.progressBar.setValue(progress)

    def ocrFinished(self):
        self.resizeTableView()
        self.setOcrButtonsEnabled(True)

    def modelReseted(self):
        self.progressBar.setMaximum(0)

    @Slot()
    def on_ocr_removeSelectedButton_clicked(self):
        if self.model():
            rows = [
                modelIndex.row()
                for modelIndex in self.tableView.selectionModel().selectedRows(0)
            ]
            self.model().removeItems(rows)

    @Slot()
    def on_ocr_acceptSelectedButton_clicked(self):
        if self.model():
            ignoreValidate = (
                self.ocr_ignoreValidateCheckBox.checkState() == Qt.CheckState.Checked
            )
            rows = [
                modelIndex.row()
                for modelIndex in self.tableView.selectionModel().selectedRows(0)
            ]
            self.model().acceptItems(rows, ignoreValidate)

    @Slot()
    def on_ocr_acceptAllButton_clicked(self):
        if self.model():
            ignoreValidate = (
                self.ocr_ignoreValidateCheckBox.checkState() == Qt.CheckState.Checked
            )
            self.model().acceptAllItems(ignoreValidate)
