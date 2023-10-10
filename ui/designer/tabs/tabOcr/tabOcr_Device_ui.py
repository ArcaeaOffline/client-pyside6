# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcr_Device.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

from ui.implements.components.fileSelector import FileSelector
from ui.implements.components.ocrQueue import OcrQueue

class Ui_TabOcr_Device(object):
    def setupUi(self, TabOcr_Device):
        if not TabOcr_Device.objectName():
            TabOcr_Device.setObjectName(u"TabOcr_Device")
        TabOcr_Device.resize(632, 527)
        TabOcr_Device.setWindowTitle(u"TabOcr_Device")
        self.verticalLayout_3 = QVBoxLayout(TabOcr_Device)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.openWizardButton = QPushButton(TabOcr_Device)
        self.openWizardButton.setObjectName(u"openWizardButton")

        self.verticalLayout_3.addWidget(self.openWizardButton)

        self.groupBox = QGroupBox(TabOcr_Device)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.options_usePresetCheckBox = QCheckBox(self.groupBox)
        self.options_usePresetCheckBox.setObjectName(u"options_usePresetCheckBox")

        self.verticalLayout.addWidget(self.options_usePresetCheckBox)

        self.options_presetComboBox = QComboBox(self.groupBox)
        self.options_presetComboBox.setObjectName(u"options_presetComboBox")
        self.options_presetComboBox.setEnabled(False)

        self.verticalLayout.addWidget(self.options_presetComboBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.options_preciseControlWidget = QWidget(self.groupBox)
        self.options_preciseControlWidget.setObjectName(u"options_preciseControlWidget")
        self.gridLayout_2 = QGridLayout(self.options_preciseControlWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.options_preciseControlWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.options_roisStackedWidget = QStackedWidget(self.options_preciseControlWidget)
        self.options_roisStackedWidget.setObjectName(u"options_roisStackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.options_roisComboBox = QComboBox(self.page)
        self.options_roisComboBox.setObjectName(u"options_roisComboBox")

        self.verticalLayout_2.addWidget(self.options_roisComboBox)

        self.options_roisStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.options_roisCustomSelector = FileSelector(self.page_2)
        self.options_roisCustomSelector.setObjectName(u"options_roisCustomSelector")

        self.verticalLayout_4.addWidget(self.options_roisCustomSelector)

        self.options_roisStackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.options_roisStackedWidget, 0, 1, 1, 1)

        self.label_2 = QLabel(self.options_preciseControlWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.options_roisUseCustomCheckBox = QCheckBox(self.options_preciseControlWidget)
        self.options_roisUseCustomCheckBox.setObjectName(u"options_roisUseCustomCheckBox")

        self.gridLayout_2.addWidget(self.options_roisUseCustomCheckBox, 0, 2, 1, 1)

        self.options_maskerUseCustomCheckBox = QCheckBox(self.options_preciseControlWidget)
        self.options_maskerUseCustomCheckBox.setObjectName(u"options_maskerUseCustomCheckBox")

        self.gridLayout_2.addWidget(self.options_maskerUseCustomCheckBox, 1, 2, 1, 1)

        self.options_maskerStackedWidget = QStackedWidget(self.options_preciseControlWidget)
        self.options_maskerStackedWidget.setObjectName(u"options_maskerStackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.options_maskerComboBox = QComboBox(self.page_3)
        self.options_maskerComboBox.setObjectName(u"options_maskerComboBox")

        self.verticalLayout_5.addWidget(self.options_maskerComboBox)

        self.options_maskerStackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.options_maskerCustomSelector = FileSelector(self.page_4)
        self.options_maskerCustomSelector.setObjectName(u"options_maskerCustomSelector")

        self.verticalLayout_6.addWidget(self.options_maskerCustomSelector)

        self.options_maskerStackedWidget.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.options_maskerStackedWidget, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.horizontalLayout.addWidget(self.options_preciseControlWidget)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TabOcr_Device)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.dependencies_knnModelStatusLabel = QLabel(self.groupBox_2)
        self.dependencies_knnModelStatusLabel.setObjectName(u"dependencies_knnModelStatusLabel")
        self.dependencies_knnModelStatusLabel.setText(u"...")

        self.gridLayout.addWidget(self.dependencies_knnModelStatusLabel, 0, 2, 1, 1)

        self.dependencies_phashDatabaseStatusLabel = QLabel(self.groupBox_2)
        self.dependencies_phashDatabaseStatusLabel.setObjectName(u"dependencies_phashDatabaseStatusLabel")
        self.dependencies_phashDatabaseStatusLabel.setText(u"...")

        self.gridLayout.addWidget(self.dependencies_phashDatabaseStatusLabel, 1, 2, 1, 1)

        self.dependencies_phashDatabaseSelector = FileSelector(self.groupBox_2)
        self.dependencies_phashDatabaseSelector.setObjectName(u"dependencies_phashDatabaseSelector")

        self.gridLayout.addWidget(self.dependencies_phashDatabaseSelector, 1, 4, 1, 1)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)

        self.dependencies_knnModelSelector = FileSelector(self.groupBox_2)
        self.dependencies_knnModelSelector.setObjectName(u"dependencies_knnModelSelector")

        self.gridLayout.addWidget(self.dependencies_knnModelSelector, 0, 4, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 3, 2, 1)

        self.gridLayout.setColumnStretch(4, 1)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.ocrQueue = OcrQueue(TabOcr_Device)
        self.ocrQueue.setObjectName(u"ocrQueue")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ocrQueue.sizePolicy().hasHeightForWidth())
        self.ocrQueue.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.ocrQueue)


        self.retranslateUi(TabOcr_Device)
        self.options_usePresetCheckBox.toggled.connect(self.options_presetComboBox.setEnabled)

        self.options_roisStackedWidget.setCurrentIndex(0)
        self.options_maskerStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabOcr_Device)
    # setupUi

    def retranslateUi(self, TabOcr_Device):
        self.openWizardButton.setText(QCoreApplication.translate("TabOcr_Device", u"openWizardButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabOcr_Device", u"options.title", None))
        self.options_usePresetCheckBox.setText(QCoreApplication.translate("TabOcr_Device", u"options.usePreset", None))
        self.label.setText(QCoreApplication.translate("TabOcr_Device", u"options.rois", None))
        self.label_2.setText(QCoreApplication.translate("TabOcr_Device", u"options.masker", None))
        self.options_roisUseCustomCheckBox.setText(QCoreApplication.translate("TabOcr_Device", u"options.useCustom", None))
        self.options_maskerUseCustomCheckBox.setText(QCoreApplication.translate("TabOcr_Device", u"options.useCustom", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabOcr_Device", u"dependencies.title", None))
        self.label_3.setText(QCoreApplication.translate("TabOcr_Device", u"dependencies.knnModel", None))
        self.label_4.setText(QCoreApplication.translate("TabOcr_Device", u"dependencies.phashDatabase", None))
        pass
    # retranslateUi

