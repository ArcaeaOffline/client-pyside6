from PySide6.QtGui import QFont

from .focusSelectAllLineEdit import FocusSelectAllLineEdit


class ArcaeaScoreLineEdit(FocusSelectAllLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        font = QFont("GeosansLight")
        font.setPointSize(14)
        font.setBold(True)
        font.setStyleStrategy(
            QFont.StyleStrategy.NoSubpixelAntialias
            | QFont.StyleStrategy.PreferAntialias
        )
        self.setFont(font)

        self.setInputMask("B9'999'999;_")

    def score(self) -> int | None:
        textWithoutMask = self.text().replace("'", "")
        return int(textWithoutMask) if textWithoutMask else None
