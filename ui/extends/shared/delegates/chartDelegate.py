from arcaea_offline.models import Chart, Difficulty, Song
from arcaea_offline.utils.rating import rating_class_to_short_text, rating_class_to_text
from PIL import Image
from PySide6.QtCore import QModelIndex, QRect, Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QStyleOptionViewItem,
    QWidget,
)

from ui.extends.shared.data import Data
from ui.implements.components.chartSelector import ChartSelector

from ..utils import keepWidgetInScreen
from .base import TextSegmentDelegate


def chartToRichText(chart: Chart):
    if isinstance(chart, Chart):
        text = f"{chart.title} [{rating_class_to_short_text(chart.rating_class)}]"
        text += "<br>"
        text += f'<font color="gray">({chart.song_id}, {chart.set})</font>'
    else:
        text = "(unknown chart)"
    return text


class ChartSelectorDelegateWrapper(ChartSelector):
    accepted = Signal()
    rejected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.delegateHLine = QFrame(self)
        self.delegateHLine.setFrameShape(QFrame.Shape.HLine)
        self.delegateHLine.setFrameShadow(QFrame.Shadow.Plain)
        self.delegateHLine.setFixedHeight(5)
        self.mainVerticalLayout.insertWidget(0, self.delegateHLine)

        self.delegateHeader = QWidget(self)
        self.delegateHeaderHBoxLayout = QHBoxLayout(self.delegateHeader)
        self.delegateHeaderHBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.insertWidget(0, self.delegateHeader)

        self.editorLabel = QLabel(self)
        self.editorLabel.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.delegateHeaderHBoxLayout.addWidget(self.editorLabel)

        self.editorCommitButton = QPushButton("Commit", self.delegateHeader)
        self.editorCommitButton.clicked.connect(self.accepted)
        self.delegateHeaderHBoxLayout.addWidget(self.editorCommitButton)

        self.editorDiscardButton = QPushButton("Discard", self.delegateHeader)
        self.editorDiscardButton.clicked.connect(self.rejected)
        self.delegateHeaderHBoxLayout.addWidget(self.editorDiscardButton)

    def setText(self, chart: Chart, _extra: str = None):
        text = "Editing "
        text += _extra or ""
        text += "<br>"
        text += (
            chartToRichText(chart) if isinstance(chart, Chart) else "(unknown chart)"
        )
        self.editorLabel.setText(text)

    def validate(self):
        return isinstance(self.value(), Chart)


class ChartDelegate(TextSegmentDelegate):
    RatingClassColors = [
        QColor("#399bb2"),
        QColor("#809955"),
        QColor("#702d60"),
        QColor("#710f25"),
        QColor("#8b77a4"),
    ]
    ChartInvalidBackgroundColor = QColor("#e6a23c")

    def getChart(self, index: QModelIndex) -> Chart | None:
        return None

    def getSong(self, index: QModelIndex) -> Song | None:
        return None

    def getDifficulty(self, index: QModelIndex) -> Difficulty | None:
        return None

    def getTextSegments(self, index: QModelIndex, option):
        chart = self.getChart(index)
        song = self.getSong(index)
        difficulty = self.getDifficulty(index)

        chartValid = isinstance(chart, Chart)
        songValid = isinstance(song, Song)
        difficultyValid = isinstance(difficulty, Difficulty)

        if not chartValid and not songValid:
            return [
                [
                    {
                        self.TextRole: "Chart/Song not set",
                        self.ColorRole: QColor("#ff0000"),
                    }
                ]
            ]

        # get texts
        if chartValid:
            title = chart.title
        else:
            title = (
                difficulty.title if difficultyValid and difficulty.title else song.title
            )

        if chartValid and chart.constant is not None:
            chartConstantString = f"{chart.constant / 10:.1f}"
        elif difficultyValid:
            chartConstantString = str(difficulty.rating)
            if difficulty.rating_plus:
                chartConstantString += "+"
        else:
            chartConstantString = "?"

        if chartValid:
            ratingClass = chart.rating_class
        elif difficultyValid:
            ratingClass = difficulty.rating_class
        else:
            ratingClass = None

        ratingText = (
            f"{rating_class_to_text(ratingClass)} {chartConstantString}"
            if ratingClass is not None
            else "Unknown ?"
        )

        if chartValid:
            descText = f"({chart.song_id}, {chart.set})"
        else:
            descText = f"({song.id}, {song.set})"

        # get attributes
        ratingClassColor = (
            self.RatingClassColors[ratingClass] if ratingClass is not None else None
        )

        return [
            [
                {self.TextRole: str(title)},
            ],
            [
                {
                    self.TextRole: ratingText,
                    self.ColorRole: ratingClassColor,
                },
            ],
            [
                {
                    self.TextRole: descText,
                    self.ColorRole: option.widget.palette().placeholderText().color(),
                },
            ],
        ]

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        minWidth = size.height() + 2 * self.HorizontalPadding  # jacket size
        width = size.width() + self.HorizontalPadding + size.height()
        size.setWidth(max(minWidth, width))
        return size

    def paint(self, painter, option, index):
        option.text = ""

        data = Data()

        chart = self.getChart(index)
        song = self.getSong(index)
        difficulty = self.getDifficulty(index)

        if isinstance(chart, Chart):
            jacketPath = data.getJacketPath(chart)
        elif isinstance(song, Song):
            jacketPath = data.getJacketPath(song, difficulty)
        else:
            jacketPath = "__TEXT_ONLY__"

        if jacketPath == "__TEXT_ONLY__":
            self.setBaseXOffset(index, 0)
            super().paint(painter, option, index)
            return

        textsSizeHint = super().textsSizeHint(option, index)
        jacketSize = textsSizeHint.height()
        self.setBaseXOffset(index, self.HorizontalPadding + jacketSize)

        jacketSizeTuple = (jacketSize, jacketSize)
        if jacketPath:
            pixmap = (
                Image.open(str(jacketPath.resolve()))
                .resize(jacketSizeTuple, Image.BICUBIC)
                .toqpixmap()
            )
        else:
            pixmap = (
                Image.fromqpixmap(QPixmap(":/images/jacket-placeholder.png"))
                .resize(jacketSizeTuple, Image.BICUBIC)
                .toqpixmap()
            )

        pixmapAvailableWidth = option.rect.width() - self.HorizontalPadding
        pixmapAvailableHeight = option.rect.height()

        if pixmapAvailableWidth < jacketSize or pixmapAvailableHeight < jacketSize:
            cropRect = QRect(0, 0, pixmapAvailableWidth, pixmapAvailableHeight)
            pixmap = pixmap.copy(cropRect)

        painter.save()
        painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering, True)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        pixmapBaseY = self.baseY(option, index)
        painter.drawPixmap(
            option.rect.x() + self.HorizontalPadding,
            pixmapBaseY,
            pixmap,
        )
        painter.restore()
        super().paint(painter, option, index)

    def checkIsEditor(self, val):
        return isinstance(val, ChartSelectorDelegateWrapper)

    def _closeEditor(self):
        editor = self.sender()
        self.closeEditor.emit(editor)

    def _commitEditor(self):
        editor = self.sender()
        if editor.validate():
            confirm = QMessageBox.question(
                editor,
                "Confirm",
                f"Are you sure to change chart to<br><br>{chartToRichText(editor.value())}",
            )
            if confirm == QMessageBox.StandardButton.Yes:
                self.commitData.emit(editor)
                self.closeEditor.emit(editor)
        else:
            QMessageBox.critical(editor, "Invalid chart", "Cannot commit")

    def createEditor(
        self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex
    ) -> ChartSelectorDelegateWrapper:
        editor = ChartSelectorDelegateWrapper(parent)
        editor.setWindowFlag(Qt.WindowType.Sheet, True)
        editor.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        if isinstance(self.getChart(index), Chart):
            editor.setText(self.getChart(index))
        editor.move(parent.mapToGlobal(parent.pos()))
        editor.accepted.connect(self._commitEditor)
        editor.rejected.connect(self._closeEditor)
        return editor

    def updateEditorGeometry(self, editor: QWidget, option, index: QModelIndex) -> None:
        editor.move(editor.pos() + option.rect.topLeft())
        editor.setMaximumWidth(option.rect.width())

        keepWidgetInScreen(editor)

    def setEditorData(self, editor: ChartSelectorDelegateWrapper, index: QModelIndex):
        if self.checkIsEditor(editor) and isinstance(self.getChart(index), Chart):
            editor.selectChart(self.getChart(index))
        return super().setEditorData(editor, index)

    def setModelData(self, editor: ChartSelectorDelegateWrapper, model, index):
        ...
