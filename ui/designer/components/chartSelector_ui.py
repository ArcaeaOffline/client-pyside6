# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartSelector.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from ui.implements.components.ratingClassRadioButton import RatingClassRadioButton

class Ui_ChartSelector(object):
    def setupUi(self, ChartSelector):
        if not ChartSelector.objectName():
            ChartSelector.setObjectName(u"ChartSelector")
        ChartSelector.resize(671, 295)
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
        self.horizontalLayout = QHBoxLayout(self.songIdSelectorGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.songIdSelectorGroupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fuzzySearchLineEdit = QLineEdit(self.widget)
        self.fuzzySearchLineEdit.setObjectName(u"fuzzySearchLineEdit")
        self.fuzzySearchLineEdit.setFrame(True)
        self.fuzzySearchLineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.fuzzySearchLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.packageComboBox = QComboBox(self.widget)
        self.packageComboBox.setObjectName(u"packageComboBox")

        self.verticalLayout.addWidget(self.packageComboBox)

        self.songIdComboBox = QComboBox(self.widget)
        self.songIdComboBox.setObjectName(u"songIdComboBox")

        self.verticalLayout.addWidget(self.songIdComboBox)


        self.horizontalLayout.addWidget(self.widget)

        self.songIdSelectorQuickActionsGroupBox = QGroupBox(self.songIdSelectorGroupBox)
        self.songIdSelectorQuickActionsGroupBox.setObjectName(u"songIdSelectorQuickActionsGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.songIdSelectorQuickActionsGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.previousPackageButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.previousPackageButton.setObjectName(u"previousPackageButton")

        self.verticalLayout_2.addWidget(self.previousPackageButton)

        self.previousSongIdButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.previousSongIdButton.setObjectName(u"previousSongIdButton")

        self.verticalLayout_2.addWidget(self.previousSongIdButton)

        self.nextSongIdButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.nextSongIdButton.setObjectName(u"nextSongIdButton")

        self.verticalLayout_2.addWidget(self.nextSongIdButton)

        self.nextPackageButton = QPushButton(self.songIdSelectorQuickActionsGroupBox)
        self.nextPackageButton.setObjectName(u"nextPackageButton")

        self.verticalLayout_2.addWidget(self.nextPackageButton)


        self.horizontalLayout.addWidget(self.songIdSelectorQuickActionsGroupBox)


        self.mainVerticalLayout.addWidget(self.songIdSelectorGroupBox)

        self.ratingClassGroupBox = QGroupBox(ChartSelector)
        self.ratingClassGroupBox.setObjectName(u"ratingClassGroupBox")
        self.ratingClassGroupBox.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.ratingClassGroupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pstButton = RatingClassRadioButton(self.ratingClassGroupBox)
        self.pstButton.setObjectName(u"pstButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pstButton.sizePolicy().hasHeightForWidth())
        self.pstButton.setSizePolicy(sizePolicy1)
        self.pstButton.setText(u"PAST")
        self.pstButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.pstButton)

        self.prsButton = RatingClassRadioButton(self.ratingClassGroupBox)
        self.prsButton.setObjectName(u"prsButton")
        sizePolicy1.setHeightForWidth(self.prsButton.sizePolicy().hasHeightForWidth())
        self.prsButton.setSizePolicy(sizePolicy1)
        self.prsButton.setText(u"PRESENT")
        self.prsButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.prsButton)

        self.ftrButton = RatingClassRadioButton(self.ratingClassGroupBox)
        self.ftrButton.setObjectName(u"ftrButton")
        sizePolicy1.setHeightForWidth(self.ftrButton.sizePolicy().hasHeightForWidth())
        self.ftrButton.setSizePolicy(sizePolicy1)
        self.ftrButton.setText(u"FUTURE")
        self.ftrButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.ftrButton)

        self.bydButton = RatingClassRadioButton(self.ratingClassGroupBox)
        self.bydButton.setObjectName(u"bydButton")
        self.bydButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.bydButton.sizePolicy().hasHeightForWidth())
        self.bydButton.setSizePolicy(sizePolicy1)
        self.bydButton.setText(u"BEYOND")
        self.bydButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.bydButton)


        self.mainVerticalLayout.addWidget(self.ratingClassGroupBox)

        self.resultsHorizontalLayout = QHBoxLayout()
        self.resultsHorizontalLayout.setObjectName(u"resultsHorizontalLayout")
        self.resultLabel = QLabel(ChartSelector)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy2)
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
        self.fuzzySearchLineEdit.setPlaceholderText(QCoreApplication.translate("ChartSelector", u"fuzzySearch.lineEdit.placeholder", None))
        self.songIdSelectorQuickActionsGroupBox.setTitle(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions", None))
        self.previousPackageButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.previousPackageButton", None))
        self.previousSongIdButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.previousSongIdButton", None))
        self.nextSongIdButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.nextSongIdButton", None))
        self.nextPackageButton.setText(QCoreApplication.translate("ChartSelector", u"songIdSelector.quickActions.nextPackageButton", None))
        self.ratingClassGroupBox.setTitle(QCoreApplication.translate("ChartSelector", u"ratingClassSelector.title", None))
        self.resetButton.setText(QCoreApplication.translate("ChartSelector", u"resetButton", None))
        pass
    # retranslateUi

