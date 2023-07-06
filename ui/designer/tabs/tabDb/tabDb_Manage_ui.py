# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabDb_Manage.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_TabDb_Manage(object):
    def setupUi(self, TabDb_Manage):
        if not TabDb_Manage.objectName():
            TabDb_Manage.setObjectName(u"TabDb_Manage")
        TabDb_Manage.resize(630, 528)
        TabDb_Manage.setWindowTitle(u"TabDb_Manage")
        self.formLayout = QFormLayout(TabDb_Manage)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.syncArcSongDbButton = QPushButton(TabDb_Manage)
        self.syncArcSongDbButton.setObjectName(u"syncArcSongDbButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.syncArcSongDbButton)

        self.label = QLabel(TabDb_Manage)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.retranslateUi(TabDb_Manage)

        QMetaObject.connectSlotsByName(TabDb_Manage)
    # setupUi

    def retranslateUi(self, TabDb_Manage):
        self.syncArcSongDbButton.setText(QCoreApplication.translate("TabDb_Manage", u"syncArcSongDbButton", None))
        self.label.setText(QCoreApplication.translate("TabDb_Manage", u"syncArcSongDb.description", None))
        pass
    # retranslateUi

