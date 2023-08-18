# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcrEntry.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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

from ui.implements.tabs.tabOcr.tabOcr_B30 import TabOcr_B30
from ui.implements.tabs.tabOcr.tabOcr_Device import TabOcr_Device

class Ui_TabOcrEntry(object):
    def setupUi(self, TabOcrEntry):
        if not TabOcrEntry.objectName():
            TabOcrEntry.setObjectName(u"TabOcrEntry")
        TabOcrEntry.resize(600, 478)
        TabOcrEntry.setWindowTitle(u"TabOcrEntry")
        self.verticalLayout = QVBoxLayout(TabOcrEntry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(TabOcrEntry)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = TabOcr_Device()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = TabOcr_B30()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(TabOcrEntry)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabOcrEntry)
    # setupUi

    def retranslateUi(self, TabOcrEntry):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TabOcrEntry", u"tab.device", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TabOcrEntry", u"tab.b30", None))
        pass
    # retranslateUi

