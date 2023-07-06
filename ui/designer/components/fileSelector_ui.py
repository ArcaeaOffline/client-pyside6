# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileSelector.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

from ui.implements.components.elidedLabel import ElidedLabel

class Ui_FileSelector(object):
    def setupUi(self, FileSelector):
        if not FileSelector.objectName():
            FileSelector.setObjectName(u"FileSelector")
        FileSelector.resize(559, 42)
        FileSelector.setWindowTitle(u"FileSelector")
        self.horizontalLayout_2 = QHBoxLayout(FileSelector)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.elidedLabel = ElidedLabel(FileSelector)
        self.elidedLabel.setObjectName(u"elidedLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elidedLabel.sizePolicy().hasHeightForWidth())
        self.elidedLabel.setSizePolicy(sizePolicy)
        self.elidedLabel.setText(u"...")

        self.horizontalLayout_2.addWidget(self.elidedLabel)

        self.selectButton = QPushButton(FileSelector)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout_2.addWidget(self.selectButton)


        self.retranslateUi(FileSelector)

        QMetaObject.connectSlotsByName(FileSelector)
    # setupUi

    def retranslateUi(self, FileSelector):
        self.selectButton.setText(QCoreApplication.translate("FileSelector", u"selectButton", None))
        pass
    # retranslateUi

