from PySide6.QtCore import QDir, QFileInfo, QMetaObject, Qt, Signal, Slot
from PySide6.QtWidgets import QFileDialog, QWidget

from ui.designer.components.fileSelector_ui import Ui_FileSelector


class FileSelector(Ui_FileSelector, QWidget):
    accepted = Signal()
    filesSelected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.reset()

        self.elidedLabel.setElideMode(Qt.TextElideMode.ElideMiddle)

        self.accepted.connect(self.filesSelected)
        self.accepted.connect(self.updateLabel)
        self.filesSelected.connect(self.updateLabel)

        self.__mode = self.getOpenFileNames

    def getOpenFileNames(self):
        selectedFiles, filter = QFileDialog.getOpenFileNames(
            self,
            self.__caption,
            self.__startDirectory,
            self.__filter,
            "",
            options=self.__options,
        )
        if selectedFiles:
            self.__selectedFiles = selectedFiles
            self.accepted.emit()

    def getExistingDirectory(self):
        selectedDir = QFileDialog.getExistingDirectory(
            self,
            self.__caption,
            self.__startDirectory,
            QFileDialog.Option.ShowDirsOnly | self.__options,
        )
        if selectedDir:
            self.__selectedFiles = [selectedDir]
            self.accepted.emit()

    def selectFile(self, filename: str):
        fileInfo = QFileInfo(filename)
        if not fileInfo.exists():
            return

        self.__selectedFiles = [fileInfo.absoluteFilePath()]
        self.__startDirectory = fileInfo.dir().absolutePath()
        self.filesSelected.emit()

    def selectedFiles(self):
        return self.__selectedFiles

    def setNameFilters(self, filters: list[str]):
        self.__filter = ";;".join(filters) if filters else ""

    def setOptions(self, options: QFileDialog.Option):
        self.__options = options

    def setMode(self, mode):
        if mode in [self.getOpenFileNames, self.getExistingDirectory]:
            self.__mode = mode
        else:
            raise ValueError("Invalid mode")

    def reset(self):
        self.__selectedFiles = []
        self.__caption = None
        self.__startDirectory = QDir.currentPath()
        self.__filter = ""
        self.__options = QFileDialog.Option(0)

        self.updateLabel()

    def updateLabel(self):
        selectedFiles = self.selectedFiles()

        if not selectedFiles:
            self.elidedLabel.setText("...")
        else:
            self.elidedLabel.setText("<br>".join(selectedFiles))

    @Slot()
    def on_selectButton_clicked(self):
        self.__mode()
