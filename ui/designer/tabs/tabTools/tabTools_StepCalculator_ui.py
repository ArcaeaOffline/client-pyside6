# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabTools_StepCalculator.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_TabTools_StepCalculator(object):
    def setupUi(self, TabTools_StepCalculator):
        if not TabTools_StepCalculator.objectName():
            TabTools_StepCalculator.setObjectName(u"TabTools_StepCalculator")
        TabTools_StepCalculator.resize(615, 549)
        TabTools_StepCalculator.setWindowTitle(u"TabTools_StepCalculator")
        self.verticalLayout_3 = QVBoxLayout(TabTools_StepCalculator)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(TabTools_StepCalculator)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.partnerStepValueSpinBox = QDoubleSpinBox(self.widget_3)
        self.partnerStepValueSpinBox.setObjectName(u"partnerStepValueSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partnerStepValueSpinBox.sizePolicy().hasHeightForWidth())
        self.partnerStepValueSpinBox.setSizePolicy(sizePolicy)
        self.partnerStepValueSpinBox.setMaximum(1000.000000000000000)
        self.partnerStepValueSpinBox.setSingleStep(1.000000000000000)
        self.partnerStepValueSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)

        self.gridLayout.addWidget(self.partnerStepValueSpinBox, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.mapTypeWidget = QWidget(TabTools_StepCalculator)
        self.mapTypeWidget.setObjectName(u"mapTypeWidget")
        self.horizontalLayout = QHBoxLayout(self.mapTypeWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mapTypeSelectorWidget = QWidget(self.mapTypeWidget)
        self.mapTypeSelectorWidget.setObjectName(u"mapTypeSelectorWidget")
        self.gridLayout_2 = QGridLayout(self.mapTypeSelectorWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mapTypeLegacyPlayRadioButton = QPushButton(self.mapTypeSelectorWidget)
        self.mapTypeLegacyPlayRadioButton.setObjectName(u"mapTypeLegacyPlayRadioButton")
        self.mapTypeLegacyPlayRadioButton.setStyleSheet(u"QPushButton{background-color: transparent}")
        self.mapTypeLegacyPlayRadioButton.setCheckable(True)
        self.mapTypeLegacyPlayRadioButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.mapTypeLegacyPlayRadioButton, 0, 0, 1, 1)

        self.mapTypePlayRadioButton = QPushButton(self.mapTypeSelectorWidget)
        self.mapTypePlayRadioButton.setObjectName(u"mapTypePlayRadioButton")
        self.mapTypePlayRadioButton.setStyleSheet(u"QPushButton{background-color: transparent}")
        self.mapTypePlayRadioButton.setCheckable(True)
        self.mapTypePlayRadioButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.mapTypePlayRadioButton, 1, 0, 1, 1)

        self.mapTypeLegacyPlayPlusRadioButton = QPushButton(self.mapTypeSelectorWidget)
        self.mapTypeLegacyPlayPlusRadioButton.setObjectName(u"mapTypeLegacyPlayPlusRadioButton")
        self.mapTypeLegacyPlayPlusRadioButton.setStyleSheet(u"QPushButton{background-color: transparent}")
        self.mapTypeLegacyPlayPlusRadioButton.setCheckable(True)
        self.mapTypeLegacyPlayPlusRadioButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.mapTypeLegacyPlayPlusRadioButton, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.mapTypeSelectorWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setStyleSheet(u"QPushButton{background-color: transparent}")
        self.pushButton_4.setText(u"Beyond placeholder")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.mapTypeSelectorWidget)

        self.stackedWidget = QStackedWidget(self.mapTypeWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.legacyPlay = QWidget()
        self.legacyPlay.setObjectName(u"legacyPlay")
        self.verticalLayout = QVBoxLayout(self.legacyPlay)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.legacyPlay)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.legacyPlay)
        self.legacyPlayPlus = QWidget()
        self.legacyPlayPlus.setObjectName(u"legacyPlayPlus")
        self.verticalLayout_2 = QVBoxLayout(self.legacyPlayPlus)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.legacyPlayPlus)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.legacyPlayPlus_x2StaminaRadioButton = QRadioButton(self.widget)
        self.legacyPlayPlus_x2StaminaRadioButton.setObjectName(u"legacyPlayPlus_x2StaminaRadioButton")
        self.legacyPlayPlus_x2StaminaRadioButton.setText(u"x2")

        self.horizontalLayout_2.addWidget(self.legacyPlayPlus_x2StaminaRadioButton)

        self.legacyPlayPlus_x4StaminaRadioButton = QRadioButton(self.widget)
        self.legacyPlayPlus_x4StaminaRadioButton.setObjectName(u"legacyPlayPlus_x4StaminaRadioButton")
        self.legacyPlayPlus_x4StaminaRadioButton.setText(u"x4")

        self.horizontalLayout_2.addWidget(self.legacyPlayPlus_x4StaminaRadioButton)

        self.legacyPlayPlus_x6StaminaRadioButton = QRadioButton(self.widget)
        self.legacyPlayPlus_x6StaminaRadioButton.setObjectName(u"legacyPlayPlus_x6StaminaRadioButton")
        self.legacyPlayPlus_x6StaminaRadioButton.setText(u"x6")

        self.horizontalLayout_2.addWidget(self.legacyPlayPlus_x6StaminaRadioButton)


        self.verticalLayout_2.addWidget(self.widget)

        self.legacyPlayPlus_useFragmentsGroupBox = QGroupBox(self.legacyPlayPlus)
        self.legacyPlayPlus_useFragmentsGroupBox.setObjectName(u"legacyPlayPlus_useFragmentsGroupBox")
        sizePolicy2.setHeightForWidth(self.legacyPlayPlus_useFragmentsGroupBox.sizePolicy().hasHeightForWidth())
        self.legacyPlayPlus_useFragmentsGroupBox.setSizePolicy(sizePolicy2)
        self.legacyPlayPlus_useFragmentsGroupBox.setCheckable(True)
        self.legacyPlayPlus_useFragmentsGroupBox.setChecked(False)
        self.horizontalLayout_3 = QHBoxLayout(self.legacyPlayPlus_useFragmentsGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.legacyPlayPlus_x11fragRadioButton = QRadioButton(self.legacyPlayPlus_useFragmentsGroupBox)
        self.legacyPlayPlus_x11fragRadioButton.setObjectName(u"legacyPlayPlus_x11fragRadioButton")
        self.legacyPlayPlus_x11fragRadioButton.setText(u"x1.1\n"
"100")

        self.horizontalLayout_3.addWidget(self.legacyPlayPlus_x11fragRadioButton)

        self.legacyPlayPlus_x125fragRadioButton = QRadioButton(self.legacyPlayPlus_useFragmentsGroupBox)
        self.legacyPlayPlus_x125fragRadioButton.setObjectName(u"legacyPlayPlus_x125fragRadioButton")
        self.legacyPlayPlus_x125fragRadioButton.setText(u"x1.25\n"
"125")

        self.horizontalLayout_3.addWidget(self.legacyPlayPlus_x125fragRadioButton)

        self.legacyPlayPlus_x15fragRadioButton = QRadioButton(self.legacyPlayPlus_useFragmentsGroupBox)
        self.legacyPlayPlus_x15fragRadioButton.setObjectName(u"legacyPlayPlus_x15fragRadioButton")
        self.legacyPlayPlus_x15fragRadioButton.setText(u"x1.5\n"
"500")

        self.horizontalLayout_3.addWidget(self.legacyPlayPlus_x15fragRadioButton)


        self.verticalLayout_2.addWidget(self.legacyPlayPlus_useFragmentsGroupBox)

        self.stackedWidget.addWidget(self.legacyPlayPlus)
        self.play = QWidget()
        self.play.setObjectName(u"play")
        self.verticalLayout_4 = QVBoxLayout(self.play)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.play_memoryBoostCheckBox = QCheckBox(self.play)
        self.play_memoryBoostCheckBox.setObjectName(u"play_memoryBoostCheckBox")

        self.verticalLayout_4.addWidget(self.play_memoryBoostCheckBox)

        self.stackedWidget.addWidget(self.play)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.mapTypeWidget)

        self.widget_2 = QWidget(TabTools_StepCalculator)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalWidget = QWidget(self.groupBox)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.horizontalWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.playResultSpinBox = QDoubleSpinBox(self.horizontalWidget)
        self.playResultSpinBox.setObjectName(u"playResultSpinBox")
        sizePolicy.setHeightForWidth(self.playResultSpinBox.sizePolicy().hasHeightForWidth())
        self.playResultSpinBox.setSizePolicy(sizePolicy)
        self.playResultSpinBox.setDecimals(3)
        self.playResultSpinBox.setMaximum(100.000000000000000)
        self.playResultSpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.playResultSpinBox)


        self.verticalLayout_5.addWidget(self.horizontalWidget)

        self.calculatePlayResultFromScoreButton = QPushButton(self.groupBox)
        self.calculatePlayResultFromScoreButton.setObjectName(u"calculatePlayResultFromScoreButton")

        self.verticalLayout_5.addWidget(self.calculatePlayResultFromScoreButton)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalWidget_2 = QWidget(self.groupBox_2)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.horizontalWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.doubleSpinBox = QDoubleSpinBox(self.horizontalWidget_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox)


        self.verticalLayout_6.addWidget(self.horizontalWidget_2)


        self.horizontalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(TabTools_StepCalculator)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TabTools_StepCalculator)
    # setupUi

    def retranslateUi(self, TabTools_StepCalculator):
        self.label.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partnerStepValueLabel", None))
        self.mapTypeLegacyPlayRadioButton.setText("")
        self.mapTypePlayRadioButton.setText("")
        self.mapTypeLegacyPlayPlusRadioButton.setText("")
        self.label_3.setText(QCoreApplication.translate("TabTools_StepCalculator", u"legacyPlay.noOptions", None))
        self.legacyPlayPlus_useFragmentsGroupBox.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"legacyPlayPlus.useFragments", None))
        self.play_memoryBoostCheckBox.setText(QCoreApplication.translate("TabTools_StepCalculator", u"play.memoryBoost", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"calculation", None))
        self.label_2.setText(QCoreApplication.translate("TabTools_StepCalculator", u"playResultLabel", None))
        self.calculatePlayResultFromScoreButton.setText(QCoreApplication.translate("TabTools_StepCalculator", u"calculatePlayResultFromScoreButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"inverseCalculation", None))
        self.label_4.setText(QCoreApplication.translate("TabTools_StepCalculator", u"targetStep", None))
        pass
    # retranslateUi

