# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbTableViewer.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_DbTableViewer(object):
    def setupUi(self, DbTableViewer):
        if not DbTableViewer.objectName():
            DbTableViewer.setObjectName(u"DbTableViewer")
        DbTableViewer.resize(681, 575)
        DbTableViewer.setWindowTitle(u"DbTableViewer")
        self.gridLayout = QGridLayout(DbTableViewer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(DbTableViewer)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.action_removeSelectedButton = QPushButton(self.groupBox)
        self.action_removeSelectedButton.setObjectName(u"action_removeSelectedButton")

        self.verticalLayout.addWidget(self.action_removeSelectedButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.refreshButton = QPushButton(self.groupBox)
        self.refreshButton.setObjectName(u"refreshButton")

        self.verticalLayout.addWidget(self.refreshButton)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.tableView = QTableView(DbTableViewer)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(DbTableViewer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.sort_comboBox = QComboBox(self.groupBox_2)
        self.sort_comboBox.setObjectName(u"sort_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_comboBox.sizePolicy().hasHeightForWidth())
        self.sort_comboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.sort_comboBox)

        self.sort_descendingCheckBox = QCheckBox(self.groupBox_2)
        self.sort_descendingCheckBox.setObjectName(u"sort_descendingCheckBox")
        self.sort_descendingCheckBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.sort_descendingCheckBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 9)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)


        self.retranslateUi(DbTableViewer)

        QMetaObject.connectSlotsByName(DbTableViewer)
    # setupUi

    def retranslateUi(self, DbTableViewer):
        self.groupBox.setTitle(QCoreApplication.translate("DbTableViewer", u"actions", None))
        self.action_removeSelectedButton.setText(QCoreApplication.translate("DbTableViewer", u"actions.removeSelected", None))
        self.refreshButton.setText(QCoreApplication.translate("DbTableViewer", u"actions.refresh", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DbTableViewer", u"view", None))
        self.label.setText(QCoreApplication.translate("DbTableViewer", u"view.sort.label", None))
        self.sort_descendingCheckBox.setText(QCoreApplication.translate("DbTableViewer", u"view.sort.descendingCheckBox", None))
        self.label_2.setText(QCoreApplication.translate("DbTableViewer", u"view.filter.label", None))
        self.pushButton.setText(QCoreApplication.translate("DbTableViewer", u"view.filter.configureButton", None))
        pass
    # retranslateUi

