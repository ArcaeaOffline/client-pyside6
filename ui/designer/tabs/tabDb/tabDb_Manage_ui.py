# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabDb_Manage.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

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

        self.importSt3Button = QPushButton(TabDb_Manage)
        self.importSt3Button.setObjectName(u"importSt3Button")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.importSt3Button)

        self.label_2 = QLabel(TabDb_Manage)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_2)

        self.line = QFrame(TabDb_Manage)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.line)

        self.exportScoresButton = QPushButton(TabDb_Manage)
        self.exportScoresButton.setObjectName(u"exportScoresButton")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.exportScoresButton)

        self.label_3 = QLabel(TabDb_Manage)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_3)

        self.line_2 = QFrame(TabDb_Manage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.line_2)

        self.importPacklistButton = QPushButton(TabDb_Manage)
        self.importPacklistButton.setObjectName(u"importPacklistButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.importPacklistButton)

        self.importSonglistButton = QPushButton(TabDb_Manage)
        self.importSonglistButton.setObjectName(u"importSonglistButton")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.importSonglistButton)

        self.label_4 = QLabel(TabDb_Manage)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_4)

        self.label_5 = QLabel(TabDb_Manage)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_5)

        self.exportArcsongJsonButton = QPushButton(TabDb_Manage)
        self.exportArcsongJsonButton.setObjectName(u"exportArcsongJsonButton")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.exportArcsongJsonButton)

        self.label_6 = QLabel(TabDb_Manage)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_6)

        self.importApkButton = QPushButton(TabDb_Manage)
        self.importApkButton.setObjectName(u"importApkButton")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.importApkButton)

        self.label_7 = QLabel(TabDb_Manage)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_7)


        self.retranslateUi(TabDb_Manage)

        QMetaObject.connectSlotsByName(TabDb_Manage)
    # setupUi

    def retranslateUi(self, TabDb_Manage):
        self.syncArcSongDbButton.setText(QCoreApplication.translate("TabDb_Manage", u"syncArcSongDbButton", None))
        self.label.setText(QCoreApplication.translate("TabDb_Manage", u"syncArcSongDb.description", None))
        self.importSt3Button.setText(QCoreApplication.translate("TabDb_Manage", u"importSt3Button", None))
        self.label_2.setText(QCoreApplication.translate("TabDb_Manage", u"importSt3.description", None))
        self.exportScoresButton.setText(QCoreApplication.translate("TabDb_Manage", u"exportScoresButton", None))
        self.label_3.setText(QCoreApplication.translate("TabDb_Manage", u"exportScores.description", None))
        self.importPacklistButton.setText(QCoreApplication.translate("TabDb_Manage", u"importPacklistButton", None))
        self.importSonglistButton.setText(QCoreApplication.translate("TabDb_Manage", u"importSonglistButton", None))
        self.label_4.setText(QCoreApplication.translate("TabDb_Manage", u"importPacklist.description", None))
        self.label_5.setText(QCoreApplication.translate("TabDb_Manage", u"importSonglist.description", None))
        self.exportArcsongJsonButton.setText(QCoreApplication.translate("TabDb_Manage", u"exportArcsongJsonButton", None))
        self.label_6.setText(QCoreApplication.translate("TabDb_Manage", u"exportArcsongJson.description", None))
        self.importApkButton.setText(QCoreApplication.translate("TabDb_Manage", u"importApkButton", None))
        self.label_7.setText(QCoreApplication.translate("TabDb_Manage", u"importApk.description", None))
        pass
    # retranslateUi

