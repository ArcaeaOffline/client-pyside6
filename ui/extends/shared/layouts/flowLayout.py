# Adapted from https://doc.qt.io/qt-6/qtwidgets-layouts-flowlayout-example.html

from PySide6.QtCore import QPoint, QRect, QSize, Qt
from PySide6.QtWidgets import QLayout, QLayoutItem, QSizePolicy, QStyle, QWidget


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, hSpacing=0, vSpacing=0):
        super().__init__(parent)
        self.hSpace = hSpacing
        self.vSpace = vSpacing
        self.setContentsMargins(margin, margin, margin, margin)
        self.itemList: list[QLayoutItem] = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            del item
            item = self.takeAt(0)

    def addItem(self, item: QLayoutItem):
        self.itemList.append(item)

    def horizontalSpacing(self):
        return (
            self.hSpace
            if self.hSpace >= 0
            else self.smartSpacing(QStyle.PixelMetric.PM_LayoutHorizontalSpacing)
        )

    def verticalSpacing(self):
        return (
            self.vSpace
            if self.vSpace >= 0
            else self.smartSpacing(QStyle.PixelMetric.PM_LayoutVerticalSpacing)
        )

    def count(self):
        return len(self.itemList)

    def itemAt(self, index: int):
        return self.itemList[index] if 0 <= index < len(self.itemList) else None

    def takeAt(self, index):
        return self.itemList.pop(index) if 0 <= index < len(self.itemList) else None

    # Qt::Orientations FlowLayout::expandingDirections() const
    # {
    #     return { };
    # }
    def expandingDirections(self):
        return Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width: int):
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect: QRect):
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margins = self.contentsMargins()
        size += QSize(
            margins.left() + margins.right(), margins.top() + margins.bottom()
        )
        return size

    def doLayout(self, rect: QRect, testOnly: bool):
        margins = self.contentsMargins()
        left = margins.left()
        top = margins.top()
        right = margins.right()
        bottom = margins.bottom()
        effectiveRect = rect.adjusted(+left, +top, -right, -bottom)
        x = effectiveRect.x()
        y = effectiveRect.y()
        lineHeight = 0
        for item in self.itemList:
            widget = item.widget()
            spaceX = self.horizontalSpacing()
            if spaceX == -1:
                spaceX = widget.style().layoutSpacing(
                    QSizePolicy.ControlType.PushButton,
                    QSizePolicy.ControlType.PushButton,
                )
            spaceY = self.verticalSpacing()
            if spaceY == -1:
                spaceY = widget.style().layoutSpacing(
                    QSizePolicy.ControlType.PushButton,
                    QSizePolicy.ControlType.PushButton,
                )

            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > effectiveRect.right() and lineHeight > 0:
                x = effectiveRect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())
        return y + lineHeight - rect.y() + bottom

    def smartSpacing(self, pm: QStyle.PixelMetric):
        parent = self.parent()
        if not parent:
            return -1
        elif parent.isWidgetType():
            parent: QWidget
            return parent.style().pixelMetric(pm, None, parent)
        else:
            parent: QLayout
            return parent.spacing()
