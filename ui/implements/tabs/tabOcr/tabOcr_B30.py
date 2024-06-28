import logging

import cv2
import numpy as np
from arcaea_offline_ocr.b30.chieri.v4.ocr import ChieriBotV4Ocr
from arcaea_offline_ocr.phash_db import ImagePhashDatabase
from arcaea_offline_ocr.utils import imread_unicode
from PIL import Image
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget

from core.settings import SettingsKeys
from ui.designer.tabs.tabOcr.tabOcr_B30_ui import Ui_TabOcr_B30
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.ocr.dependencies import (
    getCv2StatModelStatusText,
    getPhashDatabaseStatusText,
)
from ui.extends.shared.language import LanguageChangeEventFilter
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

        self.dependencies_knnModelSelector.filesSelected.connect(self.knnModelSelected)
        self.dependencies_b30KnnModelSelector.filesSelected.connect(
            self.b30KnnModelSelected
        )
        self.dependencies_phashDatabaseSelector.filesSelected.connect(
            self.phashDatabaseSelected
        )

        self.knnModel = None
        self.b30KnnModel = None
        self.phashDatabase = None

        self.ocr = None

        logger.info("Applying settings...")
        self.dependencies_knnModelSelector.connectSettings(
            SettingsKeys.Ocr.KnnModelFile
        )
        self.dependencies_b30KnnModelSelector.connectSettings(
            SettingsKeys.Ocr.B30KnnModelFile
        )
        self.dependencies_phashDatabaseSelector.connectSettings(
            SettingsKeys.Ocr.PhashDatabaseFile
        )

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueue.setModel(self.ocrQueueModel)

    # def imageSelected(self):
    #     if selectedFiles := self.imageSelector.selectedFiles():
    #         imagePath = selectedFiles[0]
    #         self.imagePath = imagePath
    #         self.img = imread_unicode(imagePath)
    #         self.tryPrepareOcr.emit()

    def knnModelSelected(self):
        try:
            filePath = self.dependencies_knnModelSelector.selectedFiles()[0]
            self.knnModel = cv2.ml.KNearest.load(filePath)
        except Exception:
            self.knnModel = None
            logger.exception("Error loading knn model:")
        finally:
            self.dependencies_knnModelStatusLabel.setText(
                getCv2StatModelStatusText(self.knnModel)
            )

    def b30KnnModelSelected(self):
        try:
            filePath = self.dependencies_b30KnnModelSelector.selectedFiles()[0]
            self.b30KnnModel = cv2.ml.KNearest.load(filePath)
        except Exception:
            self.b30KnnModel = None
            logger.exception("Error loading b30 knn model:")
        finally:
            self.dependencies_b30KnnModelStatusLabel.setText(
                getCv2StatModelStatusText(self.b30KnnModel)
            )

    def phashDatabaseSelected(self):
        try:
            filePath = self.dependencies_phashDatabaseSelector.selectedFiles()[0]
            self.phashDatabase = ImagePhashDatabase(filePath)
        except Exception:
            self.phashDatabase = None
            logger.exception("Error loading phash database:")
        finally:
            self.dependencies_phashDatabaseStatusLabel.setText(
                getPhashDatabaseStatusText(self.phashDatabase)
            )

    def checkDependencies(self):
        b30Type = self.b30TypeComboBox.currentData()
        if not b30Type:
            return False
        elif b30Type == "chieri_v4":
            return (
                self.knnModel is not None
                and self.b30KnnModel is not None
                and self.phashDatabase is not None
            )
        else:
            return False

    @Slot()
    def on_ocr_addImageButton_clicked(self):
        if not self.checkDependencies():
            QMessageBox.critical(self, None, "Dependencies not configured.")
            return

        imagePath, _ = QFileDialog.getOpenFileName(
            self, None, "", "Image Files (*.png *.jpg *.jpeg *.bmp *.webp);;*"
        )

        if not imagePath:
            return

        self.ocrQueueModel.clear()

        img = imread_unicode(imagePath, cv2.IMREAD_COLOR)
        ocr = ChieriBotV4Ocr(self.knnModel, self.b30KnnModel, self.phashDatabase)
        ocr.set_factor(img)
        self.ocr = ocr

        roi = ocr.rois
        for component in roi.components(img):
            qImage = Image.fromarray(component.copy()).toqimage()
            self.ocrQueueModel.addItem(qImage)
        self.ocrQueue.resizeTableView()

    @Slot()
    def on_ocr_startButton_clicked(self):
        if not self.ocr:
            return

        for row in range(self.ocrQueueModel.rowCount()):
            index = self.ocrQueueModel.index(row, 0)
            qImage = index.data(OcrQueueModel.ImageQImageRole)
            cv2Mat = np.array(Image.fromqimage(qImage))
            runnable = ChieriV4OcrRunnable(self.ocr, cv2Mat)
            self.ocrQueueModel.setData(index, runnable, OcrQueueModel.OcrRunnableRole)
            self.ocrQueueModel.setData(
                index,
                b30ResultToScore,
                OcrQueueModel.ProcessOcrResultFuncRole,
            )
        self.ocrQueueModel.startQueue()
