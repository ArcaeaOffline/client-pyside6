# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabDb_RemoveDuplicateScores.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTreeView, QVBoxLayout, QWidget)

class Ui_TabDb_RemoveDuplicateScores(object):
    def setupUi(self, TabDb_RemoveDuplicateScores):
        if not TabDb_RemoveDuplicateScores.objectName():
            TabDb_RemoveDuplicateScores.setObjectName(u"TabDb_RemoveDuplicateScores")
        TabDb_RemoveDuplicateScores.resize(700, 500)
        TabDb_RemoveDuplicateScores.setWindowTitle(u"TabDb_RemoveDuplicateScores")
        self.gridLayout = QGridLayout(TabDb_RemoveDuplicateScores)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(TabDb_RemoveDuplicateScores)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scan_option_scoreCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_scoreCheckBox.setObjectName(u"scan_option_scoreCheckBox")

        self.verticalLayout_2.addWidget(self.scan_option_scoreCheckBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scan_option_pureCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_pureCheckBox.setObjectName(u"scan_option_pureCheckBox")
        self.scan_option_pureCheckBox.setText(u"PURE")

        self.horizontalLayout_2.addWidget(self.scan_option_pureCheckBox)

        self.scan_option_farCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_farCheckBox.setObjectName(u"scan_option_farCheckBox")
        self.scan_option_farCheckBox.setText(u"FAR")

        self.horizontalLayout_2.addWidget(self.scan_option_farCheckBox)

        self.scan_option_lostCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_lostCheckBox.setObjectName(u"scan_option_lostCheckBox")
        self.scan_option_lostCheckBox.setText(u"LOST")

        self.horizontalLayout_2.addWidget(self.scan_option_lostCheckBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.scan_option_maxRecallCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_maxRecallCheckBox.setObjectName(u"scan_option_maxRecallCheckBox")
        self.scan_option_maxRecallCheckBox.setText(u"MAX RECALL")

        self.verticalLayout_2.addWidget(self.scan_option_maxRecallCheckBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scan_option_clearTypeCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_clearTypeCheckBox.setObjectName(u"scan_option_clearTypeCheckBox")

        self.horizontalLayout_3.addWidget(self.scan_option_clearTypeCheckBox)

        self.scan_option_modifierCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_modifierCheckBox.setObjectName(u"scan_option_modifierCheckBox")

        self.horizontalLayout_3.addWidget(self.scan_option_modifierCheckBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.scan_scanButton = QPushButton(self.groupBox_2)
        self.scan_scanButton.setObjectName(u"scan_scanButton")

        self.verticalLayout_2.addWidget(self.scan_scanButton)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(TabDb_RemoveDuplicateScores)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.quickSelect_timeComboBox = QComboBox(self.groupBox)
        self.quickSelect_timeComboBox.setObjectName(u"quickSelect_timeComboBox")

        self.verticalLayout_3.addWidget(self.quickSelect_timeComboBox)

        self.quickSelect_ColumnComboBox = QComboBox(self.groupBox)
        self.quickSelect_ColumnComboBox.setObjectName(u"quickSelect_ColumnComboBox")

        self.verticalLayout_3.addWidget(self.quickSelect_ColumnComboBox)

        self.verticalSpacer = QSpacerItem(20, 91, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.quickSelect_selectButton = QPushButton(self.groupBox)
        self.quickSelect_selectButton.setObjectName(u"quickSelect_selectButton")

        self.verticalLayout_3.addWidget(self.quickSelect_selectButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.collapseAllButton = QPushButton(TabDb_RemoveDuplicateScores)
        self.collapseAllButton.setObjectName(u"collapseAllButton")

        self.horizontalLayout_4.addWidget(self.collapseAllButton)

        self.expandAllButton = QPushButton(TabDb_RemoveDuplicateScores)
        self.expandAllButton.setObjectName(u"expandAllButton")

        self.horizontalLayout_4.addWidget(self.expandAllButton)

        self.resetModelButton = QPushButton(TabDb_RemoveDuplicateScores)
        self.resetModelButton.setObjectName(u"resetModelButton")

        self.horizontalLayout_4.addWidget(self.resetModelButton)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.treeView = QTreeView(TabDb_RemoveDuplicateScores)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)

        self.deleteSelectedButton = QPushButton(TabDb_RemoveDuplicateScores)
        self.deleteSelectedButton.setObjectName(u"deleteSelectedButton")
        font = QFont()
        font.setBold(True)
        self.deleteSelectedButton.setFont(font)
        self.deleteSelectedButton.setStyleSheet(u"QPushButton { color: red };")

        self.gridLayout.addWidget(self.deleteSelectedButton, 1, 1, 1, 1)


        self.retranslateUi(TabDb_RemoveDuplicateScores)

        QMetaObject.connectSlotsByName(TabDb_RemoveDuplicateScores)
    # setupUi

    def retranslateUi(self, TabDb_RemoveDuplicateScores):
        self.groupBox_2.setTitle(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.title", None))
        self.scan_option_scoreCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.score", None))
        self.scan_option_clearTypeCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.clearType", None))
        self.scan_option_modifierCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.modifier", None))
        self.scan_scanButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.scanButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"quickSelect.title", None))
        self.label.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"quickSelect.keepSingleLabel", None))
        self.quickSelect_selectButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"quickSelect.selectButton", None))
        self.collapseAllButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"collapseAllButton", None))
        self.expandAllButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"expandAllButton", None))
        self.resetModelButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"resetModelButton", None))
        self.deleteSelectedButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"deleteSelectedButton", None))
        pass
    # retranslateUi

