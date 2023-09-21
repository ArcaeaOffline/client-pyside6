import json
import logging
import time

from arcaea_offline.database import Database
from arcaea_offline.external.andreal.api_data import (
    AndrealImageGeneratorApiDataConverter,
)
from arcaea_offline.models import Chart
from arcaea_offline.utils.rating import rating_class_to_short_text
from PySide6.QtCore import QDir, QFileInfo, Qt, Slot
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QButtonGroup, QFileDialog, QLabel, QMessageBox, QWidget

from ui.designer.tabs.tabTools.tabTools_Andreal_ui import Ui_TabTools_Andreal
from ui.extends.shared.settings import ANDREAL_EXECUTABLE, ANDREAL_FOLDER
from ui.extends.tabs.tabTools.tabTools_Andreal import AndrealHelper
from ui.implements.components.chartSelector import ChartSelector
from ui.implements.components.songIdSelector import SongIdSelectorMode

logger = logging.getLogger(__name__)


class PreviewLabel(QLabel):
    ...


class ChartSelectorDialog(ChartSelector):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Dialog, True)
        self.setSongIdSelectorMode(SongIdSelectorMode.Chart)


class TabTools_Andreal(Ui_TabTools_Andreal, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.db = Database()

        self.andrealHelper = AndrealHelper(self)

        self.andrealFolderSelector.setMode(
            self.andrealFolderSelector.getExistingDirectory
        )

        self.andrealFolderSelector.filesSelected.connect(self.setHelperPaths)
        self.andrealExecutableSelector.filesSelected.connect(self.setHelperPaths)

        self.andrealFolderSelector.connectSettings(ANDREAL_FOLDER)
        self.andrealExecutableSelector.connectSettings(ANDREAL_EXECUTABLE)

        self.generateImageButton.clicked.connect(self.requestGenerate)

        self.infoChart: Chart | None = None

        self.previewJsonPath = None
        self.generateJsonPath = None
        self.generateImageFormat = None

        self.andrealHelper.error.connect(self.generateError)
        self.andrealHelper.ready.connect(self.generateReady)
        self.andrealHelper.finished.connect(self.generateFinished)

        self.imageTypeButtonGroup = QButtonGroup(self)
        self.imageTypeButtonGroup.addButton(self.imageType_infoRadioButton, 0)
        self.imageTypeButtonGroup.addButton(self.imageType_bestRadioButton, 1)
        self.imageTypeButtonGroup.addButton(self.imageType_best30RadioButton, 2)

        self.imageFormatButtonGroup = QButtonGroup(self)
        self.imageFormatButtonGroup.addButton(self.imageFormat_jpgRadioButton, 0)
        self.imageFormatButtonGroup.addButton(self.imageFormat_pngRadioButton, 1)

        self.imageTypeButtonGroup.idToggled.connect(self.fillImageVersionComboBox)
        self.fillImageVersionComboBox()

    def setHelperPaths(self):
        if selectedFiles := self.andrealFolderSelector.selectedFiles():
            self.andrealHelper.andrealFolder = selectedFiles[0]
        if selectedFiles := self.andrealExecutableSelector.selectedFiles():
            self.andrealHelper.andrealExecutable = selectedFiles[0]

    def imageFormat(self):
        buttonId = self.imageFormatButtonGroup.checkedId()
        return ["jpg", "png"][buttonId] if buttonId > -1 else None

    def imageType(self):
        buttonId = self.imageTypeButtonGroup.checkedId()
        return ["info", "best", "best30"][buttonId] if buttonId > -1 else None

    def fillImageVersionComboBox(self):
        imageType = self.imageType()
        if not imageType:
            return

        self.imageVersionComboBox.clear()
        if imageType in ["info", "best"]:
            self.imageVersionComboBox.addItem("3", 3)
            self.imageVersionComboBox.addItem("2", 2)
            self.imageVersionComboBox.addItem("1", 1)
        elif imageType == "best30":
            self.imageVersionComboBox.addItem("2", 2)
            self.imageVersionComboBox.addItem("1", 1)

    def imageVersion(self):
        return self.imageVersionComboBox.currentData()

    def requestComplete(self) -> bool:
        if not self.imageType():
            return False

        imageType = self.imageType()
        if imageType == "best" and not self.infoChart:
            return False

        return self.imageVersion() is not None

    def getAndrealArguments(self, jsonFile: str, *, preview: bool = False):
        if not self.requestComplete():
            return

        arguments = [
            str(self.imageType()),
            f'--json-file="{jsonFile}"',
            f"--img-version={self.imageVersion()}",
        ]
        if self.andrealFolderSelector.selectedFiles():
            arguments.append(
                f'--path="{self.andrealFolderSelector.selectedFiles()[0]}"'
            )
        if preview:
            arguments.extend(["--img-format=jpg", "--img-quality=20"])
        else:
            arguments.append(f"--img-format={self.imageFormat()}")
            if self.imageFormat() == "jpg":
                arguments.append(f"--img-quality={self.jpgQualitySpinBox.value()}")
        return arguments

    def getAndrealJsonContent(self):
        if not self.requestComplete():
            return None

        imageType = self.imageType()
        if imageType == "best" and not self.infoChart:
            return

        jsonContentDict = {}
        with self.db.sessionmaker() as session:
            converter = AndrealImageGeneratorApiDataConverter(session)
            if imageType == "info":
                jsonContentDict = converter.user_info()
            elif imageType == "best":
                jsonContentDict = converter.user_best(
                    self.infoChart.song_id, self.infoChart.rating_class
                )
            elif imageType == "best30":
                jsonContentDict = converter.user_best30()
        return json.dumps(jsonContentDict, ensure_ascii=False)

    def getAndrealJsonFileName(self):
        if not self.requestComplete():
            return None

        imageType = self.imageType()
        timestamp = int(time.time() * 1000)

        fileNameParts = ["andreal", imageType]
        if imageType == "best":
            fileNameParts.extend(
                [
                    self.infoChart.song_id,
                    rating_class_to_short_text(self.infoChart.rating_class).lower(),
                ]
            )
        fileNameParts.append(timestamp)
        fileNameParts = [str(i) for i in fileNameParts]
        fileName = "-".join(fileNameParts)
        return f"{fileName}.json"

    def getTempAndrealJsonPath(self):
        if fileName := self.getAndrealJsonFileName():
            return QDir.temp().filePath(fileName)
        else:
            return None

    @Slot()
    def on_exportJsonButton_clicked(self):
        content = self.getAndrealJsonContent()
        fileName = self.getAndrealJsonFileName()
        if not content or not fileName:
            return

        saveFileName, _ = QFileDialog.getSaveFileName(self, None, fileName)
        if not saveFileName:
            return
        with open(saveFileName, "w", encoding="utf-8") as jf:
            jf.write(content)

    def requestGenerate(self):
        jsonPath = self.getTempAndrealJsonPath()
        if not jsonPath:
            return

        self.generateImageButton.setEnabled(False)
        self.generateJsonPath = jsonPath
        self.generateImageFormat = self.imageFormat()
        with open(jsonPath, "w", encoding="utf-8") as jf:
            jf.write(self.getAndrealJsonContent())

        self.andrealHelper.request(jsonPath, self.getAndrealArguments(jsonPath))

    def generateFinished(self):
        self.generateImageButton.setEnabled(True)

    def generateError(self, jsonPath: str, errorMsg: str):
        if jsonPath != self.generateJsonPath:
            return
        QMessageBox.critical(self, "Generate Error", errorMsg)

    def generateReady(self, jsonPath: str, imageBytes: bytes):
        if jsonPath != self.generateJsonPath:
            return

        if not imageBytes:
            QMessageBox.critical(self, "Generate Error", "Empty bytes received.")
            return

        qImage = QImage.fromData(imageBytes)

        filePathParts = jsonPath.split(".")
        filePathParts[-1] = self.generateImageFormat
        filePath = ".".join(filePathParts)
        fileName = QFileInfo(filePath).fileName()

        saveFileName, _ = QFileDialog.getSaveFileName(self, None, fileName)
        if not saveFileName:
            return
        qImage.save(saveFileName, self.generateImageFormat)
