import logging

from arcaea_offline.calculate.world_step import (
    AmaneBelowExPartnerBonus,
    AwakenedEtoPartnerBonus,
    AwakenedIlithPartnerBonus,
    AwakenedLunaPartnerBonus,
    LegacyMapStepBooster,
    MayaPartnerBonus,
    MemoriesStepBooster,
    PartnerBonus,
    PlayResult,
    calculate_play_rating_from_step,
    calculate_step,
    calculate_step_original,
)
from PySide6.QtCore import (
    QCoreApplication,
    QEasingCurve,
    QObject,
    QSize,
    QTimeLine,
    Signal,
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QAbstractButton,
    QButtonGroup,
    QDialog,
    QGraphicsColorizeEffect,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ui.designer.tabs.tabTools.tabTools_StepCalculator_ui import (
    Ui_TabTools_StepCalculator,
)
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.implements.components.chartSelector import ChartSelector
from ui.implements.components.playRatingCalculator import PlayRatingCalculator
from ui.implements.components.songIdSelector import SongIdSelectorMode

logger = logging.getLogger(__name__)


class ButtonGrayscaleEffectApplier(QObject):
    def __init__(self, parent: QAbstractButton):
        super().__init__(parent)
        self.timeline = QTimeLine(500, self)
        self.timeline.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.timeline.frameChanged.connect(self.applyGrayscaleEffect)

        parent.toggled.connect(self.triggerEffectAnimation)
        self.triggerEffectAnimation(parent.isChecked())

    def triggerEffectAnimation(self, buttonEnabled: bool):
        if self.timeline.state() == QTimeLine.State.Running:
            self.timeline.stop()
        startFrame = self.timeline.currentFrame()
        stopFrame = 0 if buttonEnabled else 100

        self.timeline.setFrameRange(startFrame, stopFrame)
        self.timeline.start()

    def applyGrayscaleEffect(self, frame: int):
        target: QAbstractButton = self.parent()
        value = frame / 100

        effect = QGraphicsColorizeEffect(target)
        effect.setColor("#000000")
        effect.setStrength(value)
        target.setGraphicsEffect(effect)


class PlayRatingCalculatorDialog(QDialog):
    accepted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.verticalLayout = QVBoxLayout(self)

        self.chartSelector = ChartSelector(self)
        self.chartSelector.setSongIdSelectorMode(SongIdSelectorMode.Chart)
        self.verticalLayout.addWidget(self.chartSelector)

        self.playRatingCalculator = PlayRatingCalculator(self)
        self.verticalLayout.addWidget(self.playRatingCalculator)

        self.acceptButton = QPushButton(self)
        self.acceptButton.setText(
            QCoreApplication.translate("StepCalculator", "playRatingCalculatorDialog.acceptButton")
        )  # fmt: skip
        self.acceptButton.setEnabled(False)
        self.verticalLayout.addWidget(self.acceptButton)

        self.chartSelector.valueChanged.connect(self.updatePlayRatingCalculator)
        self.playRatingCalculator.arcaeaScoreLineEdit.textChanged.connect(
            self.updateAcceptButton
        )
        self.acceptButton.clicked.connect(self.accepted)

    def updatePlayRatingCalculator(self):
        chart = self.chartSelector.value()
        if chart is None:
            self.playRatingCalculator.setConstant(None)
        else:
            self.playRatingCalculator.setConstant(chart.constant)
        self.updateAcceptButton()

    def updateAcceptButton(self):
        if self.playRatingCalculator.result is None:
            self.acceptButton.setEnabled(False)
        else:
            self.acceptButton.setEnabled(True)

    def reset(self):
        self.chartSelector.resetButton.click()
        self.playRatingCalculator.arcaeaScoreLineEdit.clear()

    def value(self):
        return self.playRatingCalculator.result


class TabTools_StepCalculator(Ui_TabTools_StepCalculator, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.calculate_toStep_calculatePlayResultFromScoreButton.clicked.connect(
            self.openChartAndScoreInputDialog
        )

        # set icons
        staminaIcon = QIcon(":/images/stepCalculator/stamina.png")
        for radioButton in [
            self.legacyPlayPlus_x2StaminaRadioButton,
            self.legacyPlayPlus_x4StaminaRadioButton,
            self.legacyPlayPlus_x6StaminaRadioButton,
        ]:
            radioButton.setIcon(staminaIcon)
            radioButton.setIconSize(QSize(25, 15))

        memoryBoostIcon = QIcon(":/images/stepCalculator/memory-boost.png")
        self.play_memoryBoostCheckBox.setIcon(memoryBoostIcon)
        self.play_memoryBoostCheckBox.setIconSize(QSize(75, 100))

        mapTypeIconSize = QSize(150, 50)

        for button, pixmap in zip(
            [
                self.mapTypeLegacyPlayRadioButton,
                self.mapTypeLegacyPlayPlusRadioButton,
                self.mapTypePlayRadioButton,
            ],
            [
                QPixmap(":/images/stepCalculator/legacy-play.png"),
                QPixmap(":/images/stepCalculator/legacy-play-plus.png"),
                QPixmap(":/images/stepCalculator/play.png"),
            ],
        ):
            button.setIconSize(mapTypeIconSize)
            button.setIcon(pixmap)

        # apply grayscale effects
        self.buttonGrayscaleEffectAppliers = []
        for button in [
            self.mapTypeLegacyPlayRadioButton,
            self.mapTypeLegacyPlayPlusRadioButton,
            self.mapTypePlayRadioButton,
            self.legacyPlayPlus_x2StaminaRadioButton,
            self.legacyPlayPlus_x4StaminaRadioButton,
            self.legacyPlayPlus_x6StaminaRadioButton,
            self.play_memoryBoostCheckBox,
        ]:
            applier = ButtonGrayscaleEffectApplier(button)
            self.buttonGrayscaleEffectAppliers.append(applier)

        # create button groups
        self.mapTypeButtonGroup = QButtonGroup(self)
        self.mapTypeButtonGroup.addButton(self.mapTypeLegacyPlayRadioButton, 0)
        self.mapTypeButtonGroup.addButton(self.mapTypeLegacyPlayPlusRadioButton, 1)
        self.mapTypeButtonGroup.addButton(self.mapTypePlayRadioButton, 2)
        self.mapTypeButtonGroup.idToggled.connect(self.stackedWidget.setCurrentIndex)
        self.mapTypePlayRadioButton.setChecked(True)

        self.legacyPlayPlusStaminaButtonGroup = QButtonGroup(self)
        self.legacyPlayPlusStaminaButtonGroup.addButton(
            self.legacyPlayPlus_x2StaminaRadioButton, 2
        )
        self.legacyPlayPlusStaminaButtonGroup.addButton(
            self.legacyPlayPlus_x4StaminaRadioButton, 4
        )
        self.legacyPlayPlusStaminaButtonGroup.addButton(
            self.legacyPlayPlus_x6StaminaRadioButton, 6
        )
        self.legacyPlayPlus_x2StaminaRadioButton.setChecked(True)

        self.legacyPlayPlusFragmentsButtonGroup = QButtonGroup(self)
        self.legacyPlayPlusFragmentsButtonGroup.addButton(
            self.legacyPlayPlus_x11fragRadioButton, 100
        )
        self.legacyPlayPlusFragmentsButtonGroup.addButton(
            self.legacyPlayPlus_x125fragRadioButton, 250
        )
        self.legacyPlayPlusFragmentsButtonGroup.addButton(
            self.legacyPlayPlus_x15fragRadioButton, 500
        )

        # bind calculate functions
        self.mapTypeButtonGroup.buttonToggled.connect(self.tryCalculate)
        self.legacyPlayPlusStaminaButtonGroup.buttonToggled.connect(self.tryCalculate)
        self.legacyPlayPlusFragmentsButtonGroup.buttonToggled.connect(self.tryCalculate)
        self.play_memoryBoostCheckBox.toggled.connect(self.tryCalculate)
        self.partnerStepValueSpinBox.valueChanged.connect(self.tryCalculate)
        self.partnerSkillGroupBox.toggled.connect(self.tryCalculate)
        self.partnerSkillStepBonusLineEdit.textChanged.connect(self.tryCalculate)
        self.partnerSkillFinalMultiplierLineEdit.textChanged.connect(self.tryCalculate)
        self.calculate_toStep_playResultSpinBox.valueChanged.connect(self.tryCalculate)
        self.calculate_fromStep_targetStepSpinBox.valueChanged.connect(
            self.tryCalculate
        )

        # connect partner skill preset buttons
        self.partnerSkillPresetButton_awakenedIlith.clicked.connect(
            self.applyPartnerPreset
        )
        self.partnerSkillPresetButton_awakenedEto.clicked.connect(
            self.applyPartnerPreset
        )
        self.partnerSkillPresetButton_awakenedLuna.clicked.connect(
            self.applyPartnerPreset
        )
        self.partnerSkillPresetButton_amaneBelowEx.clicked.connect(
            self.applyPartnerPreset
        )
        self.partnerSkillPresetButton_maya.clicked.connect(self.applyPartnerPreset)

        self.playRatingCalculatorDialog = PlayRatingCalculatorDialog(self)
        self.playRatingCalculatorDialog.accepted.connect(self.set_toStep_PlayRating)

    def openChartAndScoreInputDialog(self):
        self.playRatingCalculatorDialog.reset()
        self.playRatingCalculatorDialog.show()

    def set_toStep_PlayRating(self):
        result = self.playRatingCalculatorDialog.value()
        if result is not None:
            self.calculate_toStep_playResultSpinBox.setValue(result)
            self.playRatingCalculatorDialog.close()

    def applyPartnerPreset(self):
        if not self.sender():
            return

        objectName = self.sender().objectName()

        if not objectName:
            return

        formatString = "partnerSkillPresetButton_{}"
        if objectName == formatString.format("awakenedIlith"):
            pb = AwakenedIlithPartnerBonus
        elif objectName == formatString.format("awakenedEto"):
            pb = AwakenedEtoPartnerBonus
        elif objectName == formatString.format("awakenedLuna"):
            pb = AwakenedLunaPartnerBonus
        elif objectName == formatString.format("amaneBelowEx"):
            pb = AmaneBelowExPartnerBonus
        elif objectName == formatString.format("maya"):
            pb = MayaPartnerBonus
        else:
            return

        self.partnerSkillStepBonusLineEdit.setText(str(pb.step_bonus))
        self.partnerSkillFinalMultiplierLineEdit.setText(str(pb.final_multiplier))

    def toStepPlayResult(self):
        return PlayResult(
            play_rating=self.calculate_toStep_playResultSpinBox.value(),
            partner_step=self.partnerStepValueSpinBox.value(),
        )

    def partnerBonus(self):
        if self.partnerSkillGroupBox.isChecked():
            try:
                partnerBonus = PartnerBonus(
                    step_bonus=self.partnerSkillStepBonusLineEdit.text(),
                    final_multiplier=self.partnerSkillFinalMultiplierLineEdit.text(),
                )
                partnerBonus.step_bonus
                partnerBonus.final_multiplier
                return partnerBonus
            except Exception:
                if self.detailedLogOutputCheckBox.isChecked():
                    logger.exception("Cannot parse PartnerBonus input")
                return PartnerBonus()

        return PartnerBonus()

    def stepBooster(self):
        if self.mapTypeButtonGroup.checkedId() == 1:
            # Legacy Play+
            stamina = self.legacyPlayPlusStaminaButtonGroup.checkedId()
            if self.legacyPlayPlus_useFragmentsGroupBox.isChecked():
                fragment = self.legacyPlayPlusFragmentsButtonGroup.checkedId()
                fragment = fragment if fragment > -1 else None
            else:
                fragment = None
            return None if stamina < 0 else LegacyMapStepBooster(stamina, fragment)
        elif self.mapTypeButtonGroup.checkedId() == 2:
            # General Music Play
            if self.play_memoryBoostCheckBox.isChecked():
                return MemoriesStepBooster()
            else:
                return None
        else:
            return None

    def tryCalculate(self):
        if self.partnerStepValueSpinBox.value() <= 0.0:
            self.calculate_toStep_resultLabel.setText("...")
            self.calculate_fromStep_resultLabel.setText("...")
            return

        # toStep
        try:
            playResult = self.toStepPlayResult()
            partnerBonus = self.partnerBonus()
            stepBooster = self.stepBooster()

            stepOriginal = calculate_step_original(
                playResult, partner_bonus=partnerBonus, step_booster=stepBooster
            )
            step = calculate_step(
                playResult, partner_bonus=partnerBonus, step_booster=stepBooster
            )
            self.calculate_toStep_resultLabel.setText(str(step))
            self.calculate_toStep_detailedResultLabel.setText(str(stepOriginal))
        except Exception:
            if self.detailedLogOutputCheckBox.isChecked():
                logger.exception("Cannot calculate toStep")
            self.calculate_toStep_resultLabel.setText("...")

        # fromStep
        try:
            fromStepResult = calculate_play_rating_from_step(
                self.calculate_fromStep_targetStepSpinBox.value(),
                self.partnerStepValueSpinBox.value(),
                partner_bonus=partnerBonus,
                step_booster=stepBooster,
            )
            self.calculate_fromStep_resultLabel.setText(str(round(fromStepResult, 2)))
            self.calculate_fromStep_detailedResultLabel.setText(str(fromStepResult))
        except Exception:
            if self.detailedLogOutputCheckBox.isChecked():
                logger.exception("Cannot calculate fromStep")
            self.calculate_fromStep_resultLabel.setText("...")
