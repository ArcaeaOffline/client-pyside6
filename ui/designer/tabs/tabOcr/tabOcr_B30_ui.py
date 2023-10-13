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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

from ui.implements.components.fileSelector import FileSelector
from ui.implements.components.ocrQueue import OcrQueue

class Ui_TabOcr_B30(object):
    def setupUi(self, TabOcr_B30):
        if not TabOcr_B30.objectName():
            TabOcr_B30.setObjectName(u"TabOcr_B30")
        TabOcr_B30.resize(555, 461)
        TabOcr_B30.setWindowTitle(u"TabOcr_B30")
        self.verticalLayout_2 = QVBoxLayout(TabOcr_B30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(TabOcr_B30)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b30TypeComboBox = QComboBox(self.groupBox)
        self.b30TypeComboBox.setObjectName(u"b30TypeComboBox")

        self.verticalLayout.addWidget(self.b30TypeComboBox)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_6 = QGroupBox(TabOcr_B30)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dependencies_knnModelStatusLabel = QLabel(self.groupBox_6)
        self.dependencies_knnModelStatusLabel.setObjectName(u"dependencies_knnModelStatusLabel")
        self.dependencies_knnModelStatusLabel.setText(u"...")

        self.gridLayout.addWidget(self.dependencies_knnModelStatusLabel, 0, 2, 1, 1)

        self.line_2 = QFrame(self.groupBox_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 3, 3, 1)

        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dependencies_phashDatabaseStatusLabel = QLabel(self.groupBox_6)
        self.dependencies_phashDatabaseStatusLabel.setObjectName(u"dependencies_phashDatabaseStatusLabel")
        self.dependencies_phashDatabaseStatusLabel.setText(u"...")

        self.gridLayout.addWidget(self.dependencies_phashDatabaseStatusLabel, 2, 2, 1, 1)

        self.line = QFrame(self.groupBox_6)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)

        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dependencies_b30KnnModelStatusLabel = QLabel(self.groupBox_6)
        self.dependencies_b30KnnModelStatusLabel.setObjectName(u"dependencies_b30KnnModelStatusLabel")
        self.dependencies_b30KnnModelStatusLabel.setText(u"...")

        self.gridLayout.addWidget(self.dependencies_b30KnnModelStatusLabel, 1, 2, 1, 1)

        self.dependencies_knnModelSelector = FileSelector(self.groupBox_6)
        self.dependencies_knnModelSelector.setObjectName(u"dependencies_knnModelSelector")

        self.gridLayout.addWidget(self.dependencies_knnModelSelector, 0, 4, 1, 1)

        self.dependencies_b30KnnModelSelector = FileSelector(self.groupBox_6)
        self.dependencies_b30KnnModelSelector.setObjectName(u"dependencies_b30KnnModelSelector")

        self.gridLayout.addWidget(self.dependencies_b30KnnModelSelector, 1, 4, 1, 1)

        self.dependencies_phashDatabaseSelector = FileSelector(self.groupBox_6)
        self.dependencies_phashDatabaseSelector.setObjectName(u"dependencies_phashDatabaseSelector")

        self.gridLayout.addWidget(self.dependencies_phashDatabaseSelector, 2, 4, 1, 1)

        self.gridLayout.setColumnStretch(4, 1)

        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.ocrQueue = OcrQueue(TabOcr_B30)
        self.ocrQueue.setObjectName(u"ocrQueue")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ocrQueue.sizePolicy().hasHeightForWidth())
        self.ocrQueue.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.ocrQueue)


        self.retranslateUi(TabOcr_B30)

        QMetaObject.connectSlotsByName(TabOcr_B30)
    # setupUi

    def retranslateUi(self, TabOcr_B30):
        self.groupBox.setTitle(QCoreApplication.translate("TabOcr_B30", u"b30type", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TabOcr_B30", u"dependencies.title", None))
        self.label.setText(QCoreApplication.translate("TabOcr_B30", u"dependencies.knnModel", None))
        self.label_2.setText(QCoreApplication.translate("TabOcr_B30", u"dependencies.b30KnnModel", None))
        self.label_3.setText(QCoreApplication.translate("TabOcr_B30", u"dependencies.phashDatabase", None))
        pass
    # retranslateUi

