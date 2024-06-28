from dataclasses import dataclass
from enum import IntEnum
from typing import Any, Optional

from arcaea_offline.calculate import calculate_score_range
from arcaea_offline.models import Chart, Score
from PySide6.QtCore import QCoreApplication, QDateTime, Signal, Slot
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QLineEdit,
    QMessageBox,
    QSpinBox,
    QWidget,
)

from ui.designer.components.scoreEditor_ui import Ui_ScoreEditor
from ui.extends.shared.language import LanguageChangeEventFilter


class ScoreValidateResult(IntEnum):
    Ok = 0x001

    ScoreMismatch = 0x010
    ScoreEmpty = 0x020
    ScoreIncomplete = 0x040
    ScoreIncompleteForValidate = 0x080

    ChartNotSet = 0x100
    ChartIncomplete = 0x200


@dataclass
class ScoreEditorValidationItem:
    flag: int
    title: str = ""
    text: str = ""
    warnIfIncomplete: bool = False


class ScoreEditor(Ui_ScoreEditor, QWidget):
    valueChanged = Signal()
    accepted = Signal()

    VALIDATION_ITEMS = [
        ScoreEditorValidationItem(
            ScoreValidateResult.ChartIncomplete,
            warnIfIncomplete=True,
        ),
        ScoreEditorValidationItem(
            ScoreValidateResult.ScoreMismatch,
        ),
        ScoreEditorValidationItem(
            ScoreValidateResult.ScoreEmpty,
        ),
        ScoreEditorValidationItem(
            ScoreValidateResult.ScoreIncompleteForValidate, warnIfIncomplete=True
        ),
    ]

    VALIDATION_ITEMS_TEXT = [
        [
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.chartIncomplete.title"),
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.chartIncomplete.text"),
        ],
        [
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.scoreMismatch.title"),
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.scoreMismatch.text"),
        ],
        [
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.emptyScore.title"),
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.emptyScore.text"),
        ],
        [
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.scoreIncompleteForValidate.title"),
            lambda: QCoreApplication.translate("ScoreEditor", "confirmDialog.scoreIncompleteForValidate.text"),
        ],
    ]  # fmt: skip

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.__validateBeforeAccept = True
        self.__warnIfIncomplete = True
        self.warnIfIncompleteCheckBox.setChecked(self.__warnIfIncomplete)
        self.warnIfIncompleteCheckBox.toggled.connect(self.setWarnIfIncomplete)

        self.__chart = None
        self.__score_id = None

        self.scoreLineEdit.textChanged.connect(self.valueChanged)
        self.pureSpinBox.valueChanged.connect(self.valueChanged)
        self.farSpinBox.valueChanged.connect(self.valueChanged)
        self.lostSpinBox.valueChanged.connect(self.valueChanged)
        self.dateTimeEdit.dateTimeChanged.connect(self.valueChanged)
        self.maxRecallSpinBox.valueChanged.connect(self.valueChanged)
        self.modifierComboBox.currentIndexChanged.connect(self.valueChanged)
        self.clearTypeComboBox.currentIndexChanged.connect(self.valueChanged)
        self.commentLineEdit.textChanged.connect(self.valueChanged)
        self.pureNoneCheckBox.toggled.connect(self.valueChanged)
        self.farNoneCheckBox.toggled.connect(self.valueChanged)
        self.lostNoneCheckBox.toggled.connect(self.valueChanged)
        self.dateNoneCheckBox.toggled.connect(self.valueChanged)
        self.maxRecallNoneCheckBox.toggled.connect(self.valueChanged)
        self.modifierNoneCheckBox.toggled.connect(self.valueChanged)
        self.clearTypeNoneCheckBox.toggled.connect(self.valueChanged)
        self.commentNoneCheckBox.toggled.connect(self.valueChanged)
        self.valueChanged.connect(self.validateScore)
        self.valueChanged.connect(self.updateValidateLabel)

        self.modifierComboBox.addItem("NORMAL", 0)
        self.modifierComboBox.addItem("EASY", 1)
        self.modifierComboBox.addItem("HARD", 2)
        self.modifierComboBox.setCurrentIndex(-1)
        self.clearTypeComboBox.addItem("TRACK LOST", 0)
        self.clearTypeComboBox.addItem("NORMAL CLEAR", 1)
        self.clearTypeComboBox.addItem("FULL RECALL", 2)
        self.clearTypeComboBox.addItem("PURE MEMORY", 3)
        self.clearTypeComboBox.addItem("EASY CLEAR", 4)
        self.clearTypeComboBox.addItem("HARD CLEAR", 5)
        self.clearTypeComboBox.setCurrentIndex(-1)

        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.valueChanged.connect(self.updatePreviewLabel)

    def retranslateUi(self, *args):
        super().retranslateUi(self)

        for item, itemTextCallables in zip(
            self.VALIDATION_ITEMS, self.VALIDATION_ITEMS_TEXT
        ):
            titleCallable, textCallable = itemTextCallables
            item.title = titleCallable()
            item.text = textCallable()

    def updatePreviewLabel(self):
        if score := self.value():
            texts = [
                f"({score.song_id}, {score.rating_class}), Score {score.score}",
                f"PURE {score.pure}, FAR {score.far}, LOST {score.lost}",
                f"MAX RECALL {score.max_recall}",
                f"Date {score.date}",
                f"Clear type {score.clear_type}",
                f"Modifier {score.modifier}",
            ]
            self.previewLabel.setText(
                f"{score.score}, P{score.pure} F{score.far} L{score.lost}, MR {score.max_recall}"
            )
            self.previewLabel.setToolTip("<br>".join(texts))
        else:
            self.previewLabel.setText("None")
            self.previewLabel.setToolTip("")

    def validateBeforeAccept(self):
        return self.__validateBeforeAccept

    def setValidateBeforeAccept(self, __bool: bool):
        self.__validateBeforeAccept = __bool

    def warnIfIncomplete(self):
        return self.__warnIfIncomplete

    def setWarnIfIncomplete(self, __bool: bool):
        if self.sender() != self.warnIfIncompleteCheckBox:
            self.warnIfIncompleteCheckBox.setChecked(__bool)
        self.__warnIfIncomplete = __bool

    def __triggerMessageBox(
        self, methodStr: str, title: str, text: str, userConfirmButton: bool = False
    ) -> QMessageBox.StandardButton:
        if methodStr == "critical":
            method = QMessageBox.critical
        elif methodStr == "warning":
            method = QMessageBox.warning
        else:
            method = QMessageBox.information

        if userConfirmButton:
            return method(
                self,
                title,
                text,
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No,
            )
        else:
            return method(self, title, text)

    def triggerValidateMessageBox(self):
        validate = self.validateScore()

        if validate & ScoreValidateResult.Ok:
            return True
        if validate & ScoreValidateResult.ChartNotSet:
            self.__triggerMessageBox(
                "critical",
                QCoreApplication.translate("ScoreEditor", "confirmDialog.chartNotSet.title"),
                QCoreApplication.translate("ScoreEditor", "confirmDialog.chartNotSet.text"),
            )  # fmt: skip
            return False
        if validate & ScoreValidateResult.ScoreIncomplete:
            self.__triggerMessageBox(
                "critical",
                QCoreApplication.translate("ScoreEditor", "confirmDialog.scoreIncomplete.title"),
                QCoreApplication.translate("ScoreEditor", "confirmDialog.scoreIncomplete.text"),
            )  # fmt: skip
            return False

        # since validate may have multiple results
        # ask user step by step, then return the final result
        finalResult = True

        for item in self.VALIDATION_ITEMS:
            if not finalResult:
                # user canceled commit, break then return
                break

            if not validate & item.flag:
                continue

            if item.warnIfIncomplete and not self.warnIfIncomplete():
                # if the item requires `warnIfIncomplete`
                # and the user set the `warnIfIncomplete` option to `False`
                # skip this validation
                continue

            finalResult = (
                self.__triggerMessageBox(
                    "warning", item.title, item.text, userConfirmButton=True
                )
                == QMessageBox.StandardButton.Yes
            )

        return finalResult

    @Slot()
    def on_commitButton_clicked(self):
        userAccept = (
            self.triggerValidateMessageBox() if self.__validateBeforeAccept else True
        )

        if userAccept:
            self.accepted.emit()

    def score(self):
        score_text = self.scoreLineEdit.text().replace("'", "")
        return int(score_text) if score_text else None

    def setComboBoxMaximums(self, max: int):
        self.pureSpinBox.setMaximum(max)
        self.farSpinBox.setMaximum(max)
        self.lostSpinBox.setMaximum(max)
        self.maxRecallSpinBox.setMaximum(max)

    def setLimits(self, chart: Chart):
        if not isinstance(chart, Chart) or chart.notes is None:
            self.setComboBoxMaximums(283375)
        else:
            self.setComboBoxMaximums(chart.notes)

    def resetLimits(self):
        self.setComboBoxMaximums(0)

    def setChart(self, chart: Optional[Chart]):
        if isinstance(chart, Chart):
            self.__chart = chart
            self.setLimits(chart)
        else:
            self.__chart = None
            self.resetLimits()
        self.updateValidateLabel()
        self.updatePreviewLabel()

    def validateScore(self) -> ScoreValidateResult:
        if not isinstance(self.__chart, Chart):
            return ScoreValidateResult.ChartNotSet

        flags = 0x000

        if self.__chart.notes is None:
            flags |= ScoreValidateResult.ChartIncomplete

        score = self.value()

        if score.score is None:
            flags |= ScoreValidateResult.ScoreIncomplete
        elif score.pure is None or score.far is None or score.lost is None:
            flags |= ScoreValidateResult.ScoreIncompleteForValidate
        elif self.__chart.notes is not None:
            score_range = calculate_score_range(
                self.__chart.notes, score.pure, score.far
            )
            note_in_range = score.pure + score.far + score.lost <= self.__chart.notes
            score_in_range = score_range[0] <= score.score <= score_range[1]
            if not score_in_range or not note_in_range:
                flags |= ScoreValidateResult.ScoreMismatch

        if score.score == 0:
            flags |= ScoreValidateResult.ScoreEmpty

        return ScoreValidateResult.Ok if flags == 0x000 else flags

    def updateValidateLabel(self):
        validate = self.validateScore()

        texts = []

        if validate & ScoreValidateResult.Ok:
            texts.append(QCoreApplication.translate("ScoreEditor", "validate.ok"))
        if validate & ScoreValidateResult.ChartNotSet:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.chartNotSet")
            )
        if validate & ScoreValidateResult.ChartIncomplete:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.chartIncomple")
            )
        if validate & ScoreValidateResult.ScoreMismatch:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.scoreMismatch")
            )
        if validate & ScoreValidateResult.ScoreEmpty:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.scoreEmpty")
            )
        if validate & ScoreValidateResult.ScoreIncomplete:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.scoreIncomplete")
            )
        if validate & ScoreValidateResult.ScoreIncompleteForValidate:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.scoreIncompleteForValidate")
            )  # fmt: skip

        if not texts:
            texts.append(
                QCoreApplication.translate("ScoreEditor", "validate.unknownState")
            )

        self.validateLabel.setText(" | ".join(texts))

    def __getItemBaseName(self, item: QLineEdit | QSpinBox | QDateTimeEdit | QComboBox):
        if isinstance(item, QSpinBox):
            return item.objectName().replace("SpinBox", "")
        elif isinstance(item, QLineEdit):
            if item.objectName() == "scoreLineEdit":
                return "score"
            return item.objectName().replace("LineEdit", "")
        elif isinstance(item, QComboBox):
            return item.objectName().replace("ComboBox", "")
        elif isinstance(item, QDateTimeEdit):
            return "date"

    def __getItemNoneCheckBox(self, itemBaseName: str) -> QCheckBox | None:
        return self.findChild(QCheckBox, f"{itemBaseName}NoneCheckBox")

    def __getItemEnabled(self, itemBaseName: str):
        return not self.__getItemNoneCheckBox(itemBaseName).isChecked()

    def getItemValue(self, item: QLineEdit | QSpinBox | QDateTimeEdit | QComboBox):
        if isinstance(item, QDateTimeEdit) and item.objectName() == "dateTimeEdit":
            return (
                None
                if self.dateNoneCheckBox.isChecked()
                else self.dateTimeEdit.dateTime().toSecsSinceEpoch()
            )

        itemBaseName = self.__getItemBaseName(item)
        itemEnabled = self.__getItemEnabled(itemBaseName)

        if isinstance(item, QSpinBox):
            return item.value() if itemEnabled else None
        elif isinstance(item, QLineEdit):
            return item.text() if itemEnabled else None
        elif isinstance(item, QComboBox):
            return item.currentData() if itemEnabled else None

    def value(self):
        if not isinstance(self.__chart, Chart):
            return

        score = Score(
            song_id=self.__chart.song_id, rating_class=self.__chart.rating_class
        )
        if self.__score_id is not None:
            score.id = self.__score_id
        score.score = self.score()
        score.pure = self.getItemValue(self.pureSpinBox)
        score.far = self.getItemValue(self.farSpinBox)
        score.lost = self.getItemValue(self.lostSpinBox)
        score.date = self.getItemValue(self.dateTimeEdit)
        score.max_recall = self.getItemValue(self.maxRecallSpinBox)
        score.modifier = self.getItemValue(self.modifierComboBox)
        score.clear_type = self.getItemValue(self.clearTypeComboBox)
        score.comment = self.getItemValue(self.commentLineEdit)
        return score

    def setItemValue(
        self, item: QLineEdit | QSpinBox | QDateTimeEdit | QComboBox, value: Any
    ):
        if isinstance(item, QDateTimeEdit) and item.objectName() == "dateTimeEdit":
            if value is None:
                self.dateNoneCheckBox.setChecked(True)
            else:
                self.dateNoneCheckBox.setChecked(False)
                self.dateTimeEdit.setDateTime(QDateTime.fromSecsSinceEpoch(value))

        itemBaseName = self.__getItemBaseName(item)
        itemNoneCheckBox = self.__getItemNoneCheckBox(itemBaseName)

        if value is None:
            itemNoneCheckBox.setChecked(True)
            return
        else:
            itemNoneCheckBox.setChecked(False)

        if isinstance(item, QSpinBox):
            item.setValue(value)
        elif isinstance(item, QLineEdit):
            item.setText(value)
        elif isinstance(item, QComboBox):
            item.setCurrentIndex(value)

    def setValue(self, score: Score):
        if not isinstance(score, Score):
            return

        if score.id is not None:
            self.__score_id = score.id
            self.idLabel.setText(str(self.__score_id))
        scoreText = str(score.score)
        scoreText = scoreText.rjust(8, "0")
        self.scoreLineEdit.setText(scoreText)

        self.setItemValue(self.pureSpinBox, score.pure)
        self.setItemValue(self.farSpinBox, score.far)
        self.setItemValue(self.lostSpinBox, score.lost)
        self.setItemValue(self.dateTimeEdit, score.date)
        self.setItemValue(self.maxRecallSpinBox, score.max_recall)
        self.setItemValue(self.modifierComboBox, score.modifier)
        self.setItemValue(self.clearTypeComboBox, score.clear_type)
        self.setItemValue(self.commentLineEdit, score.comment)

    def reset(self):
        self.setChart(None)
        self.scoreLineEdit.setText("''")
        self.pureSpinBox.setValue(0)
        self.farSpinBox.setValue(0)
        self.lostSpinBox.setValue(0)
        self.maxRecallSpinBox.setValue(0)
        self.modifierComboBox.setCurrentIndex(-1)
        self.clearTypeComboBox.setCurrentIndex(-1)
        self.commentLineEdit.setText("")
