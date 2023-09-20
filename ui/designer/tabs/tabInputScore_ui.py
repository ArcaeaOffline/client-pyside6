# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabInputScore.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from ui.implements.components.chartAndScoreInput import ChartAndScoreInput

class Ui_TabInputScore(object):
    def setupUi(self, TabInputScore):
        if not TabInputScore.objectName():
            TabInputScore.setObjectName(u"TabInputScore")
        TabInputScore.resize(500, 400)
        TabInputScore.setWindowTitle(u"TabInputScore")
        self.verticalLayout = QVBoxLayout(TabInputScore)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chartAndScoreInput = ChartAndScoreInput(TabInputScore)
        self.chartAndScoreInput.setObjectName(u"chartAndScoreInput")

        self.verticalLayout.addWidget(self.chartAndScoreInput)


        self.retranslateUi(TabInputScore)

        QMetaObject.connectSlotsByName(TabInputScore)
    # setupUi

    def retranslateUi(self, TabInputScore):
        pass
    # retranslateUi

