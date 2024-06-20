from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QLabel, QPushButton

from core.settings import SettingsKeys, settings
from ui.implements.components.fileSelector import FileSelector
from ui.implements.settings.settingsBaseWidget import SettingsBaseWidget


class SettingsOcr(SettingsBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        if knnModelFile := settings.stringValue(SettingsKeys.Ocr.KnnModelFile):
            self.knnModelFileValueWidget.selectFile(knnModelFile)
        self.knnModelFileValueWidget.filesSelected.connect(self.setKnnModelFile)
        self.knnModelFileResetButton.clicked.connect(self.resetKnnModelFile)
        self.insertItem(
            "knnModelFile",
            self.knnModelFileLabel,
            self.knnModelFileValueWidget,
            self.knnModelFileResetButton,
        )

        if b30KnnModelFile := settings.stringValue(SettingsKeys.Ocr.B30KnnModelFile):
            self.b30KnnModelFileValueWidget.selectFile(b30KnnModelFile)
        self.b30KnnModelFileValueWidget.filesSelected.connect(self.setB30KnnModelFile)
        self.b30KnnModelFileResetButton.clicked.connect(self.resetB30KnnModelFile)
        self.insertItem(
            "b30KnnModelFile",
            self.b30KnnModelFileLabel,
            self.b30KnnModelFileValueWidget,
            self.b30KnnModelFileResetButton,
        )

        if phashDatabaseFile := settings.stringValue(
            SettingsKeys.Ocr.PhashDatabaseFile
        ):
            self.phashDatabaseFileValueWidget.selectFile(phashDatabaseFile)
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

    def setKnnModelFile(self):
        selectedFile = self.knnModelFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            settings.setValue(SettingsKeys.Ocr.KnnModelFile, file)

    def resetKnnModelFile(self):
        self.knnModelFileValueWidget.reset()
        settings.setValue(SettingsKeys.Ocr.KnnModelFile, None)

    def setB30KnnModelFile(self):
        selectedFile = self.b30KnnModelFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            settings.setValue(SettingsKeys.Ocr.B30KnnModelFile, file)

    def resetB30KnnModelFile(self):
        self.b30KnnModelFileValueWidget.reset()
        settings.setValue(SettingsKeys.Ocr.B30KnnModelFile, None)

    def setPHashDatabaseFile(self):
        selectedFile = self.phashDatabaseFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            settings.setValue(SettingsKeys.Ocr.PhashDatabaseFile, file)

    def resetPHashDatabaseFile(self):
        self.phashDatabaseFileValueWidget.reset()
        settings.setValue(SettingsKeys.Ocr.PhashDatabaseFile, None)

    def setupUi(self, *args):
        self.knnModelFileLabel = QLabel(self)
        self.knnModelFileValueWidget = FileSelector(self)
        self.knnModelFileResetButton = QPushButton(self)

        self.b30KnnModelFileLabel = QLabel(self)
        self.b30KnnModelFileValueWidget = FileSelector(self)
        self.b30KnnModelFileResetButton = QPushButton(self)

        self.phashDatabaseFileLabel = QLabel(self)
        self.phashDatabaseFileValueWidget = FileSelector(self)
        self.phashDatabaseFileResetButton = QPushButton(self)

        super().setupUi(self)
        self.retranslateUi()

    def retranslateUi(self, *args):
        super().retranslateUi(self)

        # fmt: off
        self.setTitle(QCoreApplication.translate("Settings", "ocr.title"))

        self.knnModelFileLabel.setText(QCoreApplication.translate("Settings", "ocr.knnModelFile.label"))
        self.knnModelFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.b30KnnModelFileLabel.setText(QCoreApplication.translate("Settings", "ocr.b30KnnModelFile.label"))
        self.b30KnnModelFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.phashDatabaseFileLabel.setText(QCoreApplication.translate("Settings", "ocr.phashDatabaseFile.label"))
        self.phashDatabaseFileResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))
        # fmt: on
