from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QLabel, QPushButton

from ui.implements.components.devicesComboBox import DevicesComboBox
from ui.implements.components.fileSelector import FileSelector
from ui.implements.settings.settingsBaseWidget import SettingsBaseWidget


class SettingsOcr(SettingsBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        if self.settings.devicesJsonFile():
            self.devicesJsonValueWidget.selectFile(self.settings.devicesJsonFile())
        self.devicesJsonValueWidget.filesSelected.connect(self.setDevicesJson)
        self.devicesJsonResetButton.clicked.connect(self.resetDevicesJson)
        self.insertItem(
            "devicesJson",
            self.devicesJsonLabel,
            self.devicesJsonValueWidget,
            self.devicesJsonResetButton,
        )

        if self.settings.deviceUuid():
            self.deviceUuidValueWidget.selectDevice(self.settings.deviceUuid())
        self.deviceUuidValueWidget.activated.connect(self.setDeviceUuid)
        self.deviceUuidResetButton.clicked.connect(self.resetDeviceUuid)
        self.insertItem(
            "deviceUuid",
            self.deviceUuidLabel,
            self.deviceUuidValueWidget,
            self.deviceUuidResetButton,
        )

        if self.settings.knnModelFile():
            self.knnModelFileValueWidget.selectFile(self.settings.knnModelFile())
        self.knnModelFileValueWidget.filesSelected.connect(self.setKnnModelFile)
        self.knnModelFileResetButton.clicked.connect(self.resetKnnModelFile)
        self.insertItem(
            "knnModelFile",
            self.knnModelFileLabel,
            self.knnModelFileValueWidget,
            self.knnModelFileResetButton,
        )

        if self.settings.b30KnnModelFile():
            self.b30KnnModelFileValueWidget.selectFile(self.settings.b30KnnModelFile())
        self.b30KnnModelFileValueWidget.filesSelected.connect(self.setB30KnnModelFile)
        self.b30KnnModelFileResetButton.clicked.connect(self.resetB30KnnModelFile)
        self.insertItem(
            "b30KnnModelFile",
            self.b30KnnModelFileLabel,
            self.b30KnnModelFileValueWidget,
            self.b30KnnModelFileResetButton,
        )

        if self.settings.siftDatabaseFile():
            self.siftDatabaseFileValueWidget.selectFile(
                self.settings.siftDatabaseFile()
            )
        self.siftDatabaseFileValueWidget.filesSelected.connect(self.setSiftDatabaseFile)
        self.siftDatabaseFileResetButton.clicked.connect(self.resetSiftDatabaseFile)
        self.insertItem(
            "siftDatabaseFile",
            self.siftDatabaseFileLabel,
            self.siftDatabaseFileValueWidget,
            self.siftDatabaseFileResetButton,
        )

        if self.settings.phashDatabaseFile():
            self.phashDatabaseFileValueWidget.selectFile(
                self.settings.phashDatabaseFile()
            )
        self.phashDatabaseFileValueWidget.filesSelected.connect(
            self.setPHashDatabaseFile
        )
        self.phashDatabaseFileResetButton.clicked.connect(self.resetPHashDatabaseFile)
        self.insertItem(
            "phashDatabaseFile",
            self.phashDatabaseFileLabel,
            self.phashDatabaseFileValueWidget,
            self.phashDatabaseFileResetButton,
        )

    def setDevicesJson(self):
        selectedFile = self.devicesJsonValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setDevicesJsonFile(file)
            self.fillDeviceUuidComboBox()

    def fillDeviceUuidComboBox(self):
        devicesJsonPath = self.devicesJsonValueWidget.selectedFiles()[0]
        self.deviceUuidValueWidget.loadDevicesJson(devicesJsonPath)

        storedDeviceUuid = self.settings.deviceUuid()
        self.deviceUuidValueWidget.selectDevice(storedDeviceUuid)

    def resetDevicesJson(self):
        self.deviceUuidValueWidget.clear()
        self.devicesJsonValueWidget.reset()
        self.settings.resetDeviceUuid()
        self.settings.resetDevicesJsonFile()

    def setDeviceUuid(self):
        if device := self.deviceUuidValueWidget.currentData():
            self.settings.setDeviceUuid(device.uuid)

    def resetDeviceUuid(self):
        self.deviceUuidValueWidget.setCurrentIndex(-1)
        self.settings.resetDeviceUuid()

    def setKnnModelFile(self):
        selectedFile = self.knnModelFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setKnnModelFile(file)

    def resetKnnModelFile(self):
        self.knnModelFileValueWidget.reset()
        self.settings.resetKnnModelFile()

    def setB30KnnModelFile(self):
        selectedFile = self.b30KnnModelFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setB30KnnModelFile(file)

    def resetB30KnnModelFile(self):
        self.b30KnnModelFileValueWidget.reset()
        self.settings.resetB30KnnModelFile()

    def setSiftDatabaseFile(self):
        selectedFile = self.siftDatabaseFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setSiftDatabaseFile(file)

    def resetSiftDatabaseFile(self):
        self.siftDatabaseFileValueWidget.reset()
        self.settings.resetSiftDatabaseFile()

    def setPHashDatabaseFile(self):
        selectedFile = self.phashDatabaseFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setPHashDatabaseFile(file)

    def resetPHashDatabaseFile(self):
        self.phashDatabaseFileValueWidget.reset()
        self.settings.resetPHashDatabaseFile()

    def setupUi(self, *args):
        self.devicesJsonLabel = QLabel(self)
        self.devicesJsonValueWidget = FileSelector(self)
        self.devicesJsonResetButton = QPushButton(self)

        self.deviceUuidLabel = QLabel(self)
        self.deviceUuidValueWidget = DevicesComboBox(self)
        self.deviceUuidResetButton = QPushButton(self)

        self.knnModelFileLabel = QLabel(self)
        self.knnModelFileValueWidget = FileSelector(self)
        self.knnModelFileResetButton = QPushButton(self)

        self.b30KnnModelFileLabel = QLabel(self)
        self.b30KnnModelFileValueWidget = FileSelector(self)
        self.b30KnnModelFileResetButton = QPushButton(self)

        self.siftDatabaseFileLabel = QLabel(self)
        self.siftDatabaseFileValueWidget = FileSelector(self)
        self.siftDatabaseFileResetButton = QPushButton(self)

        self.phashDatabaseFileLabel = QLabel(self)
        self.phashDatabaseFileValueWidget = FileSelector(self)
        self.phashDatabaseFileResetButton = QPushButton(self)

        super().setupUi(self)
        self.retranslateUi()

    def retranslateUi(self, *args):
        super().retranslateUi(self)

        # fmt: off
        self.setTitle(QCoreApplication.translate("Settings", "ocr.title"))

        self.devicesJsonLabel.setText(QCoreApplication.translate("Settings", "ocr.devicesJson.label"))
        self.devicesJsonResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.deviceUuidLabel.setText(QCoreApplication.translate("Settings", "ocr.deviceUuid.label"))
        self.deviceUuidResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.knnModelFileLabel.setText(QCoreApplication.translate("Settings", "ocr.knnModelFile.label"))
        self.knnModelFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.b30KnnModelFileLabel.setText(QCoreApplication.translate("Settings", "ocr.b30KnnModelFile.label"))
        self.b30KnnModelFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.siftDatabaseFileLabel.setText(QCoreApplication.translate("Settings", "ocr.siftDatabaseFile.label"))
        self.siftDatabaseFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.phashDatabaseFileLabel.setText(QCoreApplication.translate("Settings", "ocr.phashDatabaseFile.label"))
        self.phashDatabaseFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))
        # fmt: on
