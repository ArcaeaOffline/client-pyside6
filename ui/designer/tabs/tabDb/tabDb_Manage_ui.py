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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_TabDb_Manage(object):
    def setupUi(self, TabDb_Manage):
        if not TabDb_Manage.objectName():
            TabDb_Manage.setObjectName(u"TabDb_Manage")
        TabDb_Manage.resize(580, 521)
        TabDb_Manage.setWindowTitle(u"TabDb_Manage")
        self.formLayout = QFormLayout(TabDb_Manage)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.importPacklistButton = QPushButton(TabDb_Manage)
        self.importPacklistButton.setObjectName(u"importPacklistButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.importPacklistButton)

        self.label_4 = QLabel(TabDb_Manage)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_4)

        self.importSonglistButton = QPushButton(TabDb_Manage)
        self.importSonglistButton.setObjectName(u"importSonglistButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.importSonglistButton)

        self.label_5 = QLabel(TabDb_Manage)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_5)

        self.importApkButton = QPushButton(TabDb_Manage)
        self.importApkButton.setObjectName(u"importApkButton")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.importApkButton)

        self.label_7 = QLabel(TabDb_Manage)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_7)

        self.label_11 = QLabel(TabDb_Manage)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_11.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label_11)

        self.syncArcSongDbButton = QPushButton(TabDb_Manage)
        self.syncArcSongDbButton.setObjectName(u"syncArcSongDbButton")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.syncArcSongDbButton)

        self.label = QLabel(TabDb_Manage)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label)

        self.label_12 = QLabel(TabDb_Manage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.label_12)

        self.importSt3Button = QPushButton(TabDb_Manage)
        self.importSt3Button.setObjectName(u"importSt3Button")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.importSt3Button)

        self.label_2 = QLabel(TabDb_Manage)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.label_2)

        self.importOnlineButton = QPushButton(TabDb_Manage)
        self.importOnlineButton.setObjectName(u"importOnlineButton")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.importOnlineButton)

        self.label_8 = QLabel(TabDb_Manage)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.label_8)

        self.label_13 = QLabel(TabDb_Manage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.label_13)

        self.exportScoresButton = QPushButton(TabDb_Manage)
        self.exportScoresButton.setObjectName(u"exportScoresButton")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.exportScoresButton)

        self.label_3 = QLabel(TabDb_Manage)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.label_3)

        self.exportSmartRteB30Button = QPushButton(TabDb_Manage)
        self.exportSmartRteB30Button.setObjectName(u"exportSmartRteB30Button")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.exportSmartRteB30Button)

        self.label_9 = QLabel(TabDb_Manage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.label_9)

        self.label_14 = QLabel(TabDb_Manage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.formLayout.setWidget(16, QFormLayout.SpanningRole, self.label_14)

        self.exportArcsongJsonButton = QPushButton(TabDb_Manage)
        self.exportArcsongJsonButton.setObjectName(u"exportArcsongJsonButton")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.exportArcsongJsonButton)

        self.label_6 = QLabel(TabDb_Manage)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.label_6)

        self.label_10 = QLabel(TabDb_Manage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_10)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout.setItem(11, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout.setItem(15, QFormLayout.LabelRole, self.verticalSpacer_4)


        self.retranslateUi(TabDb_Manage)

        QMetaObject.connectSlotsByName(TabDb_Manage)
    # setupUi

    def retranslateUi(self, TabDb_Manage):
        self.importPacklistButton.setText(QCoreApplication.translate("TabDb_Manage", u"importPacklistButton", None))
        self.label_4.setText(QCoreApplication.translate("TabDb_Manage", u"importPacklist.description", None))
        self.importSonglistButton.setText(QCoreApplication.translate("TabDb_Manage", u"importSonglistButton", None))
        self.label_5.setText(QCoreApplication.translate("TabDb_Manage", u"importSonglist.description", None))
        self.importApkButton.setText(QCoreApplication.translate("TabDb_Manage", u"importApkButton", None))
        self.label_7.setText(QCoreApplication.translate("TabDb_Manage", u"importApk.description", None))
        self.label_11.setText(QCoreApplication.translate("TabDb_Manage", u"chartInfoGroup", None))
        self.syncArcSongDbButton.setText(QCoreApplication.translate("TabDb_Manage", u"syncArcSongDbButton", None))
        self.label.setText(QCoreApplication.translate("TabDb_Manage", u"syncArcSongDb.description", None))
        self.label_12.setText(QCoreApplication.translate("TabDb_Manage", u"importScoreGroup", None))
        self.importSt3Button.setText(QCoreApplication.translate("TabDb_Manage", u"importSt3Button", None))
        self.label_2.setText(QCoreApplication.translate("TabDb_Manage", u"importSt3.description", None))
        self.importOnlineButton.setText(QCoreApplication.translate("TabDb_Manage", u"importOnlineButton", None))
        self.label_8.setText(QCoreApplication.translate("TabDb_Manage", u"importOnline.description", None))
        self.label_13.setText(QCoreApplication.translate("TabDb_Manage", u"exportScoreGroup", None))
        self.exportScoresButton.setText(QCoreApplication.translate("TabDb_Manage", u"exportScoresButton", None))
        self.label_3.setText(QCoreApplication.translate("TabDb_Manage", u"exportScores.description", None))
        self.exportSmartRteB30Button.setText(QCoreApplication.translate("TabDb_Manage", u"exportSmartRteB30Button", None))
        self.label_9.setText(QCoreApplication.translate("TabDb_Manage", u"exportSmartRteB30.description", None))
        self.label_14.setText(QCoreApplication.translate("TabDb_Manage", u"miscGroup", None))
        self.exportArcsongJsonButton.setText(QCoreApplication.translate("TabDb_Manage", u"exportArcsongJsonButton", None))
        self.label_6.setText(QCoreApplication.translate("TabDb_Manage", u"exportArcsongJson.description", None))
        self.label_10.setText(QCoreApplication.translate("TabDb_Manage", u"packSongInfoGroup", None))
        pass
    # retranslateUi
