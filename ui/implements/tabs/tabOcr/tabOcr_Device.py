import logging

import cv2

# from arcaea_offline_ocr_device_creation_wizard.implements.wizard import Wizard
from arcaea_offline_ocr.device.v1.definition import DeviceV1
from arcaea_offline_ocr.device.v2.definition import DeviceV2
from arcaea_offline_ocr.sift_db import SIFTDatabase
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget

from ui.designer.tabs.tabOcr.tabOcr_Device_ui import Ui_TabOcr_Device
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.shared.settings import Settings
from ui.extends.tabs.tabOcr.tabOcr_Device import (
    ScoreConverter,
    TabDeviceV2AutoRoisOcrRunnable,
    TabDeviceV2OcrRunnable,
)

logger = logging.getLogger(__name__)


class TabOcr_Device(Ui_TabOcr_Device, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openWizardButton.setEnabled(False)

        self.deviceFileSelector.filesSelected.connect(self.deviceFileSelected)
        self.knnModelSelector.filesSelected.connect(self.knnModelFileSelected)
        self.tesseractFileSelector.filesSelected.connect(
            self.tesseractFileSelectorFilesSelected
        )
        self.siftDatabaseSelector.filesSelected.connect(self.siftDatabaseFileSelected)

        settings = Settings()
        logger.info("Applying default settings...")
        self.deviceFileSelector.selectFile(settings.devicesJsonFile())
        self.tesseractFileSelector.selectFile(settings.tesseractPath())
        self.deviceComboBox.selectDevice(settings.deviceUuid())
        self.knnModelSelector.selectFile(settings.knnModelFile())
        self.siftDatabaseSelector.selectFile(settings.siftDatabaseFile())

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueue.setModel(self.ocrQueueModel)
        self.ocrQueueProxyModel = self.ocrQueue.tableProxyModel()

    @Slot()
    def on_openWizardButton_clicked(self):
        # wizard = Wizard(self)
        # wizard.open()
        pass

    @Slot()
    def on_deviceUseAutoFactorCheckBox_stateChanged(self):
        checkState = self.deviceUseAutoFactorCheckBox.checkState()
        if checkState == Qt.CheckState.Checked:
            self.deviceDependenciesStackedWidget.setCurrentIndex(1)
            self.deviceComboBox.setCurrentIndex(-1)
            self.deviceFileSelector.setEnabled(False)
            self.deviceComboBox.setEnabled(False)
        else:
            self.deviceFileSelector.setEnabled(True)
            self.deviceComboBox.setEnabled(True)

    @Slot()
    def on_deviceComboBox_currentIndexChanged(self):
        self.changeDeviceDepStackedWidget()

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
            QApplication.processEvents()
        self.ocrQueue.resizeTableView()

    @Slot()
    def on_ocr_startButton_clicked(self):
        for row in range(self.ocrQueueModel.rowCount()):
            index = self.ocrQueueModel.index(row, 0)
            imagePath = index.data(OcrQueueModel.ImagePathRole)
            if self.deviceUseAutoFactorCheckBox.checkState() == Qt.CheckState.Checked:
                runnable = TabDeviceV2AutoRoisOcrRunnable(
                    imagePath,
                    self.knnModel,
                    self.siftDatabase,
                )
            else:
                runnable = TabDeviceV2OcrRunnable(
                    imagePath,
                    self.deviceComboBox.currentData(),
                    self.knnModel,
                    self.siftDatabase,
                )
            self.ocrQueueModel.setData(index, runnable, OcrQueueModel.OcrRunnableRole)
            self.ocrQueueModel.setData(
                index,
                ScoreConverter.deviceV2,
                OcrQueueModel.ProcessOcrResultFuncRole,
            )
        self.ocrQueueModel.startQueue()

    @Slot()
    def on_ocr_removeAllButton_clicked(self):
        self.ocrQueueModel.clear()
