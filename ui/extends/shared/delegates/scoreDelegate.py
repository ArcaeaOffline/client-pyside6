from typing import Union

from arcaea_offline.calculate import calculate_score_range
from arcaea_offline.models import Chart, Score
from arcaea_offline.utils.rating import rating_class_to_text
from arcaea_offline.utils.score import score_to_grade_text, zip_score_grade
from PySide6.QtCore import QAbstractItemModel, QDateTime, QModelIndex, Qt, Signal
from PySide6.QtGui import QColor, QFont, QLinearGradient
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from ui.implements.components.scoreEditor import ScoreEditor

from ..utils import keepWidgetInScreen
from .base import TextSegmentDelegate


class ScoreEditorDelegateWrapper(ScoreEditor):
    rejected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.hLine = QFrame(self)
        self.hLine.setFrameShape(QFrame.Shape.HLine)
        self.hLine.setFrameShadow(QFrame.Shadow.Plain)
        self.hLine.setFixedHeight(5)
        self.formLayout.insertRow(0, self.hLine)

        self.delegateHeader = QWidget(self)
        self.delegateHeaderHBoxLayout = QHBoxLayout(self.delegateHeader)
        self.delegateHeaderHBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.editorLabel = QLabel(self.delegateHeader)
        self.editorLabel.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.delegateHeaderHBoxLayout.addWidget(self.editorLabel)

        self.editorDiscardButton = QPushButton("Discard", self.delegateHeader)
        self.editorDiscardButton.clicked.connect(self.rejected)
        self.delegateHeaderHBoxLayout.addWidget(self.editorDiscardButton)

        self.formLayout.insertRow(0, self.delegateHeader)

    def setText(self, score: Score, _extra: str = None):
        text = "Editing "
        text += _extra or ""
        text += f"score {score.score}"
        text += f"<br>(P{score.pure} F{score.far} L{score.lost} | MR{score.max_recall})"
        self.editorLabel.setText(text)


class ScoreDelegate(TextSegmentDelegate):
    @staticmethod
    def createGradeGradientWrapper(topColor: QColor, bottomColor: QColor):
        def wrapper(x, y, width, height):
            gradient = QLinearGradient(x + (width / 2), y, x + (width / 2), y + height)
            gradient.setColorAt(0.1, topColor)
            gradient.setColorAt(0.9, bottomColor)
            return gradient

        return wrapper

    ScoreMismatchBackgroundColor = QColor("#e6a23c")
    PureFarLostColors = [
        QColor("#f22ec6"),
        QColor("#ff9028"),
        QColor("#ff0c43"),
    ]
    GradeGradientsWrappers = [  # EX+, EX, AA, A. B, C, D
        createGradeGradientWrapper(QColor("#83238c"), QColor("#2c72ae")),
        createGradeGradientWrapper(QColor("#721b6b"), QColor("#295b8d")),
        createGradeGradientWrapper(QColor("#5a3463"), QColor("#9b4b8d")),
        createGradeGradientWrapper(QColor("#46324d"), QColor("#92588a")),
        createGradeGradientWrapper(QColor("#43334a"), QColor("#755b7c")),
        createGradeGradientWrapper(QColor("#3b2b27"), QColor("#80566b")),
        createGradeGradientWrapper(QColor("#5d1d35"), QColor("#9f3c55")),
    ]

    def getScore(self, index: QModelIndex) -> Score | None:
        return None

    def getChart(self, index: QModelIndex) -> Chart | None:
        return None

    def getScoreValidateOk(self, index: QModelIndex) -> bool | None:
        score = self.getScore(index)
        chart = self.getChart(index)

        if isinstance(score, Score) and isinstance(chart, Chart):
            scoreRange = calculate_score_range(chart, score.pure, score.far)
            return scoreRange[0] <= score.score <= scoreRange[1]

    def getScoreGradeGradientWrapper(self, score: int):
        return zip_score_grade(score, self.GradeGradientsWrappers)

    def getTextSegments(self, index, option):
        score = self.getScore(index)
        chart = self.getChart(index)
        if not (isinstance(score, Score) and isinstance(chart, Chart)):
            return [
                [
                    {
                        self.TextRole: "Chart/Score Invalid",
                        self.ColorRole: QColor("#ff0000"),
                    }
                ]
            ]

        score_str = str(score.score).rjust(8, "0")
        score_str = f"{score_str[:-6]}'{score_str[-6:-3]}'{score_str[-3:]}"
        score_font = QFont(option.font)
        score_font.setPointSize(12)
        score_grade_font = QFont(score_font)
        score_grade_font.setBold(True)
        return [
            [
                {
                    self.TextRole: score_to_grade_text(score.score),
                    self.GradientWrapperRole: self.getScoreGradeGradientWrapper(
                        score.score
                    ),
                    self.FontRole: score_grade_font,
                },
                {self.TextRole: " | "},
                {self.TextRole: score_str, self.FontRole: score_font},
            ],
            [
                {
                    self.TextRole: f"PURE {score.pure}",
                    self.ColorRole: self.PureFarLostColors[0],
                },
                {self.TextRole: "  "},
                {
                    self.TextRole: f"FAR {score.far}",
                    self.ColorRole: self.PureFarLostColors[1],
                },
                {self.TextRole: "  "},
                {
                    self.TextRole: f"LOST {score.lost}",
                    self.ColorRole: self.PureFarLostColors[2],
                },
                {self.TextRole: " | "},
                {self.TextRole: f"MAX RECALL {score.max_recall}"},
            ],
            [
                {
                    self.TextRole: QDateTime.fromSecsSinceEpoch(score.time).toString(
                        "yyyy-MM-dd hh:mm:ss"
                    )
                }
            ],
        ]

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return True

    def paint(self, painter, option, index):
        # draw scoreMismatch warning background
        score = self.getScore(index)
        chart = self.getChart(index)
        if (
            isinstance(score, Score)
            and isinstance(chart, Chart)
            and self.paintWarningBackground(index)
        ):
            scoreValidateOk = self.getScoreValidateOk(index)
            if not scoreValidateOk:
                painter.save()
                painter.setPen(Qt.PenStyle.NoPen)
                bgColor = QColor(self.ScoreMismatchBackgroundColor)
                bgColor.setAlpha(50)
                painter.setBrush(bgColor)
                painter.drawRect(option.rect)
                painter.restore()

        option.text = ""
        super().paint(painter, option, index)

    def _closeEditor(self):
        editor = self.sender()
        self.closeEditor.emit(editor)

    def _commitEditor(self):
        editor = self.sender()
        self.commitData.emit(editor)
        self.closeEditor.emit(editor)

    def createEditor(self, parent, option, index) -> ScoreEditorDelegateWrapper:
        score = self.getScore(index)
        chart = self.getChart(index)
        if isinstance(score, Score) and isinstance(chart, Chart):
            editor = ScoreEditorDelegateWrapper(parent)
            editor.setWindowFlag(Qt.WindowType.Sheet, True)
            editor.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
            editor.setWindowTitle(
                f"{chart.name_en}({chart.song_id}) | {rating_class_to_text(chart.rating_class)} | {chart.package_id}"
            )
            editor.setText(self.getScore(index))
            editor.setValidateBeforeAccept(False)
            editor.move(parent.mapToGlobal(parent.pos()))
            editor.accepted.connect(self._commitEditor)
            editor.rejected.connect(self._closeEditor)
            editor.show()
            return editor
        return super().createEditor(parent, option, index)

    def updateEditorGeometry(self, editor, option, index):
        editor.setMaximumWidth(option.rect.width())
        editor.move(editor.pos() + option.rect.topLeft())

        keepWidgetInScreen(editor)

    def setEditorData(self, editor: ScoreEditorDelegateWrapper, index) -> None:
        score = self.getScore(index)
        chart = self.getChart(index)
        if isinstance(score, Score) and isinstance(chart, Chart):
            editor.setChart(chart)
            editor.setValue(score)

    def confirmSetModelData(self, editor: ScoreEditorDelegateWrapper):
        return editor.triggerValidateMessageBox()

    def setModelData(
        self,
        editor: ScoreEditorDelegateWrapper,
        model: QAbstractItemModel,
        index: QModelIndex,
    ):
        ...
