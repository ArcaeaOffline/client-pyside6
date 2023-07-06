from enum import IntEnum
from typing import Optional

from arcaea_offline.calculate import calculate_score_range
from arcaea_offline.models import Chart, Score, ScoreInsert
from PySide6.QtCore import QCoreApplication, QDateTime, Signal, Slot
from PySide6.QtWidgets import QMessageBox, QWidget

from ui.designer.components.scoreEditor_ui import Ui_ScoreEditor


class ScoreValidateResult(IntEnum):
    Ok = 0
    ScoreMismatch = 1
    ScoreEmpty = 2
    ChartInvalid = 50


class ScoreEditor(Ui_ScoreEditor, QWidget):
    valueChanged = Signal()
    accepted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.__validateBeforeAccept = True
        self.__chart = None

        self.scoreLineEdit.textChanged.connect(self.valueChanged)
        self.pureSpinBox.valueChanged.connect(self.valueChanged)
        self.farSpinBox.valueChanged.connect(self.valueChanged)
        self.lostSpinBox.valueChanged.connect(self.valueChanged)
        self.dateTimeEdit.dateTimeChanged.connect(self.valueChanged)
        self.maxRecallSpinBox.valueChanged.connect(self.valueChanged)
        self.clearTypeComboBox.currentIndexChanged.connect(self.valueChanged)
        self.valueChanged.connect(self.validateScore)
        self.valueChanged.connect(self.updateValidateLabel)

        self.clearTypeComboBox.addItem("HARD LOST", -1)
        self.clearTypeComboBox.addItem("TRACK LOST", 0)
        self.clearTypeComboBox.addItem("TRACK COMPLETE", 1)
        self.clearTypeComboBox.setCurrentIndex(-1)

    def setValidateBeforeAccept(self, __bool: bool):
        self.__validateBeforeAccept = __bool

    def triggerValidateMessageBox(self):
        validate = self.validateScore()

        if validate == ScoreValidateResult.Ok:
            return True
        if validate == ScoreValidateResult.ChartInvalid:
            QMessageBox.critical(
                self,
                # fmt: off
                QCoreApplication.translate("ScoreEditor", "chartInvalidDialog.title"),
                QCoreApplication.translate("ScoreEditor", "chartInvalidDialog.title"),
                # fmt: on
            )
            return False
        if validate == ScoreValidateResult.ScoreMismatch:
            result = QMessageBox.warning(
                self,
                # fmt: off
                QCoreApplication.translate("ScoreEditor", "scoreMismatchDialog.title"),
                QCoreApplication.translate("ScoreEditor", "scoreMismatchDialog.content"),
                # fmt: on
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No,
            )
            return result == QMessageBox.StandardButton.Yes
        elif validate == ScoreValidateResult.ScoreEmpty:
            result = QMessageBox.warning(
                self,
                # fmt: off
                QCoreApplication.translate("ScoreEditor", "emptyScoreDialog.title"),
                QCoreApplication.translate("ScoreEditor", "emptyScoreDialog.content"),
                # fmt: on
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No,
            )
            return result == QMessageBox.StandardButton.Yes
        else:
            return False

    @Slot()
    def on_commitButton_clicked(self):
        userAccept = (
            self.triggerValidateMessageBox() if self.__validateBeforeAccept else True
        )

        if userAccept:
            self.accepted.emit()

    def score(self):
        score_text = self.scoreLineEdit.text().replace("'", "")
        return int(score_text) if score_text else 0

    def setMinimums(self):
        self.pureSpinBox.setMinimum(0)
        self.farSpinBox.setMinimum(0)
        self.lostSpinBox.setMinimum(0)
        self.maxRecallSpinBox.setMinimum(-1)

    def setLimits(self, chart: Chart):
        self.setMinimums()
        self.pureSpinBox.setMaximum(chart.note)
        self.farSpinBox.setMaximum(chart.note)
        self.lostSpinBox.setMaximum(chart.note)
        self.maxRecallSpinBox.setMaximum(chart.note)

    def resetLimits(self):
        self.setMinimums()
        self.pureSpinBox.setMaximum(0)
        self.farSpinBox.setMaximum(0)
        self.lostSpinBox.setMaximum(0)
        self.maxRecallSpinBox.setMaximum(0)

    def setChart(self, chart: Optional[Chart]):
        if isinstance(chart, Chart):
            self.__chart = chart
            self.setLimits(chart)
        else:
            self.__chart = None
            self.resetLimits()
        self.updateValidateLabel()

    def validateScore(self) -> ScoreValidateResult:
        if not isinstance(self.__chart, Chart):
            return ScoreValidateResult.ChartInvalid

        score = self.value()

        score_range = calculate_score_range(self.__chart, score.pure, score.far)
        score_in_range = score_range[0] <= score.score <= score_range[1]
        note_in_range = score.pure + score.far + score.lost <= self.__chart.note
        if not score_in_range or not note_in_range:
            return ScoreValidateResult.ScoreMismatch
        if score.score == 0:
            return ScoreValidateResult.ScoreEmpty
        return ScoreValidateResult.Ok

    def updateValidateLabel(self):
        validate = self.validateScore()

        if validate == ScoreValidateResult.Ok:
            text = QCoreApplication.translate("ScoreEditor", "validate.ok")
        elif validate == ScoreValidateResult.ChartInvalid:
            text = QCoreApplication.translate("ScoreEditor", "validate.chartInvalid")
        elif validate == ScoreValidateResult.ScoreMismatch:
            text = QCoreApplication.translate("ScoreEditor", "validate.scoreMismatch")
        elif validate == ScoreValidateResult.ScoreEmpty:
            text = QCoreApplication.translate("ScoreEditor", "validate.scoreEmpty")
        else:
            text = QCoreApplication.translate("ScoreEditor", "validate.unknownState")

        self.validateLabel.setText(text)

    def value(self):
        if isinstance(self.__chart, Chart):
            return ScoreInsert(
                song_id=self.__chart.song_id,
                rating_class=self.__chart.rating_class,
                score=self.score(),
                pure=self.pureSpinBox.value(),
                far=self.farSpinBox.value(),
                lost=self.lostSpinBox.value(),
                time=self.dateTimeEdit.dateTime().toSecsSinceEpoch(),
                max_recall=self.maxRecallSpinBox.value()
                if self.maxRecallSpinBox.value() > -1
                else None,
                clear_type=None,
            )

    def setValue(self, score: Score | ScoreInsert):
        if isinstance(score, (Score, ScoreInsert)):
            scoreText = str(score.score)
            scoreText = scoreText.rjust(8, "0")
            self.scoreLineEdit.setText(scoreText)
            self.pureSpinBox.setValue(score.pure)
            self.farSpinBox.setValue(score.far)
            self.lostSpinBox.setValue(score.lost)
            self.dateTimeEdit.setDateTime(QDateTime.fromSecsSinceEpoch(score.time))
            if score.max_recall is not None:
                self.maxRecallSpinBox.setValue(score.max_recall)
            if score.clear_type is not None:
                self.clearTypeComboBox.setCurrentIndex(score.clear_type)

    def reset(self):
        self.setChart(None)
        self.scoreLineEdit.setText("''")
        self.pureSpinBox.setValue(0)
        self.farSpinBox.setValue(0)
        self.lostSpinBox.setValue(0)
        self.maxRecallSpinBox.setValue(-1)
        self.clearTypeComboBox.setCurrentIndex(-1)
