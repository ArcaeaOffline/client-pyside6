# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOverview.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TabOverview(object):
    def setupUi(self, TabOverview):
        if not TabOverview.objectName():
            TabOverview.setObjectName(u"TabOverview")
        TabOverview.resize(696, 509)
        TabOverview.setWindowTitle(u"TabOverview")
        self.verticalLayout = QVBoxLayout(TabOverview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(TabOverview)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(TabOverview)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.b30Label = QLabel(self.widget_3)
        self.b30Label.setObjectName(u"b30Label")
        font = QFont()
        font.setPointSize(30)
        self.b30Label.setFont(font)
        self.b30Label.setText(u"0.00")
        self.b30Label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.b30Label)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_2.setText(u"B30")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.r10Label = QLabel(self.widget_4)
        self.r10Label.setObjectName(u"r10Label")
        self.r10Label.setEnabled(False)
        self.r10Label.setFont(font)
        self.r10Label.setText(u"--")
        self.r10Label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.r10Label)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setFont(font1)
        self.label_4.setText(u"R10")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(TabOverview)

        QMetaObject.connectSlotsByName(TabOverview)
    # setupUi

    def retranslateUi(self, TabOverview):
        pass
    # retranslateUi

