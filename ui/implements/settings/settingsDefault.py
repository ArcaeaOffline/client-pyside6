import logging

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ui.designer.settings.settingsDefault_ui import Ui_SettingsDefault
from ui.extends.ocr import load_devices_json
from ui.extends.shared.settings import *

logger = logging.getLogger(__name__)


class SettingsDefault(Ui_SettingsDefault, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.settings = Settings(self)

        self.devicesJsonFileSelector.filesSelected.connect(self.fillDevicesComboBox)
        self.devicesJsonFileResetButton.clicked.connect(self.resetDevicesJsonFile)
        self.deviceUuidResetButton.clicked.connect(self.resetDeviceUuid)

        devicesJsonPath = self.settings.devicesJsonFile()
        self.devicesJsonFileSelector.selectFile(devicesJsonPath)
        tesseractPath = self.settings.tesseractPath()
        self.tesseractFileSelector.selectFile(tesseractPath)

        self.devicesJsonFileSelector.accepted.connect(
            self.on_devicesJsonFileSelector_accepted
        )
        self.tesseractFileSelector.accepted.connect(
            self.on_tesseractFileSelector_accepted
        )
        self.knnModelFileSelector.accepted.connect(
            self.on_knnModelFileSelector_accepted
        )
        self.siftDatabaseFileSelector.accepted.connect(
            self.on_siftDatabaseFileSelector_accepted
        )

    def setDevicesJsonFile(self):
        try:
            filename = self.devicesJsonFileSelector.selectedFiles()[0]
            devices = load_devices_json(filename)
            assert isinstance(devices, list)
            self.settings.setDevicesJsonFile(filename)
        except Exception as e:
            logger.exception("set deviceJsonFile error")
            # QMessageBox
            return

    def resetDevicesJsonFile(self):
        self.devicesJsonFileSelector.reset()
        self.settings.resetDevicesJsonFile()

    def on_devicesJsonFileSelector_accepted(self):
        self.setDevicesJsonFile()

    def fillDevicesComboBox(self):
        devicesJsonPath = self.devicesJsonFileSelector.selectedFiles()[0]
        self.devicesComboBox.loadDevicesJson(devicesJsonPath)

        storedDeviceUuid = self.settings.deviceUuid()
        self.devicesComboBox.selectDevice(storedDeviceUuid)

    @Slot()
    def on_devicesComboBox_activated(self):
        device = self.devicesComboBox.currentData()
        if device:
            self.settings.setDeviceUuid(device.uuid)

    def resetDeviceUuid(self):
        self.devicesComboBox.setCurrentIndex(-1)
        self.settings.resetDeviceUuid()

    def setTesseractFile(self):
        file = self.tesseractFileSelector.selectedFiles()[0]
        self.settings.setTesseractPath(file)

    def on_tesseractFileSelector_accepted(self):
        self.setTesseractFile()

    def setKnnModelFile(self):
        file = self.knnModelFileSelector.selectedFiles()[0]
        self.settings.setKnnModelFile(file)

    def on_knnModelFileSelector_accepted(self):
        self.setKnnModelFile()

    def setSiftDatabaseFile(self):
        file = self.siftDatabaseFileSelector.selectedFiles()[0]
        self.settings.setSiftDatabaseFile(file)

    def on_siftDatabaseFileSelector_accepted(self):
        self.setSiftDatabaseFile()
