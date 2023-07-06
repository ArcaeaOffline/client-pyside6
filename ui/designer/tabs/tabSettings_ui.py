# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabSettings.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QListWidget, QListWidgetItem, QSizePolicy, QStackedWidget,
    QWidget)

from ui.implements.settings.settingsDefault import SettingsDefault

class Ui_TabSettings(object):
    def setupUi(self, TabSettings):
        if not TabSettings.objectName():
            TabSettings.setObjectName(u"TabSettings")
        TabSettings.resize(562, 499)
        TabSettings.setWindowTitle(u"TabSettings")
        self.horizontalLayout = QHBoxLayout(TabSettings)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(TabSettings)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(100, 0))
        self.listWidget.setBaseSize(QSize(100, 0))
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout.addWidget(self.listWidget)

        self.stackedWidget = QStackedWidget(TabSettings)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.page_default = SettingsDefault()
        self.page_default.setObjectName(u"page_default")
        self.stackedWidget.addWidget(self.page_default)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(TabSettings)

        QMetaObject.connectSlotsByName(TabSettings)
    # setupUi

    def retranslateUi(self, TabSettings):
        pass
    # retranslateUi

