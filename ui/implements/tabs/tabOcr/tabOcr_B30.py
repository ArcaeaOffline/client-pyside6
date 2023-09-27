import logging

import cv2
from arcaea_offline_ocr.b30.chieri.v4.ocr import ChieriBotV4Ocr
from arcaea_offline_ocr.phash_db import ImagePHashDatabase
from arcaea_offline_ocr.sift_db import SIFTDatabase
from arcaea_offline_ocr.utils import imread_unicode
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabOcr.tabOcr_B30_ui import Ui_TabOcr_B30
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.shared.cv2_utils import cv2BgrMatToQImage, qImageToCvMatBgr
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.extends.shared.settings import (
    B30_KNN_MODEL_FILE,
    KNN_MODEL_FILE,
    PHASH_DATABASE_FILE,
)
from ui.extends.tabs.tabOcr.tabOcr_B30 import ChieriV4OcrRunnable, b30ResultToScore

logger = logging.getLogger(__name__)


class TabOcr_B30(Ui_TabOcr_B30, QWidget):
    tryPrepareOcr = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.b30TypeComboBox.addItem("ChieriV4", "chieri_v4")
        self.b30TypeComboBox.setCurrentIndex(0)
        self.b30TypeComboBox.setEnabled(False)

        self.imageSelector.filesSelected.connect(self.imageSelected)
        self.knnModelSelector.filesSelected.connect(self.knnModelSelected)
        self.b30KnnModelSelector.filesSelected.connect(self.b30KnnModelSelected)
        self.phashDatabaseSelector.filesSelected.connect(self.phashDatabaseSelected)

        self.imagePath = None  # for checking only
        self.img = None
        self.paddleFolder = None
        self.paddle = None
        self.knnModel = None
        self.b30KnnModel = None
        # self.siftDatabase = None
        self.phashDatabase = None

        self.ocr = None

        self.tryPrepareOcr.connect(self.prepareOcr)

        logger.info("Applying default settings...")
        self.knnModelSelector.connectSettings(KNN_MODEL_FILE)
        self.b30KnnModelSelector.connectSettings(B30_KNN_MODEL_FILE)
        self.phashDatabaseSelector.connectSettings(PHASH_DATABASE_FILE)

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueue.setModel(self.ocrQueueModel)

    def imageSelected(self):
        if selectedFiles := self.imageSelector.selectedFiles():
            imagePath = selectedFiles[0]
            self.imagePath = imagePath
            self.img = imread_unicode(imagePath)
            self.tryPrepareOcr.emit()

    def knnModelSelected(self):
        if selectedFiles := self.knnModelSelector.selectedFiles():
            knnModelPath = selectedFiles[0]
            self.knnModel = cv2.ml.KNearest.load(knnModelPath)
            self.tryPrepareOcr.emit()

    def b30KnnModelSelected(self):
        if selectedFiles := self.b30KnnModelSelector.selectedFiles():
            b30KnnModelPath = selectedFiles[0]
            self.b30KnnModel = cv2.ml.KNearest.load(b30KnnModelPath)
            self.tryPrepareOcr.emit()

    def phashDatabaseSelected(self):
        if selectedFiles := self.phashDatabaseSelector.selectedFiles():
            phashDatabasePath = selectedFiles[0]
            self.phashDatabase = ImagePHashDatabase(phashDatabasePath)
            self.tryPrepareOcr.emit()

    def prepareOcr(self):
        b30Type = self.b30TypeComboBox.currentData()
        if not b30Type:
            return

        if b30Type == "chieri_v4":
            if (
                not self.imagePath
                or not self.knnModel
                or not self.b30KnnModel
                or not self.phashDatabase
            ):
                return

            self.ocrQueueModel.clear()

            ocr = ChieriBotV4Ocr(self.knnModel, self.b30KnnModel, self.phashDatabase)
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
            or not self.phashDatabase
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
                b30ResultToScore,
                OcrQueueModel.ProcessOcrResultFuncRole,
            )
        self.ocrQueueModel.startQueue()
