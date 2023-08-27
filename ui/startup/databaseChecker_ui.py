# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databaseChecker.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

from ui.implements.components.fileSelector import FileSelector

class Ui_DatabaseChecker(object):
    def setupUi(self, DatabaseChecker):
        if not DatabaseChecker.objectName():
            DatabaseChecker.setObjectName(u"DatabaseChecker")
        DatabaseChecker.resize(350, 250)
        DatabaseChecker.setWindowTitle(u"DatabaseChecker")
        self.formLayout = QFormLayout(DatabaseChecker)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(DatabaseChecker)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dbDirSelector = FileSelector(DatabaseChecker)
        self.dbDirSelector.setObjectName(u"dbDirSelector")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dbDirSelector)

        self.label_3 = QLabel(DatabaseChecker)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.dbFilenameLineEdit = QLineEdit(DatabaseChecker)
        self.dbFilenameLineEdit.setObjectName(u"dbFilenameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dbFilenameLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.confirmDbPathButton = QPushButton(DatabaseChecker)
        self.confirmDbPathButton.setObjectName(u"confirmDbPathButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmDbPathButton.sizePolicy().hasHeightForWidth())
        self.confirmDbPathButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.confirmDbPathButton)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.dbVersionLabel = QLabel(DatabaseChecker)
        self.dbVersionLabel.setObjectName(u"dbVersionLabel")
        self.dbVersionLabel.setText(u"-")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dbVersionLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.FieldRole, self.verticalSpacer)

        self.label_5 = QLabel(DatabaseChecker)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.dbCheckConnLabel = QLabel(DatabaseChecker)
        self.dbCheckConnLabel.setObjectName(u"dbCheckConnLabel")
        self.dbCheckConnLabel.setText(u"...")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.dbCheckConnLabel)

        self.continueButton = QPushButton(DatabaseChecker)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setEnabled(False)

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.continueButton)

        self.label_2 = QLabel(DatabaseChecker)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.line = QFrame(DatabaseChecker)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.line)


        self.retranslateUi(DatabaseChecker)

        QMetaObject.connectSlotsByName(DatabaseChecker)
    # setupUi

    def retranslateUi(self, DatabaseChecker):
        self.label.setText(QCoreApplication.translate("DatabaseChecker", u"dbPathLabel", None))
        self.label_3.setText(QCoreApplication.translate("DatabaseChecker", u"dbFilenameLabel", None))
        self.confirmDbPathButton.setText(QCoreApplication.translate("DatabaseChecker", u"confirmDbPathButton", None))
        self.label_5.setText(QCoreApplication.translate("DatabaseChecker", u"dbCheckConnLabel", None))
        self.continueButton.setText(QCoreApplication.translate("DatabaseChecker", u"continueButton", None))
        self.label_2.setText(QCoreApplication.translate("DatabaseChecker", u"dbVersionLabel", None))
        pass
    # retranslateUi

