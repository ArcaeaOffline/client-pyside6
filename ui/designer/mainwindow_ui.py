# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from ui.implements.tabs.tabAbout import TabAbout
from ui.implements.tabs.tabDbEntry import TabDbEntry
from ui.implements.tabs.tabInputScore import TabInputScore
from ui.implements.tabs.tabOverview import TabOverview
from ui.implements.tabs.tabSettings import TabSettings

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 601)
        MainWindow.setWindowTitle(u"Arcaea Offline")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_overview = TabOverview()
        self.tab_overview.setObjectName(u"tab_overview")
        self.tabWidget.addTab(self.tab_overview, "")
        self.tab_input = TabInputScore()
        self.tab_input.setObjectName(u"tab_input")
        self.tabWidget.addTab(self.tab_input, "")
        self.tab_db = TabDbEntry()
        self.tab_db.setObjectName(u"tab_db")
        self.tabWidget.addTab(self.tab_db, "")
        self.tab_ocr = QWidget()
        self.tab_ocr.setObjectName(u"tab_ocr")
        self.tabWidget.addTab(self.tab_ocr, "")
        self.tab_settings = TabSettings()
        self.tab_settings.setObjectName(u"tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.tab_about = TabAbout()
        self.tab_about.setObjectName(u"tab_about")
        self.tabWidget.addTab(self.tab_about, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), QCoreApplication.translate("MainWindow", u"tab.overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_input), QCoreApplication.translate("MainWindow", u"tab.input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_db), QCoreApplication.translate("MainWindow", u"tab.db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ocr), QCoreApplication.translate("MainWindow", u"tab.ocr", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"tab.settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"tab.about", None))
        pass
    # retranslateUi

