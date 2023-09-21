# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabAbout.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TabAbout(object):
    def setupUi(self, TabAbout):
        if not TabAbout.objectName():
            TabAbout.setObjectName(u"TabAbout")
        TabAbout.resize(550, 400)
        TabAbout.setWindowTitle(u"TabAbout")
        self.verticalLayout = QVBoxLayout(TabAbout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logoLabel = QLabel(TabAbout)
        self.logoLabel.setObjectName(u"logoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setText(u"")
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logoLabel)

        self.label = QLabel(TabAbout)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText(u"arcaea-offline-pyside-ui")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(TabAbout)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"A part of <a href=\"https://github.com/283375/arcaea-offline\">arcaea-offline project</a>")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.aboutQtButton = QPushButton(TabAbout)
        self.aboutQtButton.setObjectName(u"aboutQtButton")

        self.horizontalLayout.addWidget(self.aboutQtButton)

        self.versionInfoButton = QPushButton(TabAbout)
        self.versionInfoButton.setObjectName(u"versionInfoButton")

        self.horizontalLayout.addWidget(self.versionInfoButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TabAbout)

        QMetaObject.connectSlotsByName(TabAbout)
    # setupUi

    def retranslateUi(self, TabAbout):
        self.aboutQtButton.setText(QCoreApplication.translate("TabAbout", u"About Qt", None))
        self.versionInfoButton.setText(QCoreApplication.translate("TabAbout", u"Version Info", None))
        pass
    # retranslateUi

