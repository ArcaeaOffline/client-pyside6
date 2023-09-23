import logging
from enum import IntEnum
from typing import Any, Callable, Optional, overload

from arcaea_offline.calculate import calculate_score_range
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Score
from arcaea_offline_ocr.b30.shared import B30OcrResultItem
from arcaea_offline_ocr.device.shared import DeviceOcrResult
from arcaea_offline_ocr.utils import convert_to_srgb
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import (
    QAbstractListModel,
    QAbstractTableModel,
    QCoreApplication,
    QFileInfo,
    QModelIndex,
    QObject,
    QRunnable,
    Qt,
    QThreadPool,
    Signal,
    Slot,
)
from PySide6.QtGui import QImage, QPixmap

from ui.extends.shared.delegates.chartDelegate import ChartDelegate
from ui.extends.shared.delegates.imageDelegate import ImageDelegate
from ui.extends.shared.delegates.scoreDelegate import ScoreDelegate

logger = logging.getLogger(__name__)


class OcrRunnableSignals(QObject):
    rowId: int = -1

    resultReady = Signal("QVariant")
    finished = Signal()


class OcrRunnable(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = OcrRunnableSignals()


class IccOption(IntEnum):
    Ignore = 0
    UsePIL = 1
    TryFix = 2


class OcrQueueModel(QAbstractListModel):
    ImagePathRole = Qt.ItemDataRole.UserRole + 1
    ImageQImageRole = Qt.ItemDataRole.UserRole + 2
    ImagePixmapRole = Qt.ItemDataRole.UserRole + 3

    OcrResultRole = Qt.ItemDataRole.UserRole + 10
    ScoreRole = Qt.ItemDataRole.UserRole + 11
    ChartRole = Qt.ItemDataRole.UserRole + 12
    ScoreValidateOkRole = Qt.ItemDataRole.UserRole + 13

    OcrRunnableRole = Qt.ItemDataRole.UserRole + 20
    ProcessOcrResultFuncRole = (
        Qt.ItemDataRole.UserRole + 21
    )  # Callable[[imageStr, DeviceOcrResult], tuple[Chart, Score]]

    started = Signal()
    progress = Signal(int)
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__db = Database()
        self.__items: list[dict[int, Any]] = []
        self.__iccOption = IccOption.UsePIL

        self.__taskFinishedNum = 0

    @property
    def imagePaths(self):
        return [item.get(self.ImagePathRole) for item in self.__items]

    def clear(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), 0, self.rowCount() - 1)
        self.__items.clear()
        self.endRemoveRows()
        self.__taskFinishedNum = 0
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

    def setData(self, index: QModelIndex, value: Any, role: int):
        if not 0 <= index.row() < self.rowCount():
            return False

        item = self.__items[index.row()]
        updateRole = None

        if role == self.OcrResultRole:
            item[self.OcrResultRole] = value
            updateRole = role

        if role == self.ChartRole and isinstance(value, Chart):
            item[self.ChartRole] = value
            self.updateScoreValidateOk(index.row())
            updateRole = role

        if role == self.ScoreRole and isinstance(value, Score):
            item[self.ScoreRole] = value
            self.updateScoreValidateOk(index.row())
            updateRole = role

        if role == self.ScoreValidateOkRole and isinstance(value, bool):
            item[self.ScoreValidateOkRole] = value
            updateRole = role

        if role == self.OcrRunnableRole and isinstance(value, OcrRunnable):
            item[self.OcrRunnableRole] = value
            updateRole = role

        if role == self.ProcessOcrResultFuncRole and callable(value):
            item[self.ProcessOcrResultFuncRole] = value
            updateRole = role

        if updateRole is not None:
            self.dataChanged.emit(index, index, [updateRole])
            return True
        else:
            logger.warning(
                f"{repr(self)} setData at row {index.row()} with role {role} and value {value} rejected."
            )
            return False

    @property
    def iccOption(self):
        return self.__iccOption

    @iccOption.setter
    def iccOption(self, opt: IccOption):
        self.__iccOption = opt

    @overload
    def addItem(
        self,
        image: str,
        runnable: OcrRunnable = None,
        process_func: Callable[[Optional[str], QImage, Any], Score] = None,
    ):
        ...

    @overload
    def addItem(
        self,
        image: QImage,
        runnable: OcrRunnable = None,
        process_func: Callable[[Optional[str], QImage, Any], Score] = None,
    ):
        ...

    def addItem(
        self,
        image,
        runnable=None,
        process_func=None,
    ):
        if isinstance(image, str):
            if image in self.imagePaths or not QFileInfo(image).exists():
                logger.warning(f"Attempting to add an invalid file {image}")
                return
            imagePath = image
            if self.iccOption == IccOption.TryFix:
                img = Image.open(image)
                img = convert_to_srgb(img)
                qImage = ImageQt(img)
            elif self.iccOption == IccOption.UsePIL:
                img = Image.open(image)
                qImage = ImageQt(img)
            else:
                qImage = QImage(image)

            qPixmap = QPixmap(qImage)
        elif isinstance(image, QImage):
            imagePath = None
            qImage = image.copy()
            qPixmap = QPixmap(qImage)
        else:
            raise ValueError("Unsupported type for `image`")

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__items.append(
            {
                self.ImagePathRole: imagePath,
                self.ImageQImageRole: qImage,
                self.ImagePixmapRole: qPixmap,
                self.OcrResultRole: None,
                self.ScoreRole: None,
                self.ChartRole: None,
                self.ScoreValidateOkRole: False,
                self.OcrRunnableRole: runnable,
                self.ProcessOcrResultFuncRole: process_func,
            }
        )
        self.endInsertRows()

    def updateOcrResult(self, row: int, result: Any) -> bool:
        if not 0 <= row < self.rowCount():
            return False

        index = self.index(row, 0)
        imagePath: str = index.data(self.ImagePathRole)
        qImage: QImage = index.data(self.ImageQImageRole)
        logger.info(f"update request: {result}@row{row}")
        processOcrResultFunc = index.data(self.ProcessOcrResultFuncRole)

        chart, scoreInsert = processOcrResultFunc(imagePath, qImage, result)

        self.setData(index, result, self.OcrResultRole)
        self.setData(index, chart, self.ChartRole)
        self.setData(index, scoreInsert, self.ScoreRole)
        return True

    @Slot(DeviceOcrResult)
    def ocrTaskReady(self, result: DeviceOcrResult):
        row = self.sender().rowId
        self.updateOcrResult(row, result)

    @Slot()
    def ocrTaskFinished(self):
        self.__taskFinishedNum += 1
        self.progress.emit(self.__taskFinishedNum)
        if self.__taskFinishedNum == self.__taskNum:
            self.finished.emit()

    def startQueue(self):
        self.__taskNum = self.rowCount()
        self.__taskFinishedNum = 0
        self.started.emit()
        for row in range(self.rowCount()):
            modelIndex = self.index(row, 0)
            runnable: OcrRunnable = modelIndex.data(self.OcrRunnableRole)
            runnable.signals.rowId = row
            runnable.signals.resultReady.connect(self.ocrTaskReady)
            runnable.signals.finished.connect(self.ocrTaskFinished)
            QThreadPool.globalInstance().start(runnable)

    def updateScoreValidateOk(self, row: int):
        if not 0 <= row < self.rowCount():
            return

        index = self.index(row, 0)
        chart = index.data(self.ChartRole)
        score = index.data(self.ScoreRole)
        if (
            isinstance(chart, Chart)
            and isinstance(score, Score)
            and chart.notes
            and score.pure
            and score.far
        ):
            scoreRange = calculate_score_range(chart.notes, score.pure, score.far)
            scoreValidateOk = scoreRange[0] <= score.score <= scoreRange[1]
            self.setData(index, scoreValidateOk, self.ScoreValidateOkRole)
        else:
            self.setData(index, False, self.ScoreValidateOkRole)

    def acceptItem(self, row: int, ignoreValidate: bool = False):
        if not 0 <= row < self.rowCount():
            return

        item = self.__items[row]
        score = item[self.ScoreRole]
        if not isinstance(score, Score) or (
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
            [
                OcrQueueModel.ImagePathRole,
                OcrQueueModel.ImageQImageRole,
                OcrQueueModel.ImagePixmapRole,
            ],
            [
                OcrQueueModel.OcrResultRole,
                OcrQueueModel.ChartRole,
            ],
            [
                OcrQueueModel.OcrResultRole,
                OcrQueueModel.ScoreRole,
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
            return self.sourceModel().setData(index, value, role)
        if index.column() == 3 and role == OcrQueueModel.ScoreRole:
            return self.sourceModel().setData(index, value, role)
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


class OcrImageDelegate(ImageDelegate):
    def getPixmap(self, index: QModelIndex):
        return index.data(OcrQueueModel.ImagePixmapRole)

    def getImagePath(self, index: QModelIndex):
        return index.data(OcrQueueModel.ImagePathRole)


class OcrChartDelegate(ChartDelegate):
    def getChart(self, index: QModelIndex) -> Chart | None:
        return index.data(OcrQueueModel.ChartRole)

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return isinstance(index.data(OcrQueueModel.OcrResultRole), DeviceOcrResult)

    def setModelData(self, editor, model: OcrQueueTableProxyModel, index):
        if editor.validate():
            model.setData(index, editor.value(), OcrQueueModel.ChartRole)


class OcrScoreDelegate(ScoreDelegate):
    def getScore(self, index: QModelIndex):
        return index.data(OcrQueueModel.ScoreRole)

    def getChart(self, index: QModelIndex):
        return index.data(OcrQueueModel.ChartRole)

    def getScoreValidateOk(self, index: QModelIndex):
        return index.data(OcrQueueModel.ScoreValidateOkRole)

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return True
        # return isinstance(self.getChart(index), Chart) and isinstance(
        #     self.getScore(index), Score
        # )
        # return isinstance(
        #     index.data(OcrQueueModel.OcrResultRole), (DeviceOcrResult, B30OcrResultItem)
        # )

    def setModelData(self, editor, model: OcrQueueTableProxyModel, index):
        if super().confirmSetModelData(editor):
            model.setData(index, editor.value(), OcrQueueModel.ScoreRole)
