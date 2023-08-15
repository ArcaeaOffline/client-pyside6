import cv2
import pytesseract

# from arcaea_offline_ocr_device_creation_wizard.implements.wizard import Wizard
from arcaea_offline_ocr.device.v1.definition import DeviceV1
from arcaea_offline_ocr.device.v2.definition import DeviceV2
from arcaea_offline_ocr.sift_db import SIFTDatabase
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QWidget

from ui.designer.tabs.tabOcr_ui import Ui_TabOcr
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.settings import Settings
from ui.extends.tabs.tabOcr import ScoreInsertConverter, TabDeviceV2OcrRunnable


class TabOcr(Ui_TabOcr, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openWizardButton.setEnabled(False)

        self.deviceComboBox.currentIndexChanged.connect(
            self.changeDeviceDepStackedWidget
        )

        self.deviceFileSelector.filesSelected.connect(self.deviceFileSelected)
        self.knnModelSelector.filesSelected.connect(self.knnModelFileSelected)
        self.tesseractFileSelector.filesSelected.connect(
            self.tesseractFileSelectorFilesSelected
        )
        self.siftDatabaseSelector.filesSelected.connect(self.siftDatabaseFileSelected)

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

    def changeDeviceDepStackedWidget(self):
        device = self.deviceComboBox.currentData()
        if isinstance(device, (DeviceV1, DeviceV2)):
            self.deviceDependenciesStackedWidget.setCurrentIndex(device.version - 1)

    def deviceFileSelected(self):
        selectedFiles = self.deviceFileSelector.selectedFiles()
        if selectedFiles:
            file = selectedFiles[0]
            self.deviceComboBox.loadDevicesJson(file)

    def knnModelFileSelected(self):
        selectedFiles = self.knnModelSelector.selectedFiles()
        if selectedFiles:
            self.knnModel = cv2.ml.KNearest.load(selectedFiles[0])

    def tesseractFileSelectorFilesSelected(self):
        selectedFiles = self.tesseractFileSelector.selectedFiles()
        if selectedFiles:
            pytesseract.pytesseract.tesseract_cmd = selectedFiles[0]

    def siftDatabaseFileSelected(self):
        selectedFiles = self.siftDatabaseSelector.selectedFiles()
        if selectedFiles:
            self.siftDatabase = SIFTDatabase(selectedFiles[0])

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
                imagePath,
                self.deviceComboBox.currentData(),
                self.knnModel,
                self.siftDatabase,
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
