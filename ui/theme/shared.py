from dataclasses import dataclass
from typing import Literal, TypedDict

from PySide6.QtGui import QColor, QPalette


class _TCustomPalette(TypedDict):
    primary: QColor
    success: QColor
    error: QColor


_TScheme = Literal["light", "dark"]


@dataclass
class ThemeInfo:
    series: str
    name: str
    scheme: _TScheme

    def __hash__(self) -> int:
        return hash((self.series, self.name, self.scheme))


class ThemeImpl:
    DEFAULT_CUSTOM_PALETTE = {
        "primary": QColor.fromString("#616161"),
        "success": QColor.fromString("#616161"),
        "error": QColor.fromString("#616161"),
    }

    @property
    def info(self) -> ThemeInfo:
        return ThemeInfo(series="placeholder", name="placeholder", scheme="dark")

    @property
    def qPalette(self) -> QPalette:
        return QPalette()

    @property
    def customPalette(self) -> _TCustomPalette:
        return self.DEFAULT_CUSTOM_PALETTE  # pyright: ignore[reportReturnType]
