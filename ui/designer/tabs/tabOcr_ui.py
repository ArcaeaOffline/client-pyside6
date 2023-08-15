# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcr.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

from ui.implements.components.devicesComboBox import DevicesComboBox
from ui.implements.components.fileSelector import FileSelector
from ui.implements.components.ocrQueue import OcrQueue

class Ui_TabOcr(object):
    def setupUi(self, TabOcr):
        if not TabOcr.objectName():
            TabOcr.setObjectName(u"TabOcr")
        TabOcr.resize(632, 527)
        TabOcr.setWindowTitle(u"TabOcr")
        self.verticalLayout_3 = QVBoxLayout(TabOcr)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.openWizardButton = QPushButton(TabOcr)
        self.openWizardButton.setObjectName(u"openWizardButton")

        self.verticalLayout_3.addWidget(self.openWizardButton)

        self.groupBox = QGroupBox(TabOcr)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deviceFileSelector = FileSelector(self.groupBox)
        self.deviceFileSelector.setObjectName(u"deviceFileSelector")

        self.verticalLayout.addWidget(self.deviceFileSelector)

        self.deviceComboBox = DevicesComboBox(self.groupBox)
        self.deviceComboBox.setObjectName(u"deviceComboBox")

        self.verticalLayout.addWidget(self.deviceComboBox)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalWidget = QWidget(TabOcr)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.horizontalWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knnModelSelector = FileSelector(self.groupBox_6)
        self.knnModelSelector.setObjectName(u"knnModelSelector")

        self.verticalLayout_6.addWidget(self.knnModelSelector)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.deviceDependenciesStackedWidget = QStackedWidget(self.horizontalWidget)
        self.deviceDependenciesStackedWidget.setObjectName(u"deviceDependenciesStackedWidget")
        self.deviceV1 = QWidget()
        self.deviceV1.setObjectName(u"deviceV1")
        self.verticalLayout_2 = QVBoxLayout(self.deviceV1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.deviceV1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tesseractFileSelector = FileSelector(self.groupBox_4)
        self.tesseractFileSelector.setObjectName(u"tesseractFileSelector")

        self.verticalLayout_5.addWidget(self.tesseractFileSelector)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.deviceDependenciesStackedWidget.addWidget(self.deviceV1)
        self.deviceV2 = QWidget()
        self.deviceV2.setObjectName(u"deviceV2")
        self.verticalLayout_4 = QVBoxLayout(self.deviceV2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.deviceV2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.siftDatabaseSelector = FileSelector(self.groupBox_5)
        self.siftDatabaseSelector.setObjectName(u"siftDatabaseSelector")

        self.verticalLayout_7.addWidget(self.siftDatabaseSelector)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.deviceDependenciesStackedWidget.addWidget(self.deviceV2)

        self.horizontalLayout_2.addWidget(self.deviceDependenciesStackedWidget)


        self.verticalLayout_3.addWidget(self.horizontalWidget)

        self.groupBox_2 = QGroupBox(TabOcr)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ocrQueue = OcrQueue(self.groupBox_2)
        self.ocrQueue.setObjectName(u"ocrQueue")

        self.horizontalLayout.addWidget(self.ocrQueue)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(TabOcr)

        self.deviceDependenciesStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabOcr)
    # setupUi

    def retranslateUi(self, TabOcr):
        self.openWizardButton.setText(QCoreApplication.translate("TabOcr", u"openWizardButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabOcr", u"deviceSelector.title", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TabOcr", u"knnModelSelector.title", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabOcr", u"tesseractSelector.title", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TabOcr", u"siftDatabaseSelector.title", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabOcr", u"ocr.title", None))
        pass
    # retranslateUi

