import logging
from pathlib import Path

import cv2
from arcaea_offline_ocr.b30.chieri.v4.ocr import ChieriBotV4Ocr
from arcaea_offline_ocr.sift_db import SIFTDatabase
from arcaea_offline_ocr.utils import imread_unicode

# from paddleocr import PaddleOCR
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabOcr.tabOcr_B30_ui import Ui_TabOcr_B30
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.shared.cv2_utils import cv2BgrMatToQImage, qImageToCvMatBgr
from ui.extends.tabs.tabOcr.tabOcr_B30 import (
    ChieriV4OcrRunnable,
    b30ResultToScoreInsert,
)

logger = logging.getLogger(__name__)


class TabOcr_B30(Ui_TabOcr_B30, QWidget):
    tryPrepareOcr = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.b30TypeComboBox.addItem("ChieriV4", "chieri_v4")
        self.b30TypeComboBox.setCurrentIndex(0)
        self.b30TypeComboBox.setEnabled(False)

        # self.paddleFolderSelector.setMode(
        #     self.paddleFolderSelector.getExistingDirectory
        # )

        self.imageSelector.filesSelected.connect(self.imageSelected)
        self.knnModelSelector.filesSelected.connect(self.knnModelSelected)
        self.b30KnnModelSelector.filesSelected.connect(self.b30KnnModelSelected)
        # self.paddleFolderSelector.filesSelected.connect(self.paddleFolderSelected)
        self.siftDatabaseSelector.filesSelected.connect(self.siftDatabaseSelected)

        self.imagePath = None  # for checking only
        self.img = None
        self.paddleFolder = None
        self.paddle = None
        self.knnModel = None
        self.b30KnnModel = None
        self.siftDatabase = None

        self.ocr = None

        self.tryPrepareOcr.connect(self.prepareOcr)

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueue.setModel(self.ocrQueueModel)

    def imageSelected(self):
        selectedFiles = self.imageSelector.selectedFiles()
        if selectedFiles:
            imagePath = selectedFiles[0]
            self.imagePath = imagePath
            self.img = imread_unicode(imagePath)
            self.tryPrepareOcr.emit()

    def knnModelSelected(self):
        selectedFiles = self.knnModelSelector.selectedFiles()
        if selectedFiles:
            knnModelPath = selectedFiles[0]
            self.knnModel = cv2.ml.KNearest.load(knnModelPath)
            self.tryPrepareOcr.emit()

    def b30KnnModelSelected(self):
        selectedFiles = self.b30KnnModelSelector.selectedFiles()
        if selectedFiles:
            b30KnnModelPath = selectedFiles[0]
            self.b30KnnModel = cv2.ml.KNearest.load(b30KnnModelPath)
            self.tryPrepareOcr.emit()

    def siftDatabaseSelected(self):
        selectedFiles = self.siftDatabaseSelector.selectedFiles()
        if selectedFiles:
            siftDatabasePath = selectedFiles[0]
            self.siftDatabase = SIFTDatabase(siftDatabasePath)
            self.tryPrepareOcr.emit()

    def paddleFolderSelected(self):
        selectedFiles = self.paddleFolderSelector.selectedFiles()
        if selectedFiles:
            self.paddleFolder = selectedFiles[0]
            self.initPaddle()
            self.tryPrepareOcr.emit()

    def initPaddle(self):
        paddleFolder = Path(self.paddleFolder)
        paddleDetFolder = paddleFolder / "det"
        paddleClsFolder = paddleFolder / "cls"
        paddleRecFolder = paddleFolder / "rec"

        if not (paddleDetFolder.exists() and paddleRecFolder.exists()):
            logger.warning("paddleocr folder incomplete, aborting.")
            return

        self.paddle = PaddleOCR(
            show_log=False,
            use_angle_cls=False,
            det_model_dir=str(paddleDetFolder),
            cls_model_dir=str(paddleClsFolder),
            rec_model_dir=str(paddleRecFolder),
        )

    def prepareOcr(self):
        b30Type = self.b30TypeComboBox.currentData()
        if not b30Type:
            return

        if b30Type == "chieri_v4":
            if (
                not self.imagePath
                or not self.knnModel
                or not self.b30KnnModel
                or not self.siftDatabase
            ):
                return

            self.ocrQueueModel.clear()

            ocr = ChieriBotV4Ocr(self.knnModel, self.b30KnnModel, self.siftDatabase)
            ocr.set_factor(self.img)
            self.ocr = ocr

            roi = ocr.rois
            for component in roi.components(self.img):
                qImage = cv2BgrMatToQImage(component.copy())
                self.ocrQueueModel.addItem(qImage)
        self.ocrQueue.resizeTableView()

    @Slot()
    def on_ocr_startButton_clicked(self):
        if (
            not self.imagePath
            or not self.knnModel
            or not self.b30KnnModel
            or not self.siftDatabase
        ):
            return

        for row in range(self.ocrQueueModel.rowCount()):
            index = self.ocrQueueModel.index(row, 0)
            qImage = index.data(OcrQueueModel.ImageQImageRole)
            cv2Mat = qImageToCvMatBgr(qImage)
            runnable = ChieriV4OcrRunnable(self.ocr, cv2Mat)
            self.ocrQueueModel.setData(index, runnable, OcrQueueModel.OcrRunnableRole)
            self.ocrQueueModel.setData(
                index,
                b30ResultToScoreInsert,
                OcrQueueModel.ProcessOcrResultFuncRole,
            )
        self.ocrQueueModel.startQueue()
