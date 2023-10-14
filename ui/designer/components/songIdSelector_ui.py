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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SongIdSelector(object):
    def setupUi(self, SongIdSelector):
        if not SongIdSelector.objectName():
            SongIdSelector.setObjectName(u"SongIdSelector")
        SongIdSelector.resize(350, 102)
        SongIdSelector.setWindowTitle(u"SongIdSelector")
        self.verticalLayout_2 = QVBoxLayout(SongIdSelector)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.searchLineEdit = QLineEdit(SongIdSelector)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setFrame(True)
        self.searchLineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.searchLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.previousPackageButton = QPushButton(SongIdSelector)
        self.previousPackageButton.setObjectName(u"previousPackageButton")
        self.previousPackageButton.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.previousPackageButton)

        self.packComboBox = QComboBox(SongIdSelector)
        self.packComboBox.setObjectName(u"packComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packComboBox.sizePolicy().hasHeightForWidth())
        self.packComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.packComboBox)

        self.nextPackageButton = QPushButton(SongIdSelector)
        self.nextPackageButton.setObjectName(u"nextPackageButton")
        self.nextPackageButton.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.nextPackageButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.previousSongIdButton = QPushButton(SongIdSelector)
        self.previousSongIdButton.setObjectName(u"previousSongIdButton")
        self.previousSongIdButton.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_3.addWidget(self.previousSongIdButton)

        self.songIdComboBox = QComboBox(SongIdSelector)
        self.songIdComboBox.setObjectName(u"songIdComboBox")
        sizePolicy.setHeightForWidth(self.songIdComboBox.sizePolicy().hasHeightForWidth())
        self.songIdComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.songIdComboBox)

        self.nextSongIdButton = QPushButton(SongIdSelector)
        self.nextSongIdButton.setObjectName(u"nextSongIdButton")
        self.nextSongIdButton.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_3.addWidget(self.nextSongIdButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(SongIdSelector)

        QMetaObject.connectSlotsByName(SongIdSelector)
    # setupUi

    def retranslateUi(self, SongIdSelector):
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("SongIdSelector", u"search.lineEdit.placeholder", None))
        self.previousPackageButton.setText(QCoreApplication.translate("SongIdSelector", u"previous", None))
        self.nextPackageButton.setText(QCoreApplication.translate("SongIdSelector", u"next", None))
        self.previousSongIdButton.setText(QCoreApplication.translate("SongIdSelector", u"previous", None))
        self.nextSongIdButton.setText(QCoreApplication.translate("SongIdSelector", u"next", None))
        pass
    # retranslateUi

