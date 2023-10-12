from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QLabel, QPushButton

from ui.implements.components.fileSelector import FileSelector
from ui.implements.settings.settingsBaseWidget import SettingsBaseWidget


class SettingsOcr(SettingsBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

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

    def setPHashDatabaseFile(self):
        selectedFile = self.phashDatabaseFileValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setPHashDatabaseFile(file)

    def resetPHashDatabaseFile(self):
        self.phashDatabaseFileValueWidget.reset()
        self.settings.resetPHashDatabaseFile()

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
