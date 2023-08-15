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
    QSizePolicy, QVBoxLayout, QWidget)

from ui.implements.components import (DevicesComboBox, FileSelector, OcrQueue)

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

        self.groupBox_4 = QGroupBox(TabOcr)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tesseractFileSelector = FileSelector(self.groupBox_4)
        self.tesseractFileSelector.setObjectName(u"tesseractFileSelector")

        self.verticalLayout_5.addWidget(self.tesseractFileSelector)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(TabOcr)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ocrQueue = OcrQueue(self.groupBox_2)
        self.ocrQueue.setObjectName(u"ocrQueue")

        self.horizontalLayout.addWidget(self.ocrQueue)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(TabOcr)

        QMetaObject.connectSlotsByName(TabOcr)
    # setupUi

    def retranslateUi(self, TabOcr):
        self.openWizardButton.setText(QCoreApplication.translate("TabOcr", u"openWizardButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabOcr", u"deviceSelector.title", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabOcr", u"tesseractSelector.title", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabOcr", u"ocr.title", None))
        pass
    # retranslateUi

