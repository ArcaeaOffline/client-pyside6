# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcr_B30.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from ui.implements.components.fileSelector import FileSelector
from ui.implements.components.ocrQueue import OcrQueue

class Ui_TabOcr_B30(object):
    def setupUi(self, TabOcr_B30):
        if not TabOcr_B30.objectName():
            TabOcr_B30.setObjectName(u"TabOcr_B30")
        TabOcr_B30.resize(555, 461)
        TabOcr_B30.setWindowTitle(u"TabOcr_B30")
        self.verticalLayout_3 = QVBoxLayout(TabOcr_B30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(TabOcr_B30)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b30TypeComboBox = QComboBox(self.groupBox)
        self.b30TypeComboBox.setObjectName(u"b30TypeComboBox")

        self.verticalLayout.addWidget(self.b30TypeComboBox)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(TabOcr_B30)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.knnModelSelector = FileSelector(self.groupBox_3)
        self.knnModelSelector.setObjectName(u"knnModelSelector")

        self.verticalLayout_4.addWidget(self.knnModelSelector)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(TabOcr_B30)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.b30KnnModelSelector = FileSelector(self.groupBox_5)
        self.b30KnnModelSelector.setObjectName(u"b30KnnModelSelector")

        self.verticalLayout_6.addWidget(self.b30KnnModelSelector)


        self.horizontalLayout.addWidget(self.groupBox_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_4 = QGroupBox(TabOcr_B30)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.phashDatabaseSelector = FileSelector(self.groupBox_4)
        self.phashDatabaseSelector.setObjectName(u"phashDatabaseSelector")

        self.verticalLayout_5.addWidget(self.phashDatabaseSelector)


        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(TabOcr_B30)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageSelector = FileSelector(self.groupBox_2)
        self.imageSelector.setObjectName(u"imageSelector")

        self.verticalLayout_2.addWidget(self.imageSelector)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.ocrQueue = OcrQueue(TabOcr_B30)
        self.ocrQueue.setObjectName(u"ocrQueue")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ocrQueue.sizePolicy().hasHeightForWidth())
        self.ocrQueue.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.ocrQueue)


        self.retranslateUi(TabOcr_B30)

        QMetaObject.connectSlotsByName(TabOcr_B30)
    # setupUi

    def retranslateUi(self, TabOcr_B30):
        self.groupBox.setTitle(QCoreApplication.translate("TabOcr_B30", u"b30type", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabOcr_B30", u"knnModelSelector.title", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TabOcr_B30", u"b30KnnModelSelector.title", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabOcr_B30", u"phashDatabaseSelector.title", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabOcr_B30", u"imageSelector.title", None))
        pass
    # retranslateUi

