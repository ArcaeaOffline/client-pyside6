from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class ElidedLabel(QLabel):
    """
    Adapted from https://wiki.qt.io/Elided_Label
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__elideMode: Qt.TextElideMode = Qt.TextElideMode.ElideNone
        self.__cachedElidedText = ""
        self.__cachedText = ""

    def elideMode(self):
        return self.__elideMode

    def setElideMode(self, mode):
        self.__elideMode = mode
        self.__cachedText = ""
        self.update()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.__cachedText = ""

    def paintEvent(self, event) -> None:
        if self.__elideMode == Qt.TextElideMode.ElideNone:
            return super().paintEvent(event)

        self.updateCachedTexts()
        super().setText(self.__cachedElidedText)
        super().paintEvent(event)
        super().setText(self.__cachedText)

    def updateCachedTexts(self):
        text = self.text()
        if self.__cachedText == text:
            return
        self.__cachedText = text
        fontMetrics = self.fontMetrics()
        self.__cachedElidedText = fontMetrics.elidedText(
            self.text(), self.__elideMode, self.width(), Qt.TextFlag.TextShowMnemonic
        )
        # make sure to show at least the first character
        if self.__cachedText:
            firstChar = f"{self.__cachedText[0]}..."
            self.setMinimumWidth(fontMetrics.horizontalAdvance(firstChar) + 1)
