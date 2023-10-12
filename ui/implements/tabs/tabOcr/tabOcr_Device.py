import logging

import cv2
from arcaea_offline_ocr.device.rois import (
    DeviceRoisAutoT1,
    DeviceRoisAutoT2,
    DeviceRoisMaskerAutoT1,
    DeviceRoisMaskerAutoT2,
)
from arcaea_offline_ocr.phash_db import ImagePhashDatabase
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget

from ui.designer.tabs.tabOcr.tabOcr_Device_ui import Ui_TabOcr_Device
from ui.extends.components.ocrQueue import OcrQueueModel
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.extends.shared.settings import KNN_MODEL_FILE, PHASH_DATABASE_FILE
from ui.extends.tabs.tabOcr.tabOcr_Device import ScoreConverter, TabDeviceOcrRunnable

logger = logging.getLogger(__name__)


class TabOcr_Device(Ui_TabOcr_Device, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openWizardButton.setEnabled(False)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        # connect options checkBoxes & comboBoxes
        self.options_roisUseCustomCheckBox.toggled.connect(
            lambda useCustom: self.options_roisStackedWidget.setCurrentIndex(
                1 if useCustom else 0
            )
        )
        self.options_maskerUseCustomCheckBox.toggled.connect(
            lambda useCustom: self.options_maskerStackedWidget.setCurrentIndex(
                1 if useCustom else 0
            )
        )
        self.options_usePresetCheckBox.toggled.connect(self.options_setUsePreset)

        self.options_presetComboBox.currentIndexChanged.connect(
            self.options_presetSelected
        )
        # fill option values
        self.options_fillComboBoxes()

        self.dependencies_knnModelSelector.filesSelected.connect(self.knnModelSelected)
        self.dependencies_phashDatabaseSelector.filesSelected.connect(
            self.phashDatabaseSelected
        )

        logger.info("Applying settings...")
        self.dependencies_knnModelSelector.connectSettings(KNN_MODEL_FILE)
        self.dependencies_phashDatabaseSelector.connectSettings(PHASH_DATABASE_FILE)

        self.options_usePresetCheckBox.setChecked(True)
        self.options_usePresetCheckBox.setEnabled(False)

        self.ocrQueueModel = OcrQueueModel(self)
        self.ocrQueue.setModel(self.ocrQueueModel)
        self.ocrQueueProxyModel = self.ocrQueue.tableProxyModel()

    @Slot()
    def on_openWizardButton_clicked(self):
        # wizard = Wizard(self)
        # wizard.open()
        pass

    @Slot(bool)
    def options_setUsePreset(self, usePreset: bool):
        self.options_roisUseCustomCheckBox.setChecked(not usePreset)
        self.options_maskerUseCustomCheckBox.setChecked(not usePreset)
        self.options_preciseControlWidget.setEnabled(not usePreset)
        if not usePreset:
            self.options_presetComboBox.setCurrentIndex(-1)

    @Slot(int)
    def options_presetSelected(self, index: int):
        if index < 0:
            self.options_roisComboBox.setCurrentIndex(-1)
            self.options_maskerComboBox.setCurrentIndex(-1)

        autoTypeString = self.options_presetComboBox.currentData()
        roisAutoTypeIndex = self.options_roisComboBox.findData(autoTypeString)
        maskerAutoTypeIndex = self.options_maskerComboBox.findData(autoTypeString)
        self.options_roisComboBox.setCurrentIndex(roisAutoTypeIndex)
        self.options_maskerComboBox.setCurrentIndex(maskerAutoTypeIndex)

    def options_fillComboBoxes(self):
        self.options_roisComboBox.addItem("RoisAutoT1", "AutoT1")
        self.options_roisComboBox.addItem("RoisAutoT2", "AutoT2")
        self.options_roisComboBox.setCurrentIndex(-1)

        self.options_maskerComboBox.addItem("MaskerAutoT1", "AutoT1")
        self.options_maskerComboBox.addItem("MaskerAutoT2", "AutoT2")
        self.options_maskerComboBox.setCurrentIndex(-1)

        self.options_presetComboBox.addItem("AutoT1 (ver <= 4.7.2)", "AutoT1")
        self.options_presetComboBox.addItem("AutoT2 (ver >= 5.0.0)", "AutoT2")
        self.options_presetComboBox.setCurrentIndex(1)

    def knnModelSelected(self):
        try:
            knnModelFile = self.dependencies_knnModelSelector.selectedFiles()[0]
            self.knnModel = cv2.ml.KNearest.load(knnModelFile)
            varCount = self.knnModel.getVarCount()
            if varCount != 81:
                self.dependencies_knnModelStatusLabel.setText(
                    f'<font color="darkorange">WARN</font>, varCount {varCount}'
                )
            else:
                self.dependencies_knnModelStatusLabel.setText(
                    f'<font color="green">OK</font>, varCount {varCount}'
                )
        except Exception:
            logger.exception("Error loading knn model:")
            self.dependencies_knnModelStatusLabel.setText(
                '<font color="red">Error</font>'
            )

    def phashDatabaseSelected(self):
        try:
            phashDbFile = self.dependencies_phashDatabaseSelector.selectedFiles()[0]
            self.phashDatabase = ImagePhashDatabase(phashDbFile)
            self.dependencies_phashDatabaseStatusLabel.setText(
                f'<font color="green">OK</font>, '
                f"J{len(self.phashDatabase.jacket_hashes)} "
                f"PI{len(self.phashDatabase.partner_icon_hashes)}"
            )
        except Exception:
            logger.exception("Error loading phash database:")
            self.dependencies_phashDatabaseStatusLabel.setText(
                '<font color="red">Error</font>'
            )

    @Slot()
    def on_ocr_addImageButton_clicked(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, None, "", "Image Files (*.png *.jpg *.jpeg *.bmp *.webp);;*"
        )
        filesNum = len(files)
        if filesNum >= 1000:
            updateFreq = 20
        elif filesNum >= 100:
            updateFreq = 10
        elif filesNum >= 30:
            updateFreq = 5
        else:
            updateFreq = 1
        for i, file in enumerate(files):
            self.ocrQueueModel.addItem(file)
            if i % updateFreq == 0:
                QApplication.processEvents()
        self.ocrQueue.resizeTableView()

    def deviceRois(self):
        if self.options_roisUseCustomCheckBox.isChecked():
            ...
        else:
            selectedPreset = self.options_roisComboBox.currentData()
            if selectedPreset == "AutoT1":
                return DeviceRoisAutoT1
            elif selectedPreset == "AutoT2":
                return DeviceRoisAutoT2
            else:
                QMessageBox.critical(self, None, "Select a Rois preset first.")
                return None

    def deviceRoisMasker(self):
        if self.options_maskerUseCustomCheckBox.isChecked():
            ...
        else:
            selectedPreset = self.options_maskerComboBox.currentData()
            if selectedPreset == "AutoT1":
                return DeviceRoisMaskerAutoT1()
            elif selectedPreset == "AutoT2":
                return DeviceRoisMaskerAutoT2()
            else:
                QMessageBox.critical(self, None, "Select a Masker preset first.")
                return None

    @Slot()
    def on_ocr_startButton_clicked(self):
        for row in range(self.ocrQueueModel.rowCount()):
            index = self.ocrQueueModel.index(row, 0)
            imagePath = index.data(OcrQueueModel.ImagePathRole)

            rois = self.deviceRois()
            masker = self.deviceRoisMasker()

            if rois is None or masker is None:
                return

            runnable = TabDeviceOcrRunnable(
                imagePath, rois, masker, self.knnModel, self.phashDatabase
            )
            self.ocrQueueModel.setData(index, runnable, OcrQueueModel.OcrRunnableRole)
            self.ocrQueueModel.setData(
                index,
                ScoreConverter.device,
                OcrQueueModel.ProcessOcrResultFuncRole,
            )
        self.ocrQueueModel.startQueue()

    @Slot()
    def on_ocr_removeAllButton_clicked(self):
        self.ocrQueueModel.clear()
