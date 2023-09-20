# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartAndScoreInput.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QSizePolicy, QVBoxLayout,
    QWidget)

from ui.implements.components.chartSelector import ChartSelector
from ui.implements.components.scoreEditor import ScoreEditor

class Ui_ChartAndScoreInput(object):
    def setupUi(self, ChartAndScoreInput):
        if not ChartAndScoreInput.objectName():
            ChartAndScoreInput.setObjectName(u"ChartAndScoreInput")
        ChartAndScoreInput.resize(400, 450)
        ChartAndScoreInput.setWindowTitle(u"ChartAndScoreInput")
        self.verticalLayout = QVBoxLayout(ChartAndScoreInput)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(ChartAndScoreInput)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chartSelector = ChartSelector(self.groupBox)
        self.chartSelector.setObjectName(u"chartSelector")

        self.verticalLayout_2.addWidget(self.chartSelector)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(ChartAndScoreInput)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scoreEditor = ScoreEditor(self.groupBox_2)
        self.scoreEditor.setObjectName(u"scoreEditor")

        self.verticalLayout_3.addWidget(self.scoreEditor)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(ChartAndScoreInput)

        QMetaObject.connectSlotsByName(ChartAndScoreInput)
    # setupUi

    def retranslateUi(self, ChartAndScoreInput):
        self.groupBox.setTitle(QCoreApplication.translate("ChartAndScoreInput", u"selectChart", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ChartAndScoreInput", u"editScore", None))
        pass
    # retranslateUi

