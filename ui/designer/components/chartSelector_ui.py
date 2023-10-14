# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartSelector.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from ui.implements.components.ratingClassSelector import RatingClassSelector
from ui.implements.components.songIdSelector import SongIdSelector

class Ui_ChartSelector(object):
    def setupUi(self, ChartSelector):
        if not ChartSelector.objectName():
            ChartSelector.setObjectName(u"ChartSelector")
        ChartSelector.resize(476, 93)
        ChartSelector.setWindowTitle(u"ChartSelector")
        self.mainVerticalLayout = QVBoxLayout(ChartSelector)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.songIdSelectorGroupBox = QGroupBox(ChartSelector)
        self.songIdSelectorGroupBox.setObjectName(u"songIdSelectorGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.songIdSelectorGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.songIdSelector = SongIdSelector(self.songIdSelectorGroupBox)
        self.songIdSelector.setObjectName(u"songIdSelector")

        self.verticalLayout_3.addWidget(self.songIdSelector)


        self.mainVerticalLayout.addWidget(self.songIdSelectorGroupBox)

        self.ratingClassSelector = RatingClassSelector(ChartSelector)
        self.ratingClassSelector.setObjectName(u"ratingClassSelector")

        self.mainVerticalLayout.addWidget(self.ratingClassSelector)

        self.resultsHorizontalLayout = QHBoxLayout()
        self.resultsHorizontalLayout.setObjectName(u"resultsHorizontalLayout")
        self.resultLabel = QLabel(ChartSelector)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy)
        self.resultLabel.setText(u"...")
        self.resultLabel.setTextFormat(Qt.RichText)

        self.resultsHorizontalLayout.addWidget(self.resultLabel)

        self.resetButton = QPushButton(ChartSelector)
        self.resetButton.setObjectName(u"resetButton")

        self.resultsHorizontalLayout.addWidget(self.resetButton)


        self.mainVerticalLayout.addLayout(self.resultsHorizontalLayout)


        self.retranslateUi(ChartSelector)

        QMetaObject.connectSlotsByName(ChartSelector)
    # setupUi

    def retranslateUi(self, ChartSelector):
        self.songIdSelectorGroupBox.setTitle(QCoreApplication.translate("ChartSelector", u"songIdSelector.title", None))
        self.resetButton.setText(QCoreApplication.translate("ChartSelector", u"resetButton", None))
        pass
    # retranslateUi

