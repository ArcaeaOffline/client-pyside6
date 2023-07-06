from typing import Callable

from PySide6.QtCore import QEvent, QModelIndex, QObject, QPoint, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QFontMetrics, QLinearGradient, QPainter
from PySide6.QtWidgets import QApplication, QStyledItemDelegate, QStyleOptionViewItem


class TextSegmentDelegate(QStyledItemDelegate):
    VerticalPadding = 3
    HorizontalPadding = 5

    TextRole = 3375
    ColorRole = TextRole + 1
    BrushRole = TextRole + 2
    GradientWrapperRole = TextRole + 3
    FontRole = TextRole + 20

    def getTextSegments(
        self, index: QModelIndex, option
    ) -> list[
        list[
            dict[
                int,
                str
                | QColor
                | QBrush
                | Callable[[float, float, float, float], QLinearGradient]
                | QFont,
            ]
        ]
    ]:
        return []

    def sizeHint(self, option, index) -> QSize:
        width = 0
        height = self.VerticalPadding
        fm: QFontMetrics = option.fontMetrics
        for line in self.getTextSegments(index, option):
            lineWidth = 4 * self.HorizontalPadding
            lineHeight = 0
            for textFrag in line:
                font = textFrag.get(self.FontRole)
                _fm = QFontMetrics(font) if font else fm
                text = textFrag[self.TextRole]
                textWidth = _fm.horizontalAdvance(text)
                textHeight = _fm.height()
                lineWidth += textWidth
                lineHeight = max(lineHeight, textHeight)
            width = max(lineWidth, width)
            height += lineHeight + self.VerticalPadding
        return QSize(width, height)

    def paint(
        self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex
    ):
        self.initStyleOption(option, index)
        # draw text only
        baseX = option.rect.x() + self.HorizontalPadding
        baseY = option.rect.y() + self.VerticalPadding
        maxWidth = option.rect.width() - (2 * self.HorizontalPadding)
        fm: QFontMetrics = option.fontMetrics
        painter.save()
        for line in self.getTextSegments(index, option):
            lineBaseX = baseX
            lineBaseY = baseY
            lineHeight = 0
            for textFrag in line:
                painter.save()
                # elide text, get font values
                text = textFrag[self.TextRole]
                fragMaxWidth = maxWidth - (lineBaseX - baseX)
                font = textFrag.get(self.FontRole)
                if font:
                    painter.setFont(font)
                    _fm = QFontMetrics(font)
                else:
                    _fm = fm
                lineHeight = max(lineHeight, _fm.height())
                elidedText = _fm.elidedText(
                    text, Qt.TextElideMode.ElideRight, fragMaxWidth
                )

                # confirm proper color
                brush = textFrag.get(self.BrushRole)
                gradientWrapper = textFrag.get(self.GradientWrapperRole)
                color = textFrag.get(self.ColorRole)
                pen = painter.pen()
                if brush:
                    pen.setBrush(brush)
                elif gradientWrapper:
                    gradient = gradientWrapper(
                        lineBaseX,
                        lineBaseY + lineHeight - _fm.height(),
                        fragMaxWidth,
                        _fm.height(),
                    )
                    pen.setBrush(gradient)
                elif color:
                    pen.setColor(color)
                painter.setPen(pen)

                painter.drawText(
                    QPoint(lineBaseX, lineBaseY + lineHeight - _fm.descent()),
                    elidedText,
                )
                painter.restore()

                # if text elided, skip to next line
                # remember to add height before skipping
                if _fm.boundingRect(text).width() >= fragMaxWidth:
                    break
                lineBaseX += _fm.horizontalAdvance(elidedText)

            baseY += lineHeight + self.VerticalPadding
        painter.restore()

    def super_styledItemDelegate_paint(self, painter, option, index):
        return super().paint(painter, option, index)


class NoCommitWhenFocusOutEventFilter(QObject):
    """
    --DEPRECATED--

    The default QAbstractItemDelegate implementation has a private function
    `editorEventFilter()`, when editor sends focusOut/hide event, it emits the
    `commitData(editor)` signal. We don't want this since we need to validate
    the input, so we filter the event out and handle it by ourselves.

    Reimplement `checkIsEditor(self, val) -> bool` to ensure this filter is
    working. The default implementation always return `False`.
    """

    def checkIsEditor(self, val) -> bool:
        return False

    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if self.checkIsEditor(object) and event.type() in [
            QEvent.Type.FocusOut,
            QEvent.Type.Hide,
        ]:
            widget = QApplication.focusWidget()
            while widget:
                # check if focus changed into editor's child
                if self.checkIsEditor(widget):
                    return False
                widget = widget.parentWidget()

            object.hide()
            object.deleteLater()
            return True
        return False
