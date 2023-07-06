# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDefault.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

from ui.implements.components import DevicesComboBox
from ui.implements.components.fileSelector import FileSelector

class Ui_SettingsDefault(object):
    def setupUi(self, SettingsDefault):
        if not SettingsDefault.objectName():
            SettingsDefault.setObjectName(u"SettingsDefault")
        SettingsDefault.resize(682, 493)
        SettingsDefault.setWindowTitle(u"SettingsDefault")
        self.formLayout = QFormLayout(SettingsDefault)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(SettingsDefault)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.devicesJsonFileSelector = FileSelector(SettingsDefault)
        self.devicesJsonFileSelector.setObjectName(u"devicesJsonFileSelector")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.devicesJsonFileSelector.sizePolicy().hasHeightForWidth())
        self.devicesJsonFileSelector.setSizePolicy(sizePolicy1)
        self.devicesJsonFileSelector.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.devicesJsonFileSelector)

        self.devicesJsonFileResetButton = QPushButton(SettingsDefault)
        self.devicesJsonFileResetButton.setObjectName(u"devicesJsonFileResetButton")

        self.horizontalLayout_2.addWidget(self.devicesJsonFileResetButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_3 = QLabel(SettingsDefault)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.devicesComboBox = DevicesComboBox(SettingsDefault)
        self.devicesComboBox.setObjectName(u"devicesComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.devicesComboBox.sizePolicy().hasHeightForWidth())
        self.devicesComboBox.setSizePolicy(sizePolicy2)
        self.devicesComboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.devicesComboBox)

        self.deviceUuidResetButton = QPushButton(SettingsDefault)
        self.deviceUuidResetButton.setObjectName(u"deviceUuidResetButton")

        self.horizontalLayout.addWidget(self.deviceUuidResetButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_4 = QLabel(SettingsDefault)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.tesseractFileSelector = FileSelector(SettingsDefault)
        self.tesseractFileSelector.setObjectName(u"tesseractFileSelector")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tesseractFileSelector.sizePolicy().hasHeightForWidth())
        self.tesseractFileSelector.setSizePolicy(sizePolicy3)
        self.tesseractFileSelector.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tesseractFileSelector)

        self.verticalSpacer = QSpacerItem(20, 500000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)


        self.retranslateUi(SettingsDefault)

        QMetaObject.connectSlotsByName(SettingsDefault)
    # setupUi

    def retranslateUi(self, SettingsDefault):
        self.label_2.setText(QCoreApplication.translate("SettingsDefault", u"devicesJsonFile", None))
        self.devicesJsonFileResetButton.setText(QCoreApplication.translate("SettingsDefault", u"devicesJsonPath.resetButton", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDefault", u"deviceUuid", None))
        self.deviceUuidResetButton.setText(QCoreApplication.translate("SettingsDefault", u"defaultDevice.resetButton", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDefault", u"tesseractFile", None))
        pass
    # retranslateUi

