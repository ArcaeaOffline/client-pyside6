from dataclasses import dataclass, field
from typing import Literal

from PySide6.QtGui import QColor, QPalette


@dataclass(kw_only=True)
class CustomPalette:
    primary: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))
    secondary: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))
    tertiary: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))
    success: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))
    error: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))

    toolTipBase: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))
    toolTipText: QColor = field(default_factory=lambda: QColor.fromRgb(0x616161))

    past: QColor = field(default_factory=lambda: QColor.fromRgb(0x5CBAD3))
    present: QColor = field(default_factory=lambda: QColor.fromRgb(0x829438))
    future: QColor = field(default_factory=lambda: QColor.fromRgb(0x913A79))
    beyond: QColor = field(default_factory=lambda: QColor.fromRgb(0xBF0D25))
    eternal: QColor = field(default_factory=lambda: QColor.fromRgb(0x8B77A4))
    pure: QColor = field(default_factory=lambda: QColor.fromRgb(0xF22EC6))
    far: QColor = field(default_factory=lambda: QColor.fromRgb(0xFF9028))
    lost: QColor = field(default_factory=lambda: QColor.fromRgb(0xFF0C43))


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
    DEFAULT_CUSTOM_PALETTE: CustomPalette = CustomPalette()

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
    def customPalette(self) -> CustomPalette:
        return self.DEFAULT_CUSTOM_PALETTE  # pyright: ignore[reportReturnType]
