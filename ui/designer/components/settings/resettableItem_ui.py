# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resettableItem.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_ResettableItem(object):
    def setupUi(self, ResettableItem):
        if not ResettableItem.objectName():
            ResettableItem.setObjectName(u"ResettableItem")
        ResettableItem.resize(559, 42)
        ResettableItem.setWindowTitle(u"ResettableItem")
        self.horizontalLayout = QHBoxLayout(ResettableItem)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.resetButton = QPushButton(ResettableItem)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout.addWidget(self.resetButton)


        self.retranslateUi(ResettableItem)

        QMetaObject.connectSlotsByName(ResettableItem)
    # setupUi

    def retranslateUi(self, ResettableItem):
        self.resetButton.setText(QCoreApplication.translate("ResettableItem", u"resetButton", None))
        pass
    # retranslateUi

