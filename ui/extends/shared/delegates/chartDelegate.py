from arcaea_offline.models import Chart
from arcaea_offline.utils.rating import rating_class_to_short_text, rating_class_to_text
from PySide6.QtCore import QModelIndex, Qt, Signal
from PySide6.QtGui import QColor
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

from ui.implements.components.chartSelector import ChartSelector

from .base import TextSegmentDelegate


def chartToRichText(chart: Chart):
    if isinstance(chart, Chart):
        text = f"{chart.name_en} [{rating_class_to_short_text(chart.rating_class)}]"
        text += "<br>"
        text += f'<font color="gray">({chart.song_id}, {chart.package_id})</font>'
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
    ]
    ChartInvalidBackgroundColor = QColor("#e6a23c")

    def getChart(self, index: QModelIndex) -> Chart | None:
        return None

    def getTextSegments(self, index: QModelIndex, option):
        chart = self.getChart(index)
        if not isinstance(chart, Chart):
            return [
                [{self.TextRole: "Chart Invalid", self.ColorRole: QColor("#ff0000")}]
            ]

        return [
            [
                {self.TextRole: f"{chart.name_en}"},
            ],
            [
                {
                    self.TextRole: f"{rating_class_to_text(chart.rating_class)} {chart.rating / 10:.1f}",
                    self.ColorRole: self.RatingClassColors[chart.rating_class],
                },
            ],
            [
                {
                    self.TextRole: f"({chart.song_id}, {chart.package_id})",
                    self.ColorRole: option.widget.palette().placeholderText().color(),
                },
            ],
        ]

    def paintWarningBackground(self, index: QModelIndex) -> bool:
        return True

    def paint(self, painter, option, index):
        # draw chartInvalid warning background
        chart = self.getChart(index)
        if not isinstance(chart, Chart) and self.paintWarningBackground(index):
            painter.save()
            painter.setPen(Qt.PenStyle.NoPen)
            bgColor = QColor(self.ChartInvalidBackgroundColor)
            bgColor.setAlpha(50)
            painter.setBrush(bgColor)
            painter.drawRect(option.rect)
            painter.restore()
        option.text = ""
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
        if isinstance(self.getChart(index), Chart):
            editor = ChartSelectorDelegateWrapper(parent)
            editor.setWindowFlag(Qt.WindowType.Sheet, True)
            editor.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
            editor.setText(self.getChart(index))
            editor.move(parent.mapToGlobal(parent.pos()))
            editor.accepted.connect(self._commitEditor)
            editor.rejected.connect(self._closeEditor)
            return editor

    def updateEditorGeometry(self, editor: QWidget, option, index: QModelIndex) -> None:
        editor.move(editor.pos() + option.rect.topLeft())
        editor.setMaximumWidth(option.rect.width())

    def setEditorData(self, editor: ChartSelectorDelegateWrapper, index: QModelIndex):
        if self.checkIsEditor(editor) and isinstance(self.getChart(index), Chart):
            editor.selectChart(self.getChart(index))
        return super().setEditorData(editor, index)

    def setModelData(self, editor: ChartSelectorDelegateWrapper, model, index):
        ...
