import pytesseract

# from arcaea_offline_ocr_device_creation_wizard.implements.wizard import Wizard
from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFileDialog, QHeaderView, QWidget

from ui.designer.tabs.tabOcr_ui import Ui_TabOcr
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.settings import Settings
from ui.extends.tabs.tabOcr import TabDeviceV2OcrRunnable, ScoreInsertConverter


class TabOcr(Ui_TabOcr, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openWizardButton.setEnabled(False)

        self.deviceFileSelector.filesSelected.connect(self.deviceFileSelected)
        self.tesseractFileSelector.filesSelected.connect(
            self.tesseractFileSelectorFilesSelected
        )

        settings = Settings()
        self.deviceFileSelector.selectFile(settings.devicesJsonFile())
        self.tesseractFileSelector.selectFile(settings.tesseractPath())
        self.deviceComboBox.selectDevice(settings.deviceUuid())

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueue.setModel(self.ocrQueueModel)
        self.ocrQueueProxyModel = self.ocrQueue.tableProxyModel()

    @Slot()
    def on_openWizardButton_clicked(self):
        # wizard = Wizard(self)
        # wizard.open()
        pass

    def deviceFileSelected(self):
        selectedFiles = self.deviceFileSelector.selectedFiles()
        if selectedFiles:
            file = selectedFiles[0]
            self.deviceComboBox.loadDevicesJson(file)

    def tesseractFileSelectorFilesSelected(self):
        selectedFiles = self.tesseractFileSelector.selectedFiles()
        if selectedFiles:
            pytesseract.pytesseract.tesseract_cmd = selectedFiles[0]

    @Slot()
    def on_ocr_addImageButton_clicked(self):
        files, _filter = QFileDialog.getOpenFileNames(
            self, None, "", "Image Files (*.png *.jpg *.jpeg *.bmp *.webp);;*"
        )
        for file in files:
            self.ocrQueueModel.addItem(file)
        self.ocrQueue.resizeTableView()

    @Slot()
    def on_ocr_startButton_clicked(self):
        for row in range(self.ocrQueueModel.rowCount()):
            index = self.ocrQueueModel.index(row, 0)
            imagePath = index.data(OcrQueueModel.ImagePathRole)
            runnable = TabDeviceV2OcrRunnable(
                imagePath, self.deviceComboBox.currentData(), self.knn, self.siftDb
            )
            self.ocrQueueModel.setData(index, runnable, OcrQueueModel.OcrRunnableRole)
            self.ocrQueueModel.setData(
                index,
                ScoreInsertConverter.deviceV2,
                OcrQueueModel.ProcessOcrResultFuncRole,
            )
        self.ocrQueueModel.startQueue()

    @Slot()
    def on_ocr_removeAllButton_clicked(self):
        self.ocrQueueModel.clear()
