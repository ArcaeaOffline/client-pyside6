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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from ui.implements.components.ratingClassSelector import RatingClassSelector

class Ui_ChartSelector(object):
    def setupUi(self, ChartSelector):
        if not ChartSelector.objectName():
            ChartSelector.setObjectName(u"ChartSelector")
        ChartSelector.resize(476, 347)
        ChartSelector.setWindowTitle(u"ChartSelector")
        self.mainVerticalLayout = QVBoxLayout(ChartSelector)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.songIdSelectorGroupBox = QGroupBox(ChartSelector)
        self.songIdSelectorGroupBox.setObjectName(u"songIdSelectorGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songIdSelectorGroupBox.sizePolicy().hasHeightForWidth())
        self.songIdSelectorGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.songIdSelectorGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.songIdSelectorQuickActionsGroupBox = QGroupBox(self.songIdSelectorGroupBox)
        self.songIdSelectorQuickActionsGroupBox.setObjectName(u"songIdSelectorQuickActionsGroupBox")
        self.horizontalLayout = QHBoxLayout(self.songIdSelectorQuickActionsGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nextPackageButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.nextPackageButton.setObjectName(u"nextPackageButton")
        self.nextPackageButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.nextPackageButton)

        self.nextSongIdButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.nextSongIdButton.setObjectName(u"nextSongIdButton")
        self.nextSongIdButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.nextSongIdButton)

        self.previousSongIdButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.previousSongIdButton.setObjectName(u"previousSongIdButton")
        self.previousSongIdButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.previousSongIdButton)

        self.previousPackageButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.previousPackageButton.setObjectName(u"previousPackageButton")
        self.previousPackageButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.previousPackageButton)


        self.verticalLayout_3.addWidget(self.songIdSelectorQuickActionsGroupBox)

        self.widget = QWidget(self.songIdSelectorGroupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLineEdit = QLineEdit(self.widget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setFrame(True)
        self.searchLineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.searchLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.packComboBox = QComboBox(self.widget)
        self.packComboBox.setObjectName(u"packComboBox")

        self.verticalLayout.addWidget(self.packComboBox)

        self.songIdComboBox = QComboBox(self.widget)
        self.songIdComboBox.setObjectName(u"songIdComboBox")

        self.verticalLayout.addWidget(self.songIdComboBox)


        self.verticalLayout_3.addWidget(self.widget)


        self.mainVerticalLayout.addWidget(self.songIdSelectorGroupBox)

        self.ratingClassSelector = RatingClassSelector(ChartSelector)
        self.ratingClassSelector.setObjectName(u"ratingClassSelector")

        self.mainVerticalLayout.addWidget(self.ratingClassSelector)

        self.resultsHorizontalLayout = QHBoxLayout()
        self.resultsHorizontalLayout.setObjectName(u"resultsHorizontalLayout")
        self.resultLabel = QLabel(ChartSelector)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy1)
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
        self.songIdSelectorQuickActionsGroupBox.setTitle(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions", None))
        self.nextPackageButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.nextPackageButton", None))
        self.nextSongIdButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.nextSongIdButton", None))
        self.previousSongIdButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.previousSongIdButton", None))
        self.previousPackageButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.previousPackageButton", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("ChartSelector", u"search.lineEdit.placeholder", None))
        self.resetButton.setText(QCoreApplication.translate("ChartSelector", u"resetButton", None))
        pass
    # retranslateUi

