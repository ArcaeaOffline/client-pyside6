# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDefault.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

from ui.implements.components.devicesComboBox import DevicesComboBox
from ui.implements.components.fileSelector import FileSelector

class Ui_SettingsDefault(object):
    def setupUi(self, SettingsDefault):
        if not SettingsDefault.objectName():
            SettingsDefault.setObjectName(u"SettingsDefault")
        SettingsDefault.resize(682, 493)
        SettingsDefault.setWindowTitle(u"SettingsDefault")
        self.gridLayout = QGridLayout(SettingsDefault)
        self.gridLayout.setObjectName(u"gridLayout")
        self.devicesComboBox = DevicesComboBox(SettingsDefault)
        self.devicesComboBox.setObjectName(u"devicesComboBox")
        self.devicesComboBox.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.devicesComboBox, 1, 1, 1, 1)

        self.label_3 = QLabel(SettingsDefault)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(SettingsDefault)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.tesseractFileSelector = FileSelector(SettingsDefault)
        self.tesseractFileSelector.setObjectName(u"tesseractFileSelector")
        self.tesseractFileSelector.setEnabled(False)
        self.tesseractFileSelector.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.tesseractFileSelector, 2, 1, 1, 1)

        self.devicesJsonFileSelector = FileSelector(SettingsDefault)
        self.devicesJsonFileSelector.setObjectName(u"devicesJsonFileSelector")
        self.devicesJsonFileSelector.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.devicesJsonFileSelector, 0, 1, 1, 1)

        self.label_2 = QLabel(SettingsDefault)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.deviceUuidResetButton = QPushButton(SettingsDefault)
        self.deviceUuidResetButton.setObjectName(u"deviceUuidResetButton")

        self.gridLayout.addWidget(self.deviceUuidResetButton, 1, 2, 1, 1)

        self.label = QLabel(SettingsDefault)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.devicesJsonFileResetButton = QPushButton(SettingsDefault)
        self.devicesJsonFileResetButton.setObjectName(u"devicesJsonFileResetButton")

        self.gridLayout.addWidget(self.devicesJsonFileResetButton, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 500000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.label_5 = QLabel(SettingsDefault)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.knnModelFileSelector = FileSelector(SettingsDefault)
        self.knnModelFileSelector.setObjectName(u"knnModelFileSelector")

        self.gridLayout.addWidget(self.knnModelFileSelector, 3, 1, 1, 1)

        self.siftDatabaseFileSelector = FileSelector(SettingsDefault)
        self.siftDatabaseFileSelector.setObjectName(u"siftDatabaseFileSelector")

        self.gridLayout.addWidget(self.siftDatabaseFileSelector, 4, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(SettingsDefault)

        QMetaObject.connectSlotsByName(SettingsDefault)
    # setupUi

    def retranslateUi(self, SettingsDefault):
        self.label_3.setText(QCoreApplication.translate("SettingsDefault", u"deviceUuid", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDefault", u"tesseractFile", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDefault", u"devicesJsonFile", None))
        self.deviceUuidResetButton.setText(QCoreApplication.translate("SettingsDefault", u"resetButton", None))
        self.label.setText(QCoreApplication.translate("SettingsDefault", u"knnModelFile", None))
        self.devicesJsonFileResetButton.setText(QCoreApplication.translate("SettingsDefault", u"resetButton", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDefault", u"siftDatabaseFile", None))
        pass
    # retranslateUi

