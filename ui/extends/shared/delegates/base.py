from enum import IntEnum
from typing import Callable, Literal

from PySide6.QtCore import QModelIndex, QPoint, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QFontMetrics, QLinearGradient, QPainter
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem


class TextSegmentDelegateVerticalAlign(IntEnum):
    Top = 0
    Middle = 1
    Bottom = 2


class TextSegmentDelegate(QStyledItemDelegate):
    VerticalPadding = 3
    HorizontalPadding = 5

    TextRole = 3375
    ColorRole = TextRole + 1
    BrushRole = TextRole + 2
    GradientWrapperRole = TextRole + 3
    FontRole = TextRole + 20

    def __init__(self, parent=None):
        super().__init__(parent)

        # TODO: make this differ by index
        self.baseXOffset = 0
        self.baseYOffset = 0

        self.verticalAlign = TextSegmentDelegateVerticalAlign.Middle

    def setVerticalAlign(self, align: Literal["top", "middle", "bottom"]):
        if not isinstance(align, str) and align not in ["top", "middle", "bottom"]:
            raise ValueError(
                "TextSegment only supports top/middle/bottom vertical aligning."
            )

        if align == "top":
            self.verticalAlign = TextSegmentDelegateVerticalAlign.Top
        elif align == "middle":
            self.verticalAlign = TextSegmentDelegateVerticalAlign.Middle
        elif align == "bottom":
            self.verticalAlign = TextSegmentDelegateVerticalAlign.Bottom

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

    def baseX(self, option: QStyleOptionViewItem, index: QModelIndex):
        return option.rect.x() + self.HorizontalPadding + self.baseXOffset

    def baseY(self, option: QStyleOptionViewItem, index: QModelIndex):
        baseY = option.rect.y() + self.VerticalPadding + self.baseYOffset
        if self.verticalAlign != TextSegmentDelegateVerticalAlign.Top:
            paintAreaSize: QSize = option.rect.size()
            delegateSize = self.sizeHint(option, index)
            if self.verticalAlign == TextSegmentDelegateVerticalAlign.Middle:
                baseY += round((paintAreaSize.height() - delegateSize.height()) / 2)
            elif self.verticalAlign == TextSegmentDelegateVerticalAlign.Bottom:
                baseY += paintAreaSize.height() - delegateSize.height()
        return baseY

    def textMaxWidth(self, option: QStyleOptionViewItem, index: QModelIndex):
        return option.rect.width() - (2 * self.HorizontalPadding) - self.baseXOffset

    def paint(
        self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex
    ):
        self.initStyleOption(option, index)

        baseX = self.baseX(option, index)
        baseY = self.baseY(option, index)
        maxWidth = self.textMaxWidth(option, index)

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
                if font := textFrag.get(self.FontRole):
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
