# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databaseChecker.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)

from ui.implements.components.fileSelector import FileSelector


class Ui_DatabaseChecker(object):
    def setupUi(self, DatabaseChecker):
        if not DatabaseChecker.objectName():
            DatabaseChecker.setObjectName("DatabaseChecker")
        DatabaseChecker.resize(350, 250)
        DatabaseChecker.setWindowTitle("DatabaseChecker")
        self.formLayout = QFormLayout(DatabaseChecker)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label = QLabel(DatabaseChecker)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dbFileSelector = FileSelector(DatabaseChecker)
        self.dbFileSelector.setObjectName("dbFileSelector")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dbFileSelector)

        self.label_2 = QLabel(DatabaseChecker)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.dbVersionLabel = QLabel(DatabaseChecker)
        self.dbVersionLabel.setObjectName("dbVersionLabel")
        self.dbVersionLabel.setText("-")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dbVersionLabel)

        self.label_4 = QLabel(DatabaseChecker)
        self.label_4.setObjectName("label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(DatabaseChecker)
        self.label_5.setObjectName("label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.dbInitButton = QPushButton(DatabaseChecker)
        self.dbInitButton.setObjectName("dbInitButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dbInitButton)

        self.dbCheckConnLabel = QLabel(DatabaseChecker)
        self.dbCheckConnLabel.setObjectName("dbCheckConnLabel")
        self.dbCheckConnLabel.setText("...")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dbCheckConnLabel)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer)

        self.continueButton = QPushButton(DatabaseChecker)
        self.continueButton.setObjectName("continueButton")
        self.continueButton.setEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.continueButton)

        self.retranslateUi(DatabaseChecker)

        QMetaObject.connectSlotsByName(DatabaseChecker)

    # setupUi

    def retranslateUi(self, DatabaseChecker):
        self.label.setText(
            QCoreApplication.translate("DatabaseChecker", "dbPathLabel", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("DatabaseChecker", "dbVersionLabel", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("DatabaseChecker", "dbInitLabel", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("DatabaseChecker", "dbCheckConnLabel", None)
        )
        self.dbInitButton.setText(
            QCoreApplication.translate("DatabaseChecker", "dbInitButton", None)
        )
        self.continueButton.setText(
            QCoreApplication.translate("DatabaseChecker", "continueButton", None)
        )
        pass

    # retranslateUi
