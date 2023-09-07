from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QLabel, QPushButton

from ui.implements.components.fileSelector import FileSelector
from ui.implements.settings.settingsBaseWidget import SettingsBaseWidget


class SettingsAndreal(SettingsBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        if self.settings.andrealFolder():
            self.andrealFolderValueWidget.selectFile(self.settings.andrealFolder())
        self.andrealFolderValueWidget.filesSelected.connect(self.setAndrealFolder)
        self.andrealFolderResetButton.clicked.connect(self.resetAndrealFolder)
        self.insertItem(
            "andrealFolder",
            self.andrealFolderLabel,
            self.andrealFolderValueWidget,
            self.andrealFolderResetButton,
        )

        if self.settings.andrealExecutable():
            self.andrealExecutableValueWidget.selectFile(
                self.settings.andrealExecutable()
            )
        self.andrealExecutableValueWidget.filesSelected.connect(
            self.setAndrealExecutable
        )
        self.andrealExecutableResetButton.clicked.connect(self.resetAndrealExecutable)
        self.insertItem(
            "andrealExecutable",
            self.andrealExecutableLabel,
            self.andrealExecutableValueWidget,
            self.andrealExecutableResetButton,
        )

    def setAndrealFolder(self):
        selectedFile = self.andrealFolderValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setAndrealFolder(file)

    def resetAndrealFolder(self):
        self.andrealFolderValueWidget.reset()
        self.settings.resetAndrealFolder()

    def setAndrealExecutable(self):
        selectedFile = self.andrealExecutableValueWidget.selectedFiles()
        if selectedFile and selectedFile[0]:
            file = selectedFile[0]
            self.settings.setAndrealExecutable(file)

    def resetAndrealExecutable(self):
        self.andrealExecutableValueWidget.reset()
        self.settings.resetAndrealExecutable()

    def setupUi(self, *args):
        self.andrealFolderLabel = QLabel(self)
        self.andrealFolderValueWidget = FileSelector(self)
        self.andrealFolderResetButton = QPushButton(self)

        self.andrealExecutableLabel = QLabel(self)
        self.andrealExecutableValueWidget = FileSelector(self)
        self.andrealExecutableResetButton = QPushButton(self)

        super().setupUi(self)
        self.retranslateUi()

    def retranslateUi(self, *args):
        super().retranslateUi(self)

        # fmt: off
        self.setTitle(QCoreApplication.translate("Settings", "andreal.title"))

        self.andrealFolderLabel.setText(QCoreApplication.translate("Settings", "andreal.andrealFolder.label"))
        self.andrealFolderResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))

        self.andrealExecutableLabel.setText(QCoreApplication.translate("Settings", "andreal.andrealExecutable.label"))
        self.andrealExecutableResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))
        # fmt: on
