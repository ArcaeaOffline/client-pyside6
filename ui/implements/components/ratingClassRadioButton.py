from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsColorizeEffect, QRadioButton

from core.color import mixColor

STYLESHEET = """
QRadioButton {{
  padding: 10px;
  background-color: qlineargradient(spread:pad, x1:0.7, y1:0.5, x2:1, y2:0.525, stop:0 {dark_color}, stop:1 {mid_color});
  color: {text_color};
}}

QRadioButton::indicator {{
  border: 2px solid palette(Window);
  width: 7px;
  height: 7px;
  border-radius: 0px;
}}

QRadioButton::indicator:unchecked {{
  background-color: palette(Window);
}}

QPushButton::indicator:checked {{
  background-color: {mid_color};
}}
"""


class RatingClassRadioButton(QRadioButton):
    def __init__(self, parent):
        super().__init__(parent)

        self.toggled.connect(self.updateCheckedEffect)

        self.grayscaleEffect = QGraphicsColorizeEffect(self)
        self.grayscaleEffect.setColor("#000000")

    def setColors(self, dark_color: QColor, text_color: QColor):
        self._dark_color = dark_color
        self._text_color = text_color
        self._mid_color = mixColor(dark_color, text_color, 0.616)
        self.updateEffects()

    def isColorsSet(self) -> bool:
        return (
            hasattr(self, "_dark_color")
            and hasattr(self, "_text_color")
            and hasattr(self, "_mid_color")
            and isinstance(self._dark_color, QColor)
            and isinstance(self._text_color, QColor)
            and isinstance(self._mid_color, QColor)
        )

    def setNormalStyleSheet(self):
        self.setStyleSheet(
            STYLESHEET.format(
                dark_color=self._dark_color.name(QColor.NameFormat.HexArgb),
                mid_color=self._mid_color.name(QColor.NameFormat.HexArgb),
                text_color=self._text_color.name(QColor.NameFormat.HexArgb),
            )
        )

    def setDisabledStyleSheet(self):
        self.setStyleSheet(
            STYLESHEET.format(
                dark_color="#282828",
                mid_color="#282828",
                text_color="#9e9e9e",
            ).replace("palette(Window)", "#333333")
        )

    @Slot()
    def updateEnabledEffect(self):
        if self.isColorsSet():
            if self.isEnabled():
                self.setNormalStyleSheet()
            else:
                self.setDisabledStyleSheet()

    @Slot()
    def updateCheckedEffect(self):
        if self.isColorsSet():
            if self.isEnabled():
                self.grayscaleEffect.setStrength(0.0 if self.isChecked() else 1.0)
                self.setGraphicsEffect(self.grayscaleEffect)

    @Slot()
    def updateEffects(self):
        self.updateCheckedEffect()
        self.updateEnabledEffect()

    def setChecked(self, arg__1: bool):
        super().setChecked(arg__1)
        self.updateEffects()

    def setEnabled(self, arg__1: bool):
        super().setEnabled(arg__1)
        self.updateEffects()
