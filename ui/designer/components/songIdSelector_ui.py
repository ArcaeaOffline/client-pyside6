# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'songIdSelector.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SongIdSelector(object):
    def setupUi(self, SongIdSelector):
        if not SongIdSelector.objectName():
            SongIdSelector.setObjectName(u"SongIdSelector")
        SongIdSelector.resize(470, 350)
        SongIdSelector.setWindowTitle(u"SongIdSelector")
        self.verticalLayout_2 = QVBoxLayout(SongIdSelector)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.songIdSelectorQuickActionsGroupBox = QGroupBox(SongIdSelector)
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


        self.verticalLayout_2.addWidget(self.songIdSelectorQuickActionsGroupBox)

        self.searchLineEdit = QLineEdit(SongIdSelector)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setFrame(True)
        self.searchLineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.searchLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.packComboBox = QComboBox(SongIdSelector)
        self.packComboBox.setObjectName(u"packComboBox")

        self.verticalLayout_2.addWidget(self.packComboBox)

        self.songIdComboBox = QComboBox(SongIdSelector)
        self.songIdComboBox.setObjectName(u"songIdComboBox")

        self.verticalLayout_2.addWidget(self.songIdComboBox)


        self.retranslateUi(SongIdSelector)

        QMetaObject.connectSlotsByName(SongIdSelector)
    # setupUi

    def retranslateUi(self, SongIdSelector):
        self.songIdSelectorQuickActionsGroupBox.setTitle(QCoreApplication.translate("SongIdSelector", u"songIdSelector.quickActions", None))
        self.nextPackageButton.setText(QCoreApplication.translate("SongIdSelector", u"songIdSelector.quickActions.nextPackageButton", None))
        self.nextSongIdButton.setText(QCoreApplication.translate("SongIdSelector", u"songIdSelector.quickActions.nextSongIdButton", None))
        self.previousSongIdButton.setText(QCoreApplication.translate("SongIdSelector", u"songIdSelector.quickActions.previousSongIdButton", None))
        self.previousPackageButton.setText(QCoreApplication.translate("SongIdSelector", u"songIdSelector.quickActions.previousPackageButton", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("SongIdSelector", u"search.lineEdit.placeholder", None))
        pass
    # retranslateUi

