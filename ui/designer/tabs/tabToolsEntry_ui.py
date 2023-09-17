# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabToolsEntry.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

from ui.implements.tabs.tabTools.tabTools_InfoLookup import TabTools_InfoLookup
from ui.implements.tabs.tabTools.tabTools_StepCalculator import TabTools_StepCalculator

class Ui_TabToolsEntry(object):
    def setupUi(self, TabToolsEntry):
        if not TabToolsEntry.objectName():
            TabToolsEntry.setObjectName(u"TabToolsEntry")
        TabToolsEntry.resize(500, 400)
        TabToolsEntry.setWindowTitle(u"TabToolsEntry")
        self.verticalLayout = QVBoxLayout(TabToolsEntry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(TabToolsEntry)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = TabTools_InfoLookup()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = TabTools_StepCalculator()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(TabToolsEntry)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabToolsEntry)
    # setupUi

    def retranslateUi(self, TabToolsEntry):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TabToolsEntry", u"tab.infoLookup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TabToolsEntry", u"tab.stepCalculator", None))
        pass
    # retranslateUi

