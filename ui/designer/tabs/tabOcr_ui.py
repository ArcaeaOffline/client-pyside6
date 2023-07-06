# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcr.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGroupBox,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

from ui.implements.components import (DevicesComboBox, FileSelector)

class Ui_TabOcr(object):
    def setupUi(self, TabOcr):
        if not TabOcr.objectName():
            TabOcr.setObjectName(u"TabOcr")
        TabOcr.resize(632, 527)
        TabOcr.setWindowTitle(u"TabOcr")
        self.verticalLayout_3 = QVBoxLayout(TabOcr)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.openWizardButton = QPushButton(TabOcr)
        self.openWizardButton.setObjectName(u"openWizardButton")

        self.verticalLayout_3.addWidget(self.openWizardButton)

        self.groupBox = QGroupBox(TabOcr)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deviceFileSelector = FileSelector(self.groupBox)
        self.deviceFileSelector.setObjectName(u"deviceFileSelector")

        self.verticalLayout.addWidget(self.deviceFileSelector)

        self.deviceComboBox = DevicesComboBox(self.groupBox)
        self.deviceComboBox.setObjectName(u"deviceComboBox")

        self.verticalLayout.addWidget(self.deviceComboBox)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(TabOcr)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tesseractFileSelector = FileSelector(self.groupBox_4)
        self.tesseractFileSelector.setObjectName(u"tesseractFileSelector")

        self.verticalLayout_5.addWidget(self.tesseractFileSelector)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(TabOcr)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ocr_addImageButton = QPushButton(self.groupBox_3)
        self.ocr_addImageButton.setObjectName(u"ocr_addImageButton")

        self.verticalLayout_2.addWidget(self.ocr_addImageButton)

        self.ocr_removeSelectedButton = QPushButton(self.groupBox_3)
        self.ocr_removeSelectedButton.setObjectName(u"ocr_removeSelectedButton")
        self.ocr_removeSelectedButton.setEnabled(True)

        self.verticalLayout_2.addWidget(self.ocr_removeSelectedButton)

        self.ocr_removeAllButton = QPushButton(self.groupBox_3)
        self.ocr_removeAllButton.setObjectName(u"ocr_removeAllButton")
        self.ocr_removeAllButton.setEnabled(True)

        self.verticalLayout_2.addWidget(self.ocr_removeAllButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ocr_startButton = QPushButton(self.groupBox_3)
        self.ocr_startButton.setObjectName(u"ocr_startButton")

        self.verticalLayout_2.addWidget(self.ocr_startButton)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.tableView = QTableView(self.groupBox_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout.addWidget(self.tableView)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ocr_acceptSelectedButton = QPushButton(self.groupBox_5)
        self.ocr_acceptSelectedButton.setObjectName(u"ocr_acceptSelectedButton")
        self.ocr_acceptSelectedButton.setEnabled(True)

        self.verticalLayout_4.addWidget(self.ocr_acceptSelectedButton)

        self.ocr_acceptAllButton = QPushButton(self.groupBox_5)
        self.ocr_acceptAllButton.setObjectName(u"ocr_acceptAllButton")

        self.verticalLayout_4.addWidget(self.ocr_acceptAllButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.ocr_ignoreValidateCheckBox = QCheckBox(self.groupBox_5)
        self.ocr_ignoreValidateCheckBox.setObjectName(u"ocr_ignoreValidateCheckBox")

        self.verticalLayout_4.addWidget(self.ocr_ignoreValidateCheckBox)


        self.horizontalLayout.addWidget(self.groupBox_5)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(TabOcr)

        QMetaObject.connectSlotsByName(TabOcr)
    # setupUi

    def retranslateUi(self, TabOcr):
        self.openWizardButton.setText(QCoreApplication.translate("TabOcr", u"openWizardButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabOcr", u"deviceSelector.title", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabOcr", u"tesseractSelector.title", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabOcr", u"ocr.title", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabOcr", u"ocr.queue.title", None))
        self.ocr_addImageButton.setText(QCoreApplication.translate("TabOcr", u"ocr.queue.addImageButton", None))
        self.ocr_removeSelectedButton.setText(QCoreApplication.translate("TabOcr", u"ocr.queue.removeSelected", None))
        self.ocr_removeAllButton.setText(QCoreApplication.translate("TabOcr", u"ocr.queue.removeAll", None))
        self.ocr_startButton.setText(QCoreApplication.translate("TabOcr", u"ocr.queue.startOcrButton", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TabOcr", u"ocr.results", None))
        self.ocr_acceptSelectedButton.setText(QCoreApplication.translate("TabOcr", u"ocr.results.acceptSelectedButton", None))
        self.ocr_acceptAllButton.setText(QCoreApplication.translate("TabOcr", u"ocr.results.acceptAllButton", None))
        self.ocr_ignoreValidateCheckBox.setText(QCoreApplication.translate("TabOcr", u"ocr.results.ignoreValidate", None))
        pass
    # retranslateUi

