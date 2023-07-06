# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabInputScore.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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

class Ui_TabInputScore(object):
    def setupUi(self, TabInputScore):
        if not TabInputScore.objectName():
            TabInputScore.setObjectName(u"TabInputScore")
        TabInputScore.resize(514, 400)
        TabInputScore.setWindowTitle(u"TabInputScore")
        self.verticalLayout = QVBoxLayout(TabInputScore)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(TabInputScore)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chartSelector = ChartSelector(self.groupBox)
        self.chartSelector.setObjectName(u"chartSelector")

        self.verticalLayout_2.addWidget(self.chartSelector)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TabInputScore)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scoreEditor = ScoreEditor(self.groupBox_2)
        self.scoreEditor.setObjectName(u"scoreEditor")

        self.verticalLayout_3.addWidget(self.scoreEditor)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(TabInputScore)

        QMetaObject.connectSlotsByName(TabInputScore)
    # setupUi

    def retranslateUi(self, TabInputScore):
        self.groupBox.setTitle(QCoreApplication.translate("TabInputScore", u"tab.selectChart", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabInputScore", u"tab.scoreEdit", None))
        pass
    # retranslateUi

