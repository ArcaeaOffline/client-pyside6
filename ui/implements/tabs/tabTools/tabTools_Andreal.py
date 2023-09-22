import json
import logging
import time

from arcaea_offline.database import Database
from arcaea_offline.external.andreal.api_data import (
    AndrealImageGeneratorApiDataConverter,
)
from arcaea_offline.models import Chart
from PySide6.QtCore import QCoreApplication, QDir, QFileInfo, Qt, Slot
from PySide6.QtGui import QGuiApplication, QImage, QPainter, QPaintEvent, QPixmap
from PySide6.QtWidgets import (
    QButtonGroup,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QLabel,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from ui.designer.tabs.tabTools.tabTools_Andreal_ui import Ui_TabTools_Andreal
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.extends.shared.settings import ANDREAL_EXECUTABLE, ANDREAL_FOLDER
from ui.extends.tabs.tabTools.tabTools_Andreal import AndrealHelper
from ui.implements.components.chartSelector import ChartSelector
from ui.implements.components.songIdSelector import SongIdSelectorMode

logger = logging.getLogger(__name__)


class PreviewLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Window, True)

    def show(self):
        super().show()
        # center the window
        width = self.width()
        height = self.height()
        screen = QGuiApplication.primaryScreen()
        screenWidth = screen.size().width()
        screenHeight = screen.size().height()
        self.setGeometry(
            max(0, screenWidth / 2 - width / 2),
            max(0, screenHeight / 2 - height / 2),
            min(width, screenWidth),
            min(height, screenHeight),
        )

    def paintEvent(self, e: QPaintEvent) -> None:
        size = self.size()
        painter = QPainter(self)
        scaledPixmap = self.pixmap().scaled(
            size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        x = (size.width() - scaledPixmap.width()) / 2
        y = (size.height() - scaledPixmap.height()) / 2
        painter.drawPixmap(x, y, scaledPixmap)


class ChartSelectorDialog(ChartSelector):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Dialog, True)
        self.setSongIdSelectorMode(SongIdSelectorMode.Chart)


class ImageTypeWhatIsThisDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.verticalLayout = QVBoxLayout(self)

        self.label = QLabel(
            # fmt: off
            QCoreApplication.translate('TabTools_Andreal', 'imageWhatIsThisDialog.description')
            # fmt: on
        )

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(Qt.Orientation.Horizontal)
        self.buttonBox.addButton(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.accepted.connect(self.close)
        self.buttonBox.rejected.connect(self.close)

        self.verticalLayout.addWidget(self.buttonBox)


class TabTools_Andreal(Ui_TabTools_Andreal, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.db = Database()

        self.andrealHelper = AndrealHelper(self)

        self.andrealFolderSelector.setMode(
            self.andrealFolderSelector.getExistingDirectory
        )

        self.andrealFolderSelector.filesSelected.connect(self.setHelperPaths)
        self.andrealExecutableSelector.filesSelected.connect(self.setHelperPaths)

        self.andrealFolderSelector.connectSettings(ANDREAL_FOLDER)
        self.andrealExecutableSelector.connectSettings(ANDREAL_EXECUTABLE)

        self.generatePreviewButton.clicked.connect(self.requestPreview)
        self.generateImageButton.clicked.connect(self.requestGenerate)

        self.infoChart: Chart | None = None

        self.previewJsonPath = None
        self.generateJsonPath = None
        self.generateImageFormat = None

        self.andrealHelper.error.connect(self.previewError)
        self.andrealHelper.ready.connect(self.previewReady)
        self.andrealHelper.finished.connect(self.previewFinished)
        self.andrealHelper.error.connect(self.generateError)
        self.andrealHelper.ready.connect(self.generateReady)
        self.andrealHelper.finished.connect(self.generateFinished)

        self.imageTypeWhatIsThisButton.clicked.connect(
            lambda: ImageTypeWhatIsThisDialog(self).show()
        )

        self.imageTypeButtonGroup = QButtonGroup(self)
        self.imageTypeButtonGroup.addButton(self.imageType_infoRadioButton, 0)
        self.imageTypeButtonGroup.addButton(self.imageType_bestRadioButton, 1)
        self.imageTypeButtonGroup.addButton(self.imageType_best30RadioButton, 2)

        self.imageFormatButtonGroup = QButtonGroup(self)
        self.imageFormatButtonGroup.addButton(self.imageFormat_jpgRadioButton, 0)
        self.imageFormatButtonGroup.addButton(self.imageFormat_pngRadioButton, 1)

        self.imageTypeButtonGroup.idToggled.connect(self.fillImageVersionComboBox)
        self.fillImageVersionComboBox()

        self.chartSelectorDialog = ChartSelectorDialog(self)
        self.chartSelectorDialog.valueChanged.connect(self.chartValueUpdated)
        self.chartSelectButton.clicked.connect(self.chartSelectorDialog.show)

    def setHelperPaths(self):
        if selectedFiles := self.andrealFolderSelector.selectedFiles():
            self.andrealHelper.andrealFolder = selectedFiles[0]
        if selectedFiles := self.andrealExecutableSelector.selectedFiles():
            self.andrealHelper.andrealExecutable = selectedFiles[0]

    def chartValueUpdated(self):
        chart = self.chartSelectorDialog.value()
        self.infoChart = chart
        if chart:
            self.chartSelectLabel.setText(
                f"{chart.title}({chart.song_id}), {chart.rating_class}"
            )

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
        try:
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
        except Exception as e:
            logger.exception("getAndrealJsonContent error")
            QMessageBox.critical(self, None, str(e))
        return (
            json.dumps(jsonContentDict, ensure_ascii=False) if jsonContentDict else None
        )

    def getAndrealJsonFileName(self):
        if not self.requestComplete():
            return None

        imageType = self.imageType()
        timestamp = int(time.time() * 1000)

        fileNameParts = ["andreal", imageType]
        if imageType == "best":
            fileNameParts.extend([self.infoChart.song_id, self.infoChart.rating_class])
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
        jsonContent = self.getAndrealJsonContent()
        if not jsonPath or not jsonContent:
            return

        self.generateImageButton.setEnabled(False)
        self.generateJsonPath = jsonPath
        self.generateImageFormat = self.imageFormat()
        with open(jsonPath, "w", encoding="utf-8") as jf:
            jf.write(jsonContent)

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

    def requestPreview(self):
        jsonPath = self.getTempAndrealJsonPath()
        jsonContent = self.getAndrealJsonContent()
        if not jsonPath or not jsonContent:
            return

        self.generatePreviewButton.setEnabled(False)
        self.previewJsonPath = jsonPath
        with open(jsonPath, "w", encoding="utf-8") as jf:
            jf.write(jsonContent)

        self.andrealHelper.request(
            jsonPath, self.getAndrealArguments(jsonPath, preview=True)
        )

    def previewFinished(self):
        self.generatePreviewButton.setEnabled(True)

    def previewError(self, jsonPath: str, errorMsg: str):
        if jsonPath != self.previewJsonPath:
            return
        QMessageBox.critical(self, "Preview Error", errorMsg)

    def previewReady(self, jsonPath: str, imageBytes: bytes):
        if jsonPath != self.previewJsonPath:
            return

        if not imageBytes:
            QMessageBox.critical(self, "Preview Error", "Empty bytes received.")
            return

        qImage = QImage.fromData(imageBytes)

        filePathParts = jsonPath.split(".")
        filePathParts.pop()
        filePath = ".".join(filePathParts)
        fileName = QFileInfo(filePath).fileName()

        previewLabel = PreviewLabel(self)
        previewLabel.setPixmap(QPixmap.fromImage(qImage))
        previewLabel.setWindowTitle(f"preview {fileName}")
        previewLabel.show()
