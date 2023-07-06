import contextlib
import logging
from typing import Any

import exif
from arcaea_offline.calculate import calculate_score_range
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, ScoreInsert
from arcaea_offline_ocr.device import Device
from arcaea_offline_ocr.recognize import RecognizeResult, recognize
from PySide6.QtCore import (
    QAbstractListModel,
    QAbstractTableModel,
    QCoreApplication,
    QDateTime,
    QFileInfo,
    QModelIndex,
    QObject,
    QRect,
    QRunnable,
    QSize,
    Qt,
    QThreadPool,
    Signal,
    Slot,
)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QStyledItemDelegate, QWidget

from ui.extends.shared.delegates.chartDelegate import ChartDelegate
from ui.extends.shared.delegates.scoreDelegate import ScoreDelegate
from ui.implements.components.scoreEditor import ScoreEditor

logger = logging.getLogger(__name__)


class OcrTaskSignals(QObject):
    resultReady = Signal(int, RecognizeResult)
    finished = Signal(int)


class OcrTask(QRunnable):
    def __init__(self, index: int, device: Device, imagePath: str):
        super().__init__()
        self.index = index
        self.device = device
        self.imagePath = imagePath
        self.signals = OcrTaskSignals()

    def run(self):
        try:
            result = recognize(self.imagePath, self.device)
            self.signals.resultReady.emit(self.index, result)
            logger.info(
                f"OcrTask {self.imagePath} with {repr(self.device)} got result {repr(result)}"
            )
        except Exception as e:
            logger.exception(
                f"OcrTask {self.imagePath} with {repr(self.device)} failed"
            )
        finally:
            self.signals.finished.emit(self.index)


class OcrQueueModel(QAbstractListModel):
    ImagePathRole = Qt.ItemDataRole.UserRole + 1
    ImagePixmapRole = Qt.ItemDataRole.UserRole + 2
    RecognizeResultRole = Qt.ItemDataRole.UserRole + 10
    ScoreInsertRole = Qt.ItemDataRole.UserRole + 11
    ChartRole = Qt.ItemDataRole.UserRole + 12
    ScoreValidateOkRole = Qt.ItemDataRole.UserRole + 13

    started = Signal()
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__db = Database()
        self.__items: list[dict[int, Any]] = []

    @property
    def imagePaths(self):
        return [item.get(self.ImagePathRole) for item in self.__items]

    def clear(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), 0, self.rowCount() - 1)
        self.__items.clear()
        self.endRemoveRows()
        self.endResetModel()

    def rowCount(self, *args):
        return len(self.__items)

    def data(self, index, role):
        if (
            index.isValid()
            and 0 <= index.row() < self.rowCount()
            and index.column() == 0
        ):
            return self.__items[index.row()].get(role)
        return None

    def setData(self, *args):
        return False

    def addItem(self, imagePath: str):
        if imagePath in self.imagePaths or not QFileInfo(imagePath).exists():
            return

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__items.append(
            {
                self.ImagePathRole: imagePath,
                self.ImagePixmapRole: QPixmap(imagePath),
                self.RecognizeResultRole: None,
                self.ScoreInsertRole: None,
                self.ChartRole: None,
                self.ScoreValidateOkRole: False,
            }
        )
        self.endInsertRows()

    def updateOcrResult(self, row: int, result: RecognizeResult) -> bool:
        if not 0 <= row < self.rowCount() or not isinstance(result, RecognizeResult):
            return False

        item = self.__items[row]

        imagePath: str = item[self.ImagePathRole]
        datetime = None
        with contextlib.suppress(Exception):
            with open(imagePath, "rb") as imgf:
                exifImage = exif.Image(imgf.read())
            if exifImage.has_exif and exifImage.get("datetime_original"):
                datetimeStr = exifImage.get("datetime_original")
                datetime = QDateTime.fromString(datetimeStr, "yyyy:MM:dd hh:mm:ss")
        if not isinstance(datetime, QDateTime):
            datetime = QFileInfo(imagePath).birthTime()

        score = ScoreInsert(
            song_id=self.__db.fuzzy_search_song_id(result.title)[0][0],
            rating_class=result.rating_class,
            score=result.score,
            pure=result.pure,
            far=result.far,
            lost=result.lost,
            time=datetime.toSecsSinceEpoch(),
            max_recall=result.max_recall,
            clear_type=None,
        )
        chart = Chart.from_db_row(
            self.__db.get_chart(score.song_id, score.rating_class)
        )

        item[self.RecognizeResultRole] = result
        self.setItemChart(row, chart)
        self.setItemScore(row, score)
        modelIndex = self.index(row, 0)
        self.dataChanged.emit(
            modelIndex,
            modelIndex,
            [self.RecognizeResultRole, self.ScoreInsertRole, self.ChartRole],
        )
        return True

    @Slot(int, RecognizeResult)
    def ocrTaskReady(self, row: int, result: RecognizeResult):
        self.updateOcrResult(row, result)

    @Slot(int)
    def ocrTaskFinished(self, row: int):
        self.__taskFinishedNum += 1
        if self.__taskFinishedNum == self.__taskNum:
            self.finished.emit()

    def startQueue(self, device: Device):
        self.__taskNum = self.rowCount()
        self.__taskFinishedNum = 0
        self.started.emit()
        for row in range(self.rowCount()):
            modelIndex = self.index(row, 0)
            imagePath: str = modelIndex.data(self.ImagePathRole)
            task = OcrTask(row, device, imagePath)
            task.signals.resultReady.connect(self.ocrTaskReady)
            task.signals.finished.connect(self.ocrTaskFinished)
            QThreadPool.globalInstance().start(task)

    def updateScoreValidateOk(self, row: int):
        if not 0 <= row < self.rowCount():
            return

        item = self.__items[row]
        chart = item[self.ChartRole]
        score = item[self.ScoreInsertRole]
        if isinstance(chart, Chart) and isinstance(score, ScoreInsert):
            scoreRange = calculate_score_range(chart, score.pure, score.far)
            scoreValidateOk = scoreRange[0] <= score.score <= scoreRange[1]
            item[self.ScoreValidateOkRole] = scoreValidateOk
        else:
            item[self.ScoreValidateOkRole] = False

        modelIndex = self.index(row, 0)
        self.dataChanged.emit(modelIndex, modelIndex, [self.ScoreValidateOkRole])

    def setItemChart(self, row: int, chart: Chart):
        if not 0 <= row < self.rowCount() or not isinstance(chart, Chart):
            return False

        item = self.__items[row]
        item[self.ChartRole] = chart
        updatedRoles = [self.ChartRole]

        self.updateScoreValidateOk(row)

        modelIndex = self.index(row, 0)
        self.dataChanged.emit(modelIndex, modelIndex, updatedRoles)
        return True

    def setItemScore(self, row: int, score: ScoreInsert) -> bool:
        if not 0 <= row < self.rowCount() or not isinstance(score, ScoreInsert):
            return False

        item = self.__items[row]
        item[self.ScoreInsertRole] = score
        updatedRoles = [self.ScoreInsertRole]

        self.updateScoreValidateOk(row)

        modelIndex = self.index(row, 0)
        self.dataChanged.emit(modelIndex, modelIndex, updatedRoles)
        return True

    def acceptItem(self, row: int, ignoreValidate: bool = False):
        if not 0 <= row < self.rowCount():
            return

        item = self.__items[row]
        score = item[self.ScoreInsertRole]
        if not isinstance(score, ScoreInsert) or (
            not item[self.ScoreValidateOkRole] and not ignoreValidate
        ):
            return

        try:
            self.__db.insert_score(score)
            self.beginRemoveRows(QModelIndex(), row, row)
            self.__items.pop(row)
            self.endRemoveRows()
            return
        except Exception as e:
            logger.exception(f"Error accepting {repr(item)}")
            return

    def acceptItems(self, __rows: list[int], ignoreValidate: bool = False):
        items = sorted(__rows, reverse=True)
        [self.acceptItem(item, ignoreValidate) for item in items]

    def acceptAllItems(self, ignoreValidate: bool = False):
        self.acceptItems([*range(self.rowCount())], ignoreValidate)

    def removeItem(self, row: int):
        if not 0 <= row < self.rowCount():
            return

        self.beginRemoveRows(QModelIndex(), row, row)
        self.__items.pop(row)
        self.endRemoveRows()

    def removeItems(self, __rows: list[int]):
        rows = sorted(__rows, reverse=True)
        [self.removeItem(row) for row in rows]


class OcrQueueTableProxyModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.retranslateHeaders()
        self.__sourceModel = None
        self.__columnRoleMapping = [
            [Qt.ItemDataRole.CheckStateRole],
            [OcrQueueModel.ImagePathRole, OcrQueueModel.ImagePixmapRole],
            [
                OcrQueueModel.RecognizeResultRole,
                OcrQueueModel.ChartRole,
            ],
            [
                OcrQueueModel.RecognizeResultRole,
                OcrQueueModel.ScoreInsertRole,
                OcrQueueModel.ChartRole,
                OcrQueueModel.ScoreValidateOkRole,
            ],
        ]

    def retranslateHeaders(self):
        self.__horizontalHeaders = [
            # fmt: off
            QCoreApplication.translate("OcrTableModel", "horizontalHeader.title.select"),
            QCoreApplication.translate("OcrTableModel", "horizontalHeader.title.imagePreview"),
            QCoreApplication.translate("OcrTableModel", "horizontalHeader.title.chart"),
            QCoreApplication.translate("OcrTableModel", "horizontalHeader.title.score"),
            # fmt: on
        ]

    def sourceModel(self) -> OcrQueueModel:
        return self.__sourceModel

    def setSourceModel(self, sourceModel):
        if not isinstance(sourceModel, OcrQueueModel):
            return False

        # connect signals
        sourceModel.rowsAboutToBeInserted.connect(self.rowsAboutToBeInserted)
        sourceModel.rowsInserted.connect(self.rowsInserted)
        sourceModel.rowsAboutToBeRemoved.connect(self.rowsAboutToBeRemoved)
        sourceModel.rowsRemoved.connect(self.rowsRemoved)
        sourceModel.dataChanged.connect(self.dataChanged)
        sourceModel.layoutAboutToBeChanged.connect(self.layoutAboutToBeChanged)
        sourceModel.layoutChanged.connect(self.layoutChanged)

        self.__sourceModel = sourceModel
        return True

    def rowCount(self, *args):
        return self.sourceModel().rowCount()

    def columnCount(self, *args):
        return len(self.__horizontalHeaders)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if (
            orientation == Qt.Orientation.Horizontal
            and 0 <= section < len(self.__horizontalHeaders)
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self.__horizontalHeaders[section]
        return None

    def data(self, index, role):
        if (
            0 <= index.row() < self.rowCount()
            and 0 <= index.column() < self.columnCount()
            and role in self.__columnRoleMapping[index.column()]
        ):
            srcIndex = self.sourceModel().index(index.row(), 0)
            return srcIndex.data(role)
        return None

    def setData(self, index, value, role):
        if index.column() == 2 and role == OcrQueueModel.ChartRole:
            return self.sourceModel().setItemChart(index.row(), value)
        if index.column() == 3 and role == OcrQueueModel.ScoreInsertRole:
            return self.sourceModel().setItemScore(index.row(), value)
        return False

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        flags = (
            self.sourceModel().flags(index)
            if isinstance(self.sourceModel(), OcrQueueModel)
            else super().flags(index)
        )
        flags = flags | Qt.ItemFlag.ItemIsEnabled
        flags = flags | Qt.ItemFlag.ItemIsEditable
        flags = flags | Qt.ItemFlag.ItemIsSelectable
        if index.column() == 0:
            flags = flags & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable
        return flags


class ImageDelegate(QStyledItemDelegate):
    def getPixmap(self, index: QModelIndex):
        return index.data(OcrQueueModel.ImagePixmapRole)

    def getImagePath(self, index: QModelIndex):
        return index.data(OcrQueueModel.ImagePathRole)

    def scalePixmap(self, pixmap: QPixmap):
        return pixmap.scaled(
            100,
            100,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def paint(self, painter, option, index):
        pixmap = self.getPixmap(index)
        if not isinstance(pixmap, QPixmap):
            imagePath = self.getImagePath(index)
            option.text = imagePath
            super().paint(painter, option, index)
        else:
            pixmap = self.scalePixmap(pixmap)
            # https://stackoverflow.com/a/32047499/16484891
            # CC BY-SA 3.0
            x = option.rect.center().x() - pixmap.rect().width() / 2
            y = option.rect.center().y() - pixmap.rect().height() / 2

            painter.drawPixmap(
                QRect(x, y, pixmap.rect().width(), pixmap.rect().height()), pixmap
            )

    def sizeHint(self, option, index) -> QSize:
        pixmap = self.getPixmap(index)
        if isinstance(pixmap, QPixmap):
            pixmap = self.scalePixmap(pixmap)
            return pixmap.size()
        else:
            return QSize(100, 75)

    def createEditor(self, parent, option, index) -> QWidget:
        pixmap = self.getPixmap(index)
        if isinstance(pixmap, QPixmap):
            label = QLabel(parent)
            label.setWindowFlags(Qt.WindowType.Window)
            label.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
            label.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
            label.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
            label.setWindowTitle(QFileInfo(self.getImagePath(index)).fileName())
            pixmap = pixmap.scaled(
                800,
                800,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            label.setMinimumSize(pixmap.size())
            label.setPixmap(pixmap)
            label.move(parent.mapToGlobal(parent.pos()))
            return label

    def setModelData(self, *args):
        ...

    def updateEditorGeometry(self, *args):
        ...


class TableChartDelegate(ChartDelegate):
    def getChart(self, index: QModelIndex) -> Chart | None:
        return index.data(OcrQueueModel.ChartRole)

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return isinstance(
            index.data(OcrQueueModel.RecognizeResultRole), RecognizeResult
        )

    def setModelData(self, editor, model: OcrQueueTableProxyModel, index):
        if editor.validate():
            model.setData(index, editor.value(), OcrQueueModel.ChartRole)


class TableScoreDelegate(ScoreDelegate):
    def getScoreInsert(self, index: QModelIndex):
        return index.data(OcrQueueModel.ScoreInsertRole)

    def getChart(self, index: QModelIndex):
        return index.data(OcrQueueModel.ChartRole)

    def getScoreValidateOk(self, index: QModelIndex):
        return index.data(OcrQueueModel.ScoreValidateOkRole)

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return isinstance(
            index.data(OcrQueueModel.RecognizeResultRole), RecognizeResult
        )

    # def createEditor(self, parent, option, index):
    #     editor = super().createEditor(parent, option, index)
    #     editor.setManualHandleCommit(True)
    #     return editor

    def setModelData(self, editor, model: OcrQueueTableProxyModel, index):
        # userAcceptMessageBox = editor.triggerValidateMessageBox()
        # if userAcceptMessageBox:
        #     model.setData(index, editor.value(), OcrQueueModel.ScoreInsertRole)
        if super().confirmSetModelData(editor):
            model.setData(index, editor.value(), OcrQueueModel.ScoreInsertRole)
