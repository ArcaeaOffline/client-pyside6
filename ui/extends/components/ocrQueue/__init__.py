import logging
from typing import Any, Callable

from arcaea_offline.calculate import calculate_score_range
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, ScoreInsert
from arcaea_offline_ocr.device.shared import DeviceOcrResult
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

    resultReady = Signal(DeviceOcrResult)
    finished = Signal()


class OcrRunnable(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = OcrRunnableSignals()


class OcrQueueModel(QAbstractListModel):
    ImagePathRole = Qt.ItemDataRole.UserRole + 1
    ImageQImageRole = Qt.ItemDataRole.UserRole + 2
    ImagePixmapRole = Qt.ItemDataRole.UserRole + 3

    DeviceOcrResultRole = Qt.ItemDataRole.UserRole + 10
    ScoreInsertRole = Qt.ItemDataRole.UserRole + 11
    ChartRole = Qt.ItemDataRole.UserRole + 12
    ScoreValidateOkRole = Qt.ItemDataRole.UserRole + 13

    OcrRunnableRole = Qt.ItemDataRole.UserRole + 20
    ProcessOcrResultFuncRole = (
        Qt.ItemDataRole.UserRole + 21
    )  # Callable[[imageStr, DeviceOcrResult], tuple[Chart, ScoreInsert]]

    started = Signal()
    progress = Signal(int)
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__db = Database()
        self.__items: list[dict[int, Any]] = []

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

        if role == self.DeviceOcrResultRole and isinstance(value, DeviceOcrResult):
            item[self.DeviceOcrResultRole] = value
            self.updateRole = role

        if role == self.ChartRole and isinstance(value, Chart):
            item[self.ChartRole] = value
            self.updateScoreValidateOk(index.row())
            self.updateRole = role

        if role == self.ScoreInsertRole and isinstance(value, ScoreInsert):
            item[self.ScoreInsertRole] = value
            self.updateScoreValidateOk(index.row())
            self.updateRole = role

        if role == self.ScoreValidateOkRole and isinstance(value, bool):
            item[self.ScoreValidateOkRole] = value
            self.updateRole = role

        if role == self.OcrRunnableRole and isinstance(value, OcrRunnable):
            item[self.OcrRunnableRole] = value
            self.updateRole = role

        if role == self.ProcessOcrResultFuncRole and callable(value):
            item[self.ProcessOcrResultFuncRole] = value
            self.updateRole = role

        if updateRole is not None:
            self.dataChanged.emit(index, index, [updateRole])
            return True
        else:
            return False

    def addItem(
        self,
        imagePath: str,
        runnable: OcrRunnable = None,
        process_func: Callable = None,
    ):
        if imagePath in self.imagePaths or not QFileInfo(imagePath).exists():
            logger.warning(f"Attempting to add an invalid file {imagePath}")
            return

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__items.append(
            {
                self.ImagePathRole: imagePath,
                self.ImageQImageRole: QImage(imagePath),
                self.ImagePixmapRole: QPixmap(imagePath),
                self.DeviceOcrResultRole: None,
                self.ScoreInsertRole: None,
                self.ChartRole: None,
                self.ScoreValidateOkRole: False,
                self.OcrRunnableRole: runnable,
                self.ProcessOcrResultFuncRole: process_func,
            }
        )
        self.endInsertRows()

    def updateOcrResult(self, row: int, result: DeviceOcrResult) -> bool:
        if not 0 <= row < self.rowCount() or not isinstance(result, DeviceOcrResult):
            return False

        index = self.index(row, 0)
        imagePath: str = index.data(self.ImagePathRole)
        processOcrResultFunc = index.data(self.ProcessOcrResultFuncRole)

        chart, scoreInsert = processOcrResultFunc(imagePath, result)

        # song_id = self.__db.fuzzy_search_song_id(result.title)[0][0]

        self.setData(index, result, self.DeviceOcrResultRole)
        self.setData(index, chart, self.ChartRole)
        self.setData(index, scoreInsert, self.ScoreInsertRole)
        return True

    @Slot(DeviceOcrResult)
    def ocrTaskReady(self, result: DeviceOcrResult):
        row = self.sender().rowId
        print(row)
        self.updateOcrResult(row, result)

    @Slot()
    def ocrTaskFinished(self):
        self.__taskFinishedNum += 1
        self.progress.emit(self.__taskFinishedNum)
        if self.__taskFinishedNum == self.__taskNum:
            self.finished.emit()
            print("model finished")

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
        score = index.data(self.ScoreInsertRole)
        if isinstance(chart, Chart) and isinstance(score, ScoreInsert):
            scoreRange = calculate_score_range(chart, score.pure, score.far)
            scoreValidateOk = scoreRange[0] <= score.score <= scoreRange[1]
            self.setData(index, scoreValidateOk, self.ScoreValidateOkRole)
        else:
            self.setData(index, False, self.ScoreValidateOkRole)

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
            [
                OcrQueueModel.ImagePathRole,
                OcrQueueModel.ImageQImageRole,
                OcrQueueModel.ImagePixmapRole,
            ],
            [
                OcrQueueModel.DeviceOcrResultRole,
                OcrQueueModel.ChartRole,
            ],
            [
                OcrQueueModel.DeviceOcrResultRole,
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


class OcrImageDelegate(ImageDelegate):
    def getPixmap(self, index: QModelIndex):
        return index.data(OcrQueueModel.ImagePixmapRole)

    def getImagePath(self, index: QModelIndex):
        return index.data(OcrQueueModel.ImagePathRole)


class OcrChartDelegate(ChartDelegate):
    def getChart(self, index: QModelIndex) -> Chart | None:
        return index.data(OcrQueueModel.ChartRole)

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return isinstance(
            index.data(OcrQueueModel.DeviceOcrResultRole), DeviceOcrResult
        )

    def setModelData(self, editor, model: OcrQueueTableProxyModel, index):
        if editor.validate():
            model.setData(index, editor.value(), OcrQueueModel.ChartRole)


class OcrScoreDelegate(ScoreDelegate):
    def getScoreInsert(self, index: QModelIndex):
        return index.data(OcrQueueModel.ScoreInsertRole)

    def getChart(self, index: QModelIndex):
        return index.data(OcrQueueModel.ChartRole)

    def getScoreValidateOk(self, index: QModelIndex):
        return index.data(OcrQueueModel.ScoreValidateOkRole)

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return isinstance(
            index.data(OcrQueueModel.DeviceOcrResultRole), DeviceOcrResult
        )

    def setModelData(self, editor, model: OcrQueueTableProxyModel, index):
        if super().confirmSetModelData(editor):
            model.setData(index, editor.value(), OcrQueueModel.ScoreInsertRole)
