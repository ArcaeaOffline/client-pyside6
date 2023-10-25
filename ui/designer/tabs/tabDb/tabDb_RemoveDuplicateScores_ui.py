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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTreeView,
    QVBoxLayout, QWidget)

class Ui_TabDb_RemoveDuplicateScores(object):
    def setupUi(self, TabDb_RemoveDuplicateScores):
        if not TabDb_RemoveDuplicateScores.objectName():
            TabDb_RemoveDuplicateScores.setObjectName(u"TabDb_RemoveDuplicateScores")
        TabDb_RemoveDuplicateScores.resize(600, 500)
        TabDb_RemoveDuplicateScores.setWindowTitle(u"TabDb_RemoveDuplicateScores")
        self.verticalLayout_2 = QVBoxLayout(TabDb_RemoveDuplicateScores)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(TabDb_RemoveDuplicateScores)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scan_option_scoreCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_scoreCheckBox.setObjectName(u"scan_option_scoreCheckBox")

        self.horizontalLayout_2.addWidget(self.scan_option_scoreCheckBox)

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

        self.scan_option_maxRecallCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_maxRecallCheckBox.setObjectName(u"scan_option_maxRecallCheckBox")
        self.scan_option_maxRecallCheckBox.setText(u"MAX RECALL")

        self.horizontalLayout_2.addWidget(self.scan_option_maxRecallCheckBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scan_option_dateCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_dateCheckBox.setObjectName(u"scan_option_dateCheckBox")

        self.horizontalLayout_3.addWidget(self.scan_option_dateCheckBox)

        self.scan_option_modifierCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_modifierCheckBox.setObjectName(u"scan_option_modifierCheckBox")

        self.horizontalLayout_3.addWidget(self.scan_option_modifierCheckBox)

        self.scan_option_clearTypeCheckBox = QCheckBox(self.groupBox_2)
        self.scan_option_clearTypeCheckBox.setObjectName(u"scan_option_clearTypeCheckBox")

        self.horizontalLayout_3.addWidget(self.scan_option_clearTypeCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.scan_scanButton = QPushButton(self.groupBox_2)
        self.scan_scanButton.setObjectName(u"scan_scanButton")

        self.verticalLayout.addWidget(self.scan_scanButton)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(TabDb_RemoveDuplicateScores)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeView.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.treeView)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(TabDb_RemoveDuplicateScores)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.quickSelect_comboBox = QComboBox(self.groupBox)
        self.quickSelect_comboBox.setObjectName(u"quickSelect_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickSelect_comboBox.sizePolicy().hasHeightForWidth())
        self.quickSelect_comboBox.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.quickSelect_comboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.quickSelect_selectButton = QPushButton(self.groupBox)
        self.quickSelect_selectButton.setObjectName(u"quickSelect_selectButton")
        sizePolicy.setHeightForWidth(self.quickSelect_selectButton.sizePolicy().hasHeightForWidth())
        self.quickSelect_selectButton.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.quickSelect_selectButton)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(TabDb_RemoveDuplicateScores)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.deselectAllButton = QPushButton(self.groupBox_3)
        self.deselectAllButton.setObjectName(u"deselectAllButton")

        self.verticalLayout_5.addWidget(self.deselectAllButton)

        self.reverseSelectionButton = QPushButton(self.groupBox_3)
        self.reverseSelectionButton.setObjectName(u"reverseSelectionButton")

        self.verticalLayout_5.addWidget(self.reverseSelectionButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.collapseAllButton = QPushButton(self.groupBox_3)
        self.collapseAllButton.setObjectName(u"collapseAllButton")

        self.verticalLayout_5.addWidget(self.collapseAllButton)

        self.expandAllButton = QPushButton(self.groupBox_3)
        self.expandAllButton.setObjectName(u"expandAllButton")

        self.verticalLayout_5.addWidget(self.expandAllButton)

        self.resetModelButton = QPushButton(self.groupBox_3)
        self.resetModelButton.setObjectName(u"resetModelButton")

        self.verticalLayout_5.addWidget(self.resetModelButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.deleteSelectionButton = QPushButton(self.groupBox_3)
        self.deleteSelectionButton.setObjectName(u"deleteSelectionButton")
        font = QFont()
        font.setBold(True)
        self.deleteSelectionButton.setFont(font)
        self.deleteSelectionButton.setStyleSheet(u"QPushButton { color: red };")

        self.verticalLayout_5.addWidget(self.deleteSelectionButton)


        self.verticalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.scan_option_scoreCheckBox, self.scan_option_pureCheckBox)
        QWidget.setTabOrder(self.scan_option_pureCheckBox, self.scan_option_farCheckBox)
        QWidget.setTabOrder(self.scan_option_farCheckBox, self.scan_option_lostCheckBox)
        QWidget.setTabOrder(self.scan_option_lostCheckBox, self.scan_option_maxRecallCheckBox)
        QWidget.setTabOrder(self.scan_option_maxRecallCheckBox, self.scan_option_dateCheckBox)
        QWidget.setTabOrder(self.scan_option_dateCheckBox, self.scan_option_modifierCheckBox)
        QWidget.setTabOrder(self.scan_option_modifierCheckBox, self.scan_option_clearTypeCheckBox)
        QWidget.setTabOrder(self.scan_option_clearTypeCheckBox, self.scan_scanButton)
        QWidget.setTabOrder(self.scan_scanButton, self.treeView)
        QWidget.setTabOrder(self.treeView, self.quickSelect_comboBox)
        QWidget.setTabOrder(self.quickSelect_comboBox, self.quickSelect_selectButton)
        QWidget.setTabOrder(self.quickSelect_selectButton, self.deselectAllButton)
        QWidget.setTabOrder(self.deselectAllButton, self.reverseSelectionButton)
        QWidget.setTabOrder(self.reverseSelectionButton, self.collapseAllButton)
        QWidget.setTabOrder(self.collapseAllButton, self.expandAllButton)
        QWidget.setTabOrder(self.expandAllButton, self.resetModelButton)
        QWidget.setTabOrder(self.resetModelButton, self.deleteSelectionButton)

        self.retranslateUi(TabDb_RemoveDuplicateScores)

        QMetaObject.connectSlotsByName(TabDb_RemoveDuplicateScores)
    # setupUi

    def retranslateUi(self, TabDb_RemoveDuplicateScores):
        self.groupBox_2.setTitle(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.title", None))
        self.scan_option_scoreCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.score", None))
        self.scan_option_dateCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.date", None))
        self.scan_option_modifierCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.modifier", None))
        self.scan_option_clearTypeCheckBox.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.option.clearType", None))
        self.scan_scanButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"scan.scanButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"quickSelect.title", None))
        self.label.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"quickSelect.description", None))
        self.quickSelect_selectButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"quickSelect.selectButton", None))
        self.groupBox_3.setTitle("")
        self.deselectAllButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"deselectAllButton", None))
        self.reverseSelectionButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"reverseSelectionButton", None))
        self.collapseAllButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"collapseAllButton", None))
        self.expandAllButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"expandAllButton", None))
        self.resetModelButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"resetModelButton", None))
        self.deleteSelectionButton.setText(QCoreApplication.translate("TabDb_RemoveDuplicateScores", u"deleteSelectionButton", None))
        pass
    # retranslateUi

