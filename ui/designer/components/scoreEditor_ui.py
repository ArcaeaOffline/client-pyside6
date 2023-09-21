# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoreEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

from ui.implements.components.focusSelectAllLineEdit import FocusSelectAllLineEdit

class Ui_ScoreEditor(object):
    def setupUi(self, ScoreEditor):
        if not ScoreEditor.objectName():
            ScoreEditor.setObjectName(u"ScoreEditor")
        ScoreEditor.resize(450, 350)
        ScoreEditor.setWindowTitle(u"ScoreEditor")
        self.gridLayout = QGridLayout(ScoreEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scoreLineEdit = FocusSelectAllLineEdit(ScoreEditor)
        self.scoreLineEdit.setObjectName(u"scoreLineEdit")
        self.scoreLineEdit.setInputMask(u"B9'999'999;_")

        self.gridLayout.addWidget(self.scoreLineEdit, 1, 1, 1, 1)

        self.validateLabel = QLabel(ScoreEditor)
        self.validateLabel.setObjectName(u"validateLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateLabel.sizePolicy().hasHeightForWidth())
        self.validateLabel.setSizePolicy(sizePolicy)
        self.validateLabel.setText(u"...")
        self.validateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.validateLabel, 13, 1, 1, 1)

        self.commentLineEdit = QLineEdit(ScoreEditor)
        self.commentLineEdit.setObjectName(u"commentLineEdit")
        self.commentLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.commentLineEdit, 11, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.commitButton = QPushButton(ScoreEditor)
        self.commitButton.setObjectName(u"commitButton")

        self.gridLayout.addWidget(self.commitButton, 13, 2, 1, 1)

        self.clearTypeComboBox = QComboBox(ScoreEditor)
        self.clearTypeComboBox.setObjectName(u"clearTypeComboBox")
        self.clearTypeComboBox.setEnabled(False)
        self.clearTypeComboBox.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.clearTypeComboBox, 10, 1, 1, 1)

        self.farSpinBox = QSpinBox(ScoreEditor)
        self.farSpinBox.setObjectName(u"farSpinBox")
        self.farSpinBox.setMinimumSize(QSize(100, 0))
        self.farSpinBox.setMinimum(0)
        self.farSpinBox.setMaximum(0)

        self.gridLayout.addWidget(self.farSpinBox, 3, 1, 1, 1)

        self.label = QLabel(ScoreEditor)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.commentNoneCheckBox = QCheckBox(ScoreEditor)
        self.commentNoneCheckBox.setObjectName(u"commentNoneCheckBox")
        self.commentNoneCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.commentNoneCheckBox, 11, 2, 1, 1)

        self.farNoneCheckBox = QCheckBox(ScoreEditor)
        self.farNoneCheckBox.setObjectName(u"farNoneCheckBox")

        self.gridLayout.addWidget(self.farNoneCheckBox, 3, 2, 1, 1)

        self.label_8 = QLabel(ScoreEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setText(u"Clear Type")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)

        self.label_3 = QLabel(ScoreEditor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"FAR")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lostSpinBox = QSpinBox(ScoreEditor)
        self.lostSpinBox.setObjectName(u"lostSpinBox")
        self.lostSpinBox.setMinimumSize(QSize(100, 0))
        self.lostSpinBox.setMinimum(0)
        self.lostSpinBox.setMaximum(0)

        self.gridLayout.addWidget(self.lostSpinBox, 4, 1, 1, 1)

        self.idLabel = QLabel(ScoreEditor)
        self.idLabel.setObjectName(u"idLabel")

        self.gridLayout.addWidget(self.idLabel, 0, 1, 1, 1)

        self.label_5 = QLabel(ScoreEditor)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_7 = QLabel(ScoreEditor)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setText(u"Modifier")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)

        self.maxRecallNoneCheckBox = QCheckBox(ScoreEditor)
        self.maxRecallNoneCheckBox.setObjectName(u"maxRecallNoneCheckBox")
        self.maxRecallNoneCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.maxRecallNoneCheckBox, 8, 2, 1, 1)

        self.clearTypeNoneCheckBox = QCheckBox(ScoreEditor)
        self.clearTypeNoneCheckBox.setObjectName(u"clearTypeNoneCheckBox")
        self.clearTypeNoneCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.clearTypeNoneCheckBox, 10, 2, 1, 1)

        self.label_10 = QLabel(ScoreEditor)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setText(u"ID")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_2 = QLabel(ScoreEditor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"PURE")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(ScoreEditor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"LOST")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.modifierNoneCheckBox = QCheckBox(ScoreEditor)
        self.modifierNoneCheckBox.setObjectName(u"modifierNoneCheckBox")
        self.modifierNoneCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.modifierNoneCheckBox, 9, 2, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(ScoreEditor)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy1)
        self.dateTimeEdit.setDisplayFormat(u"yyyy/MM/dd HH:mm:ss")
        self.dateTimeEdit.setCalendarPopup(False)

        self.gridLayout.addWidget(self.dateTimeEdit, 5, 1, 1, 1)

        self.modifierComboBox = QComboBox(ScoreEditor)
        self.modifierComboBox.setObjectName(u"modifierComboBox")
        self.modifierComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.modifierComboBox, 9, 1, 1, 1)

        self.dateNoneCheckBox = QCheckBox(ScoreEditor)
        self.dateNoneCheckBox.setObjectName(u"dateNoneCheckBox")

        self.gridLayout.addWidget(self.dateNoneCheckBox, 5, 2, 1, 1)

        self.pureNoneCheckBox = QCheckBox(ScoreEditor)
        self.pureNoneCheckBox.setObjectName(u"pureNoneCheckBox")

        self.gridLayout.addWidget(self.pureNoneCheckBox, 2, 2, 1, 1)

        self.pureSpinBox = QSpinBox(ScoreEditor)
        self.pureSpinBox.setObjectName(u"pureSpinBox")
        self.pureSpinBox.setMinimumSize(QSize(100, 0))
        self.pureSpinBox.setMinimum(0)
        self.pureSpinBox.setMaximum(0)

        self.gridLayout.addWidget(self.pureSpinBox, 2, 1, 1, 1)

        self.lostNoneCheckBox = QCheckBox(ScoreEditor)
        self.lostNoneCheckBox.setObjectName(u"lostNoneCheckBox")

        self.gridLayout.addWidget(self.lostNoneCheckBox, 4, 2, 1, 1)

        self.warnIfIncompleteCheckBox = QCheckBox(ScoreEditor)
        self.warnIfIncompleteCheckBox.setObjectName(u"warnIfIncompleteCheckBox")

        self.gridLayout.addWidget(self.warnIfIncompleteCheckBox, 13, 0, 1, 1)

        self.maxRecallSpinBox = QSpinBox(ScoreEditor)
        self.maxRecallSpinBox.setObjectName(u"maxRecallSpinBox")
        self.maxRecallSpinBox.setEnabled(False)
        self.maxRecallSpinBox.setMinimumSize(QSize(100, 0))
        self.maxRecallSpinBox.setMinimum(0)
        self.maxRecallSpinBox.setMaximum(0)
        self.maxRecallSpinBox.setValue(0)

        self.gridLayout.addWidget(self.maxRecallSpinBox, 8, 1, 1, 1)

        self.label_9 = QLabel(ScoreEditor)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.label_6 = QLabel(ScoreEditor)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(u"MAX RECALL")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_11 = QLabel(ScoreEditor)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)

        self.previewLabel = QLabel(ScoreEditor)
        self.previewLabel.setObjectName(u"previewLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy2)
        self.previewLabel.setStyleSheet(u"QLabel { color: gray }")
        self.previewLabel.setText(u"None")
        self.previewLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.previewLabel, 12, 1, 1, 1)

        QWidget.setTabOrder(self.scoreLineEdit, self.pureSpinBox)
        QWidget.setTabOrder(self.pureSpinBox, self.pureNoneCheckBox)
        QWidget.setTabOrder(self.pureNoneCheckBox, self.farSpinBox)
        QWidget.setTabOrder(self.farSpinBox, self.farNoneCheckBox)
        QWidget.setTabOrder(self.farNoneCheckBox, self.lostSpinBox)
        QWidget.setTabOrder(self.lostSpinBox, self.lostNoneCheckBox)
        QWidget.setTabOrder(self.lostNoneCheckBox, self.dateTimeEdit)
        QWidget.setTabOrder(self.dateTimeEdit, self.dateNoneCheckBox)
        QWidget.setTabOrder(self.dateNoneCheckBox, self.maxRecallSpinBox)
        QWidget.setTabOrder(self.maxRecallSpinBox, self.maxRecallNoneCheckBox)
        QWidget.setTabOrder(self.maxRecallNoneCheckBox, self.modifierComboBox)
        QWidget.setTabOrder(self.modifierComboBox, self.modifierNoneCheckBox)
        QWidget.setTabOrder(self.modifierNoneCheckBox, self.clearTypeComboBox)
        QWidget.setTabOrder(self.clearTypeComboBox, self.clearTypeNoneCheckBox)
        QWidget.setTabOrder(self.clearTypeNoneCheckBox, self.commentLineEdit)
        QWidget.setTabOrder(self.commentLineEdit, self.commentNoneCheckBox)
        QWidget.setTabOrder(self.commentNoneCheckBox, self.commitButton)

        self.retranslateUi(ScoreEditor)
        self.pureNoneCheckBox.toggled.connect(self.pureSpinBox.setDisabled)
        self.clearTypeNoneCheckBox.toggled.connect(self.clearTypeComboBox.setDisabled)
        self.modifierNoneCheckBox.toggled.connect(self.modifierComboBox.setDisabled)
        self.maxRecallNoneCheckBox.toggled.connect(self.maxRecallSpinBox.setDisabled)
        self.dateNoneCheckBox.toggled.connect(self.dateTimeEdit.setDisabled)
        self.lostNoneCheckBox.toggled.connect(self.lostSpinBox.setDisabled)
        self.farNoneCheckBox.toggled.connect(self.farSpinBox.setDisabled)
        self.commentNoneCheckBox.toggled.connect(self.commentLineEdit.setDisabled)

        QMetaObject.connectSlotsByName(ScoreEditor)
    # setupUi

    def retranslateUi(self, ScoreEditor):
        self.commitButton.setText(QCoreApplication.translate("ScoreEditor", u"commitButton", None))
        self.label.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.score", None))
        self.commentNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.farNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.idLabel.setText(QCoreApplication.translate("ScoreEditor", u"idAutoInsert", None))
        self.label_5.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.date", None))
        self.maxRecallNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.clearTypeNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.modifierNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.dateNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.pureNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.lostNoneCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"setNone", None))
        self.warnIfIncompleteCheckBox.setText(QCoreApplication.translate("ScoreEditor", u"warnIfIncomplete", None))
        self.label_9.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.comment", None))
        self.label_11.setText(QCoreApplication.translate("ScoreEditor", u"formLabel.preview", None))
        pass
    # retranslateUi

