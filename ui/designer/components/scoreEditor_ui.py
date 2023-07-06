# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoreEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFormLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

from ui.implements.components.focusSelectAllLineEdit import FocusSelectAllLineEdit

class Ui_ScoreEditor(object):
    def setupUi(self, ScoreEditor):
        if not ScoreEditor.objectName():
            ScoreEditor.setObjectName(u"ScoreEditor")
        ScoreEditor.resize(365, 253)
        ScoreEditor.setWindowTitle(u"ScoreEditor")
        self.formLayout = QFormLayout(ScoreEditor)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(ScoreEditor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.scoreLineEdit = FocusSelectAllLineEdit(ScoreEditor)
        self.scoreLineEdit.setObjectName(u"scoreLineEdit")
        self.scoreLineEdit.setInputMask(u"B9'999'999;_")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.scoreLineEdit)

        self.label_2 = QLabel(ScoreEditor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"PURE")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.pureSpinBox = QSpinBox(ScoreEditor)
        self.pureSpinBox.setObjectName(u"pureSpinBox")
        self.pureSpinBox.setMinimumSize(QSize(100, 0))
        self.pureSpinBox.setMaximum(0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pureSpinBox)

        self.label_3 = QLabel(ScoreEditor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"FAR")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.farSpinBox = QSpinBox(ScoreEditor)
        self.farSpinBox.setObjectName(u"farSpinBox")
        self.farSpinBox.setMinimumSize(QSize(100, 0))
        self.farSpinBox.setMaximum(0)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.farSpinBox)

        self.label_4 = QLabel(ScoreEditor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"LOST")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lostSpinBox = QSpinBox(ScoreEditor)
        self.lostSpinBox.setObjectName(u"lostSpinBox")
        self.lostSpinBox.setMinimumSize(QSize(100, 0))
        self.lostSpinBox.setMaximum(0)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lostSpinBox)

        self.label_5 = QLabel(ScoreEditor)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.dateTimeEdit = QDateTimeEdit(ScoreEditor)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setDateTime(QDateTime(QDate(2017, 1, 22), QTime(0, 0, 0)))
        self.dateTimeEdit.setMinimumDate(QDate(2017, 1, 22))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dateTimeEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_6 = QLabel(ScoreEditor)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(u"MAX RECALL")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.maxRecallSpinBox = QSpinBox(ScoreEditor)
        self.maxRecallSpinBox.setObjectName(u"maxRecallSpinBox")
        self.maxRecallSpinBox.setMinimumSize(QSize(100, 0))
        self.maxRecallSpinBox.setMinimum(-1)
        self.maxRecallSpinBox.setMaximum(0)
        self.maxRecallSpinBox.setValue(-1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.maxRecallSpinBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.validateLabel = QLabel(ScoreEditor)
        self.validateLabel.setObjectName(u"validateLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.validateLabel.sizePolicy().hasHeightForWidth())
        self.validateLabel.setSizePolicy(sizePolicy1)
        self.validateLabel.setText(u"...")
        self.validateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.validateLabel)

        self.commitButton = QPushButton(ScoreEditor)
        self.commitButton.setObjectName(u"commitButton")

        self.horizontalLayout.addWidget(self.commitButton)


        self.formLayout.setLayout(8, QFormLayout.SpanningRole, self.horizontalLayout)

        self.label_8 = QLabel(ScoreEditor)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.clearTypeComboBox = QComboBox(ScoreEditor)
        self.clearTypeComboBox.setObjectName(u"clearTypeComboBox")
        self.clearTypeComboBox.setEnabled(False)
        self.clearTypeComboBox.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.clearTypeComboBox)


        self.retranslateUi(ScoreEditor)

        QMetaObject.connectSlotsByName(ScoreEditor)
    # setupUi

    def retranslateUi(self, ScoreEditor):
        self.label.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.score", None))
        self.label_5.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.time", None))
        self.commitButton.setText(QCoreApplication.translate("ScoreEditor", u"commitButton", None))
        self.label_8.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.clearType", None))
        pass
    # retranslateUi

