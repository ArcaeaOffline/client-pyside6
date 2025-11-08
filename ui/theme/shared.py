from dataclasses import dataclass
from typing import Literal, TypedDict

from PySide6.QtGui import QColor, QPalette


class _TCustomPalette(TypedDict):
    primary: QColor
    success: QColor
    error: QColor

    toolTipBase: QColor
    toolTipText: QColor


_TScheme = Literal["light", "dark"]

TThemeInfoCacheKey = tuple[str, str, _TScheme]


@dataclass
class ThemeInfo:
    series: str
    id: str
    name: str
    scheme: _TScheme

    def cacheKey(self) -> TThemeInfoCacheKey:
        return (self.series, self.id, self.scheme)


class ThemeImpl:
    DEFAULT_CUSTOM_PALETTE: _TCustomPalette = {
        "primary": QColor.fromString("#616161"),
        "success": QColor.fromString("#616161"),
        "error": QColor.fromString("#616161"),
        "toolTipBase": QColor.fromString("#616161"),
        "toolTipText": QColor.fromString("#616161"),
    }

    @property
    def info(self) -> ThemeInfo:
        return ThemeInfo(
            series="placeholder",
            id="placeholder",
            name="placeholder",
            scheme="dark",
        )

    @property
    def qPalette(self) -> QPalette:
        return QPalette()

    @property
    def customPalette(self) -> _TCustomPalette:
        return self.DEFAULT_CUSTOM_PALETTE  # pyright: ignore[reportReturnType]
