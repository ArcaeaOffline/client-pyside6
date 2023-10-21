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
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_TabTools_StepCalculator(object):
    def setupUi(self, TabTools_StepCalculator):
        if not TabTools_StepCalculator.objectName():
            TabTools_StepCalculator.setObjectName(u"TabTools_StepCalculator")
        TabTools_StepCalculator.resize(840, 549)
        TabTools_StepCalculator.setWindowTitle(u"TabTools_StepCalculator")
        self.verticalLayout_3 = QVBoxLayout(TabTools_StepCalculator)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.detailedLogOutputCheckBox = QCheckBox(TabTools_StepCalculator)
        self.detailedLogOutputCheckBox.setObjectName(u"detailedLogOutputCheckBox")

        self.verticalLayout_3.addWidget(self.detailedLogOutputCheckBox)

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

        self.gridLayout_2.addWidget(self.mapTypePlayRadioButton, 2, 0, 1, 1)

        self.mapTypeLegacyPlayPlusRadioButton = QPushButton(self.mapTypeSelectorWidget)
        self.mapTypeLegacyPlayPlusRadioButton.setObjectName(u"mapTypeLegacyPlayPlusRadioButton")
        self.mapTypeLegacyPlayPlusRadioButton.setStyleSheet(u"QPushButton{background-color: transparent}")
        self.mapTypeLegacyPlayPlusRadioButton.setCheckable(True)
        self.mapTypeLegacyPlayPlusRadioButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.mapTypeLegacyPlayPlusRadioButton, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.mapTypeSelectorWidget)

        self.stackedWidget = QStackedWidget(self.mapTypeWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.legacyPlayPlus_useFragmentsGroupBox.sizePolicy().hasHeightForWidth())
        self.legacyPlayPlus_useFragmentsGroupBox.setSizePolicy(sizePolicy1)
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
"250")

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

        self.groupBox_3 = QGroupBox(self.mapTypeWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.partnerStepValueSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.partnerStepValueSpinBox.setObjectName(u"partnerStepValueSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.partnerStepValueSpinBox.sizePolicy().hasHeightForWidth())
        self.partnerStepValueSpinBox.setSizePolicy(sizePolicy2)
        self.partnerStepValueSpinBox.setMaximum(1000.000000000000000)
        self.partnerStepValueSpinBox.setSingleStep(1.000000000000000)
        self.partnerStepValueSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_5.addWidget(self.partnerStepValueSpinBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.partnerSkillGroupBox = QGroupBox(self.groupBox_3)
        self.partnerSkillGroupBox.setObjectName(u"partnerSkillGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.partnerSkillGroupBox.sizePolicy().hasHeightForWidth())
        self.partnerSkillGroupBox.setSizePolicy(sizePolicy3)
        self.partnerSkillGroupBox.setCheckable(True)
        self.partnerSkillGroupBox.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.partnerSkillGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.partnerSkillGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.partnerSkillGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.partnerSkillFinalMultiplierLineEdit = QLineEdit(self.partnerSkillGroupBox)
        self.partnerSkillFinalMultiplierLineEdit.setObjectName(u"partnerSkillFinalMultiplierLineEdit")
        self.partnerSkillFinalMultiplierLineEdit.setText(u"1.0")
        self.partnerSkillFinalMultiplierLineEdit.setPlaceholderText(u"1.0")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.partnerSkillFinalMultiplierLineEdit)

        self.partnerSkillStepBonusLineEdit = QLineEdit(self.partnerSkillGroupBox)
        self.partnerSkillStepBonusLineEdit.setObjectName(u"partnerSkillStepBonusLineEdit")
        self.partnerSkillStepBonusLineEdit.setText(u"+0.0")
        self.partnerSkillStepBonusLineEdit.setPlaceholderText(u"+0.0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.partnerSkillStepBonusLineEdit)


        self.verticalLayout_7.addLayout(self.formLayout)

        self.groupBox_4 = QGroupBox(self.partnerSkillGroupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.partnerSkillPresetButton_awakenedEto = QPushButton(self.groupBox_4)
        self.partnerSkillPresetButton_awakenedEto.setObjectName(u"partnerSkillPresetButton_awakenedEto")

        self.gridLayout_3.addWidget(self.partnerSkillPresetButton_awakenedEto, 0, 1, 1, 1)

        self.partnerSkillPresetButton_awakenedIlith = QPushButton(self.groupBox_4)
        self.partnerSkillPresetButton_awakenedIlith.setObjectName(u"partnerSkillPresetButton_awakenedIlith")

        self.gridLayout_3.addWidget(self.partnerSkillPresetButton_awakenedIlith, 0, 0, 1, 1)

        self.partnerSkillPresetButton_awakenedLuna = QPushButton(self.groupBox_4)
        self.partnerSkillPresetButton_awakenedLuna.setObjectName(u"partnerSkillPresetButton_awakenedLuna")

        self.gridLayout_3.addWidget(self.partnerSkillPresetButton_awakenedLuna, 1, 0, 1, 1)

        self.partnerSkillPresetButton_amaneBelowEx = QPushButton(self.groupBox_4)
        self.partnerSkillPresetButton_amaneBelowEx.setObjectName(u"partnerSkillPresetButton_amaneBelowEx")

        self.gridLayout_3.addWidget(self.partnerSkillPresetButton_amaneBelowEx, 1, 1, 1, 1)

        self.partnerSkillPresetButton_maya = QPushButton(self.groupBox_4)
        self.partnerSkillPresetButton_maya.setObjectName(u"partnerSkillPresetButton_maya")

        self.gridLayout_3.addWidget(self.partnerSkillPresetButton_maya, 2, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_4)


        self.verticalLayout_5.addWidget(self.partnerSkillGroupBox)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_3.addWidget(self.mapTypeWidget)

        self.widget_2 = QWidget(TabTools_StepCalculator)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.calculate_toStep_playResultSpinBox = QDoubleSpinBox(self.groupBox)
        self.calculate_toStep_playResultSpinBox.setObjectName(u"calculate_toStep_playResultSpinBox")
        sizePolicy2.setHeightForWidth(self.calculate_toStep_playResultSpinBox.sizePolicy().hasHeightForWidth())
        self.calculate_toStep_playResultSpinBox.setSizePolicy(sizePolicy2)
        self.calculate_toStep_playResultSpinBox.setDecimals(3)
        self.calculate_toStep_playResultSpinBox.setMaximum(100.000000000000000)
        self.calculate_toStep_playResultSpinBox.setSingleStep(0.100000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.calculate_toStep_playResultSpinBox)

        self.calculate_toStep_calculatePlayResultFromScoreButton = QPushButton(self.groupBox)
        self.calculate_toStep_calculatePlayResultFromScoreButton.setObjectName(u"calculate_toStep_calculatePlayResultFromScoreButton")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.calculate_toStep_calculatePlayResultFromScoreButton)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calculate_toStep_resultLabel = QLabel(self.groupBox)
        self.calculate_toStep_resultLabel.setObjectName(u"calculate_toStep_resultLabel")
        self.calculate_toStep_resultLabel.setText(u"...")
        self.calculate_toStep_resultLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_9.addWidget(self.calculate_toStep_resultLabel)

        self.calculate_toStep_detailedResultLabel = QLabel(self.groupBox)
        self.calculate_toStep_detailedResultLabel.setObjectName(u"calculate_toStep_detailedResultLabel")
        font = QFont()
        font.setPointSize(8)
        self.calculate_toStep_detailedResultLabel.setFont(font)
        self.calculate_toStep_detailedResultLabel.setStyleSheet(u"QLabel { color: gray; }")
        self.calculate_toStep_detailedResultLabel.setText(u"...")
        self.calculate_toStep_detailedResultLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.calculate_toStep_detailedResultLabel)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.verticalLayout_9)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_3 = QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.calculate_fromStep_targetStepSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.calculate_fromStep_targetStepSpinBox.setObjectName(u"calculate_fromStep_targetStepSpinBox")
        sizePolicy2.setHeightForWidth(self.calculate_fromStep_targetStepSpinBox.sizePolicy().hasHeightForWidth())
        self.calculate_fromStep_targetStepSpinBox.setSizePolicy(sizePolicy2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.calculate_fromStep_targetStepSpinBox)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.calculate_fromStep_resultLabel = QLabel(self.groupBox_2)
        self.calculate_fromStep_resultLabel.setObjectName(u"calculate_fromStep_resultLabel")
        self.calculate_fromStep_resultLabel.setText(u"...")
        self.calculate_fromStep_resultLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_10.addWidget(self.calculate_fromStep_resultLabel)

        self.calculate_fromStep_detailedResultLabel = QLabel(self.groupBox_2)
        self.calculate_fromStep_detailedResultLabel.setObjectName(u"calculate_fromStep_detailedResultLabel")
        self.calculate_fromStep_detailedResultLabel.setFont(font)
        self.calculate_fromStep_detailedResultLabel.setStyleSheet(u"QLabel { color: gray; }")
        self.calculate_fromStep_detailedResultLabel.setText(u"...")
        self.calculate_fromStep_detailedResultLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.calculate_fromStep_detailedResultLabel)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.verticalLayout_10)


        self.horizontalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(TabTools_StepCalculator)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TabTools_StepCalculator)
    # setupUi

    def retranslateUi(self, TabTools_StepCalculator):
        self.detailedLogOutputCheckBox.setText(QCoreApplication.translate("TabTools_StepCalculator", u"detailedLogOutput", None))
        self.mapTypeLegacyPlayRadioButton.setText("")
        self.mapTypePlayRadioButton.setText("")
        self.mapTypeLegacyPlayPlusRadioButton.setText("")
        self.label_3.setText(QCoreApplication.translate("TabTools_StepCalculator", u"legacyPlay.noOptions", None))
        self.legacyPlayPlus_useFragmentsGroupBox.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"legacyPlayPlus.useFragments", None))
        self.play_memoryBoostCheckBox.setText(QCoreApplication.translate("TabTools_StepCalculator", u"play.memoryBoost", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"partner.title", None))
        self.label.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.stepValueLabel", None))
        self.partnerSkillGroupBox.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.title", None))
        self.label_5.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.stepBonus", None))
        self.label_6.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.finalMultiplier", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.presets", None))
        self.partnerSkillPresetButton_awakenedEto.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.presets.awakenedEto", None))
        self.partnerSkillPresetButton_awakenedIlith.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.presets.awakenedIlith", None))
        self.partnerSkillPresetButton_awakenedLuna.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.presets.awakenedLuna", None))
        self.partnerSkillPresetButton_amaneBelowEx.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.presets.amaneBelowEx", None))
        self.partnerSkillPresetButton_maya.setText(QCoreApplication.translate("TabTools_StepCalculator", u"partner.skill.presets.maya", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.toStep", None))
        self.label_2.setText(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.toStep.playResultLabel", None))
        self.calculate_toStep_calculatePlayResultFromScoreButton.setText(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.toStep.calculatePlayResultFromScoreButton", None))
        self.label_7.setText(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.toStep.resultLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.fromStep", None))
        self.label_4.setText(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.fromStep.targetStepLabel", None))
        self.label_9.setText(QCoreApplication.translate("TabTools_StepCalculator", u"calculate.fromStep.resultLabel", None))
        pass
    # retranslateUi

