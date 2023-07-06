import pytesseract
from arcaea_offline_ocr_device_creation_wizard.implements.wizard import Wizard
from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QFileDialog, QWidget

from ui.designer.tabs.tabOcr_ui import Ui_TabOcr
from ui.extends.settings import Settings
from ui.extends.tabs.tabOcr import (
    ImageDelegate,
    OcrQueueModel,
    OcrQueueTableProxyModel,
    TableChartDelegate,
    TableScoreDelegate,
)


class TabOcr(Ui_TabOcr, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.deviceFileSelector.filesSelected.connect(self.deviceFileSelected)
        self.tesseractFileSelector.filesSelected.connect(
            self.tesseractFileSelectorFilesSelected
        )

        settings = Settings()
        self.deviceFileSelector.selectFile(settings.devicesJsonFile())
        self.tesseractFileSelector.selectFile(settings.tesseractPath())
        self.deviceComboBox.selectDevice(settings.deviceUuid())

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueueModel.dataChanged.connect(self.resizeViewWhenScoreChanged)
        self.ocrQueueModel.started.connect(self.ocrStarted)
        self.ocrQueueModel.finished.connect(self.ocrFinished)
        self.ocrQueueProxyModel = OcrQueueTableProxyModel(self)
        self.ocrQueueProxyModel.setSourceModel(self.ocrQueueModel)

        self.tableView.setModel(self.ocrQueueProxyModel)
        self.tableView.setItemDelegateForColumn(1, ImageDelegate(self.tableView))
        self.tableView.setItemDelegateForColumn(2, TableChartDelegate(self.tableView))
        self.tableView.setItemDelegateForColumn(3, TableScoreDelegate(self.tableView))

        tableViewPalette = QPalette(self.tableView.palette())
        highlightColor = QColor(tableViewPalette.color(QPalette.ColorRole.Highlight))
        highlightColor.setAlpha(25)
        tableViewPalette.setColor(QPalette.ColorRole.Highlight, highlightColor)
        self.tableView.setPalette(tableViewPalette)

    @Slot(QModelIndex, QModelIndex, list)
    def resizeViewWhenScoreChanged(
        self, topleft: QModelIndex, bottomRight: QModelIndex, roles: list[int]
    ):
        if OcrQueueModel.ScoreInsertRole in roles:
            rows = [*range(topleft.row(), bottomRight.row() + 1)]
            [self.tableView.resizeRowToContents(row) for row in rows]
            self.tableView.resizeColumnsToContents()

    @Slot()
    def on_openWizardButton_clicked(self):
        wizard = Wizard(self)
        wizard.open()

    def deviceFileSelected(self):
        selectedFiles = self.deviceFileSelector.selectedFiles()
        if selectedFiles:
            file = selectedFiles[0]
            self.deviceComboBox.loadDevicesJson(file)

    def tesseractFileSelectorFilesSelected(self):
        selectedFiles = self.tesseractFileSelector.selectedFiles()
        if selectedFiles:
            pytesseract.pytesseract.tesseract_cmd = selectedFiles[0]

    def setOcrButtonsEnabled(self, __bool: bool):
        self.ocr_addImageButton.setEnabled(__bool)
        self.ocr_removeSelectedButton.setEnabled(__bool)
        self.ocr_removeAllButton.setEnabled(__bool)
        self.ocr_startButton.setEnabled(__bool)
        self.ocr_acceptSelectedButton.setEnabled(__bool)
        self.ocr_acceptAllButton.setEnabled(__bool)
        self.ocr_ignoreValidateCheckBox.setEnabled(__bool)

    @Slot()
    def on_ocr_addImageButton_clicked(self):
        files, _filter = QFileDialog.getOpenFileNames(
            self, None, "", "Image Files (*.png *.jpg *.jpeg *.bmp *.webp);;*"
        )
        for file in files:
            self.ocrQueueModel.addItem(file)
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

    @Slot()
    def on_ocr_startButton_clicked(self):
        self.ocrQueueModel.startQueue(self.deviceComboBox.currentData())

    def ocrStarted(self):
        self.setOcrButtonsEnabled(False)

    def ocrFinished(self):
        self.setOcrButtonsEnabled(True)

    @Slot()
    def on_ocr_removeSelectedButton_clicked(self):
        rows = [
            modelIndex.row()
            for modelIndex in self.tableView.selectionModel().selectedRows(0)
        ]
        self.ocrQueueModel.removeItems(rows)

    @Slot()
    def on_ocr_removeAllButton_clicked(self):
        self.ocrQueueModel.clear()

    @Slot()
    def on_ocr_acceptSelectedButton_clicked(self):
        ignoreValidate = (
            self.ocr_ignoreValidateCheckBox.checkState() == Qt.CheckState.Checked
        )
        rows = [
            modelIndex.row()
            for modelIndex in self.tableView.selectionModel().selectedRows(0)
        ]
        self.ocrQueueModel.acceptItems(rows, ignoreValidate)

    @Slot()
    def on_ocr_acceptAllButton_clicked(self):
        ignoreValidate = (
            self.ocr_ignoreValidateCheckBox.checkState() == Qt.CheckState.Checked
        )
        self.ocrQueueModel.acceptAllItems(ignoreValidate)
