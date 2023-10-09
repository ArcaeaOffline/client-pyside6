# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabOcr_BuildPHashDatabase.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from ui.implements.components.fileSelector import FileSelector

class Ui_tabOcr_BuildPHashDatabase(object):
    def setupUi(self, tabOcr_BuildPHashDatabase):
        if not tabOcr_BuildPHashDatabase.objectName():
            tabOcr_BuildPHashDatabase.setObjectName(u"tabOcr_BuildPHashDatabase")
        tabOcr_BuildPHashDatabase.resize(632, 551)
        tabOcr_BuildPHashDatabase.setWindowTitle(u"tabOcr_BuildPHashDatabase")
        self.verticalLayout_3 = QVBoxLayout(tabOcr_BuildPHashDatabase)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(tabOcr_BuildPHashDatabase)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.songDirSelector = FileSelector(self.groupBox)
        self.songDirSelector.setObjectName(u"songDirSelector")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songDirSelector.sizePolicy().hasHeightForWidth())
        self.songDirSelector.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.songDirSelector)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.charIconDirSelector = FileSelector(self.groupBox)
        self.charIconDirSelector.setObjectName(u"charIconDirSelector")
        sizePolicy.setHeightForWidth(self.charIconDirSelector.sizePolicy().hasHeightForWidth())
        self.charIconDirSelector.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.charIconDirSelector)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(tabOcr_BuildPHashDatabase)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"hash_size")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.hashSizeSpinBox = QSpinBox(self.groupBox_2)
        self.hashSizeSpinBox.setObjectName(u"hashSizeSpinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hashSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.hashSizeSpinBox.setSizePolicy(sizePolicy1)
        self.hashSizeSpinBox.setMinimum(2)
        self.hashSizeSpinBox.setMaximum(64)
        self.hashSizeSpinBox.setValue(16)

        self.horizontalLayout_6.addWidget(self.hashSizeSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"highfreq_factor")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.highfreqFactorSpinBox = QSpinBox(self.groupBox_2)
        self.highfreqFactorSpinBox.setObjectName(u"highfreqFactorSpinBox")
        sizePolicy1.setHeightForWidth(self.highfreqFactorSpinBox.sizePolicy().hasHeightForWidth())
        self.highfreqFactorSpinBox.setSizePolicy(sizePolicy1)
        self.highfreqFactorSpinBox.setMaximum(32)
        self.highfreqFactorSpinBox.setValue(4)

        self.horizontalLayout_7.addWidget(self.highfreqFactorSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.optionsResetButton = QPushButton(self.groupBox_2)
        self.optionsResetButton.setObjectName(u"optionsResetButton")

        self.horizontalLayout_3.addWidget(self.optionsResetButton)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.progressBar = QProgressBar(tabOcr_BuildPHashDatabase)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat(u"%v/%m - %p%")

        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.buildButton = QPushButton(tabOcr_BuildPHashDatabase)
        self.buildButton.setObjectName(u"buildButton")

        self.horizontalLayout_5.addWidget(self.buildButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.retranslateUi(tabOcr_BuildPHashDatabase)

        QMetaObject.connectSlotsByName(tabOcr_BuildPHashDatabase)
    # setupUi

    def retranslateUi(self, tabOcr_BuildPHashDatabase):
        self.groupBox.setTitle(QCoreApplication.translate("tabOcr_BuildPHashDatabase", u"folders.title", None))
        self.label.setText(QCoreApplication.translate("tabOcr_BuildPHashDatabase", u"folders.songDir", None))
        self.label_2.setText(QCoreApplication.translate("tabOcr_BuildPHashDatabase", u"folders.charIconDir", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("tabOcr_BuildPHashDatabase", u"options.title", None))
        self.optionsResetButton.setText(QCoreApplication.translate("tabOcr_BuildPHashDatabase", u"resetButton", None))
        self.buildButton.setText(QCoreApplication.translate("tabOcr_BuildPHashDatabase", u"buildButton", None))
        pass
    # retranslateUi

