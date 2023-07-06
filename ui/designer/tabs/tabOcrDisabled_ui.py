# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcrDisabled.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_TabOcrDisabled(object):
    def setupUi(self, TabOcrDisabled):
        if not TabOcrDisabled.objectName():
            TabOcrDisabled.setObjectName(u"TabOcrDisabled")
        TabOcrDisabled.resize(564, 468)
        TabOcrDisabled.setWindowTitle(u"TabOcrDisabled")
        self.gridLayout = QGridLayout(TabOcrDisabled)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.widget = QWidget(TabOcrDisabled)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.contentLabel = QLabel(self.widget)
        self.contentLabel.setObjectName(u"contentLabel")
        sizePolicy.setHeightForWidth(self.contentLabel.sizePolicy().hasHeightForWidth())
        self.contentLabel.setSizePolicy(sizePolicy)
        self.contentLabel.setText(u"...")

        self.verticalLayout.addWidget(self.contentLabel)


        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)


        self.retranslateUi(TabOcrDisabled)

        QMetaObject.connectSlotsByName(TabOcrDisabled)
    # setupUi

    def retranslateUi(self, TabOcrDisabled):
        self.label.setText(QCoreApplication.translate("TabOcrDisabled", u"ocrDisabled.title", None))
        pass
    # retranslateUi

