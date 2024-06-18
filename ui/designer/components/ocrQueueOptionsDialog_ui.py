# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ocrQueueOptionsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OcrQueueOptionsDialog(object):
    def setupUi(self, OcrQueueOptionsDialog):
        if not OcrQueueOptionsDialog.objectName():
            OcrQueueOptionsDialog.setObjectName(u"OcrQueueOptionsDialog")
        OcrQueueOptionsDialog.resize(331, 157)
        self.verticalLayout = QVBoxLayout(OcrQueueOptionsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(OcrQueueOptionsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.iccUseQtRadioButton = QRadioButton(self.groupBox)
        self.iccUseQtRadioButton.setObjectName(u"iccUseQtRadioButton")

        self.verticalLayout_2.addWidget(self.iccUseQtRadioButton)

        self.iccUsePILRadioButton = QRadioButton(self.groupBox)
        self.iccUsePILRadioButton.setObjectName(u"iccUsePILRadioButton")
        self.iccUsePILRadioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.iccUsePILRadioButton)

        self.iccTryFixRadioButton = QRadioButton(self.groupBox)
        self.iccTryFixRadioButton.setObjectName(u"iccTryFixRadioButton")

        self.verticalLayout_2.addWidget(self.iccTryFixRadioButton)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(OcrQueueOptionsDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dateReadFromExifCheckbox = QCheckBox(self.groupBox_2)
        self.dateReadFromExifCheckbox.setObjectName(u"dateReadFromExifCheckbox")
        self.dateReadFromExifCheckbox.setEnabled(False)
        self.dateReadFromExifCheckbox.setChecked(True)

        self.verticalLayout_3.addWidget(self.dateReadFromExifCheckbox)

        self.dateUseCreationDateRadioButton = QRadioButton(self.groupBox_2)
        self.dateUseCreationDateRadioButton.setObjectName(u"dateUseCreationDateRadioButton")
        self.dateUseCreationDateRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.dateUseCreationDateRadioButton)

        self.dateUseModifyDateRadioButton = QRadioButton(self.groupBox_2)
        self.dateUseModifyDateRadioButton.setObjectName(u"dateUseModifyDateRadioButton")

        self.verticalLayout_3.addWidget(self.dateUseModifyDateRadioButton)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(OcrQueueOptionsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(OcrQueueOptionsDialog)
        self.buttonBox.accepted.connect(OcrQueueOptionsDialog.accept)
        self.buttonBox.rejected.connect(OcrQueueOptionsDialog.reject)

        QMetaObject.connectSlotsByName(OcrQueueOptionsDialog)
    # setupUi

    def retranslateUi(self, OcrQueueOptionsDialog):
        OcrQueueOptionsDialog.setWindowTitle(QCoreApplication.translate("OcrQueueOptionsDialog", u"OCR Options", None))
        self.groupBox.setTitle(QCoreApplication.translate("OcrQueueOptionsDialog", u"iccOptionsGroupBox", None))
        self.iccUseQtRadioButton.setText(QCoreApplication.translate("OcrQueueOptionsDialog", u"icc.useQt", None))
        self.iccUsePILRadioButton.setText(QCoreApplication.translate("OcrQueueOptionsDialog", u"icc.usePIL", None))
        self.iccTryFixRadioButton.setText(QCoreApplication.translate("OcrQueueOptionsDialog", u"icc.tryFix", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("OcrQueueOptionsDialog", u"dateOptionsGroupBox", None))
        self.dateReadFromExifCheckbox.setText(QCoreApplication.translate("OcrQueueOptionsDialog", u"date.readFromExif", None))
        self.dateUseCreationDateRadioButton.setText(QCoreApplication.translate("OcrQueueOptionsDialog", u"date.useCreationDate", None))
        self.dateUseModifyDateRadioButton.setText(QCoreApplication.translate("OcrQueueOptionsDialog", u"date.useModifyDate", None))
    # retranslateUi
