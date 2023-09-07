# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsBaseWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SettingsBaseWidget(object):
    def setupUi(self, SettingsBaseWidget):
        if not SettingsBaseWidget.objectName():
            SettingsBaseWidget.setObjectName(u"SettingsBaseWidget")
        SettingsBaseWidget.resize(641, 521)
        SettingsBaseWidget.setWindowTitle(u"SettingsBaseWidget")
        self.verticalLayout = QVBoxLayout(SettingsBaseWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(SettingsBaseWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setText(u"Title")

        self.verticalLayout.addWidget(self.titleLabel)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, -1, -1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(SettingsBaseWidget)

        QMetaObject.connectSlotsByName(SettingsBaseWidget)
    # setupUi

    def retranslateUi(self, SettingsBaseWidget):
        pass
    # retranslateUi

