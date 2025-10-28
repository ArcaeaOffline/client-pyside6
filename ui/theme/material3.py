from typing import TypedDict

from materialyoucolor.blend import Blend
from materialyoucolor.dynamiccolor.contrast_curve import ContrastCurve
from materialyoucolor.dynamiccolor.dynamic_color import DynamicColor, FromPaletteOptions
from materialyoucolor.dynamiccolor.material_dynamic_colors import MaterialDynamicColors
from materialyoucolor.hct import Hct
from materialyoucolor.palettes.tonal_palette import TonalPalette
from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot
from PySide6.QtGui import QColor, QPalette

from .shared import ThemeImpl, ThemeInfo, _TCustomPalette, _TScheme


class _M3ThemeDataExtendedColorItem(TypedDict):
    name: str
    color: str
    description: str
    harmonized: bool


_M3ThemeDataSchemes = TypedDict(
    "_M3ThemeDataSchemes",
    {
        "light": dict[str, str],
        "light-medium-contrast": dict[str, str],
        "light-high-contrast": dict[str, str],
        "dark": dict[str, str],
        "dark-medium-contrast": dict[str, str],
        "dark-high-contrast": dict[str, str],
    },
)

_M3ThemeDataPalettes = TypedDict(
    "_M3ThemeDataPalettes",
    {
        "primary": dict[str, str],
        "secondary": dict[str, str],
        "tertiary": dict[str, str],
        "neutral": dict[str, str],
        "neutral-variant": dict[str, str],
    },
)


class _M3ThemeData(TypedDict):
    name: str
    description: str
    seed: str
    coreColors: dict[str, str]
    extendedColors: list[_M3ThemeDataExtendedColorItem]
    schemes: _M3ThemeDataSchemes
    palettes: _M3ThemeDataPalettes


def _hexToHct(hexColor: str) -> Hct:
    pureHexPart = hexColor[1:] if hexColor.startswith("#") else hexColor
    return Hct.from_int(int(f"0xff{pureHexPart}", 16))


def _hctToQColor(hct: Hct) -> QColor:
    return QColor.fromRgba(hct.to_int())


class Material3ThemeImpl(ThemeImpl):
    COLOR_ROLE_MAPPING: dict[QPalette.ColorRole, str] = {
        QPalette.ColorRole.Window: "surface",
        QPalette.ColorRole.WindowText: "onSurface",
        QPalette.ColorRole.Base: "surfaceContainer",
        QPalette.ColorRole.AlternateBase: "surfaceContainerHighest",
        QPalette.ColorRole.ToolTipBase: "secondaryContainer",
        QPalette.ColorRole.ToolTipText: "onSecondaryContainer",
        QPalette.ColorRole.PlaceholderText: "inverseSurface",
        QPalette.ColorRole.Text: "onSurface",
        QPalette.ColorRole.Button: "primaryContainer",
        QPalette.ColorRole.ButtonText: "onPrimaryContainer",
        QPalette.ColorRole.BrightText: "onSecondary",
        QPalette.ColorRole.Light: "surfaceContainerLowest",
        QPalette.ColorRole.Midlight: "surfaceContainerLow",
        QPalette.ColorRole.Dark: "inverseSurface",
        QPalette.ColorRole.Mid: "surfaceContainer",
        QPalette.ColorRole.Shadow: "shadow",
        QPalette.ColorRole.Highlight: "primary",
        QPalette.ColorRole.Accent: "primary",
        QPalette.ColorRole.HighlightedText: "onPrimary",
        QPalette.ColorRole.Link: "tertiary",
        QPalette.ColorRole.LinkVisited: "tertiaryContainer",
    }

    def __init__(self, *, themeData: _M3ThemeData, scheme: _TScheme):
        self.themeData = themeData
        self.scheme: _TScheme = scheme

        if self.themeData["schemes"].get(scheme) is None:
            raise ValueError(f"Invalid scheme: {scheme}")

    def _findExtendedColor(
        self, colorName: str
    ) -> _M3ThemeDataExtendedColorItem | None:
        return next(
            (it for it in self.themeData["extendedColors"] if it["name"] == colorName),
            None,
        )

    @property
    def info(self):
        return ThemeInfo(
            series="material3",
            name=self.themeData["name"],
            scheme=self.scheme,
        )

    @property
    def qPalette(self) -> QPalette:
        qPalette = QPalette()

        for role, name in self.COLOR_ROLE_MAPPING.items():
            color = QColor.fromString(self.themeData["schemes"][self.scheme][name])
            qPalette.setColor(role, color)

        return qPalette

    @property
    def customPalette(self) -> _TCustomPalette:
        primaryHct = _hexToHct(self.themeData["schemes"][self.scheme]["primary"])

        successColorItem = self._findExtendedColor("Success")
        if successColorItem is None:
            raise Exception("Success color not found")
        successHct = _hexToHct(successColorItem["color"])

        successHarmonizedHct = Hct.from_int(
            Blend.harmonize(successHct.to_int(), primaryHct.to_int())
        )

        return {
            "primary": _hctToQColor(primaryHct),
            "success": _hctToQColor(successHarmonizedHct),
            "error": QColor.fromString(self.themeData["schemes"][self.scheme]["error"]),
        }


class Material3DynamicThemeImpl(ThemeImpl):
    ACTIVE_COLOR_ROLE_MAPPING: dict[QPalette.ColorRole, DynamicColor] = {
        QPalette.ColorRole.Window: MaterialDynamicColors.surface,
        QPalette.ColorRole.WindowText: MaterialDynamicColors.onSurface,
        QPalette.ColorRole.Base: MaterialDynamicColors.surfaceContainer,
        QPalette.ColorRole.AlternateBase: MaterialDynamicColors.surfaceContainerHighest,
        QPalette.ColorRole.ToolTipBase: MaterialDynamicColors.secondaryContainer,
        QPalette.ColorRole.ToolTipText: MaterialDynamicColors.onSecondaryContainer,
        QPalette.ColorRole.PlaceholderText: MaterialDynamicColors.inverseSurface,
        QPalette.ColorRole.Text: MaterialDynamicColors.onSurface,
        QPalette.ColorRole.Button: MaterialDynamicColors.primaryContainer,
        QPalette.ColorRole.ButtonText: MaterialDynamicColors.onPrimaryContainer,
        QPalette.ColorRole.BrightText: MaterialDynamicColors.onSecondary,
        QPalette.ColorRole.Light: MaterialDynamicColors.surfaceContainerLowest,
        QPalette.ColorRole.Midlight: MaterialDynamicColors.surfaceContainerLow,
        QPalette.ColorRole.Dark: MaterialDynamicColors.inverseSurface,
        QPalette.ColorRole.Mid: MaterialDynamicColors.surfaceContainer,
        QPalette.ColorRole.Shadow: MaterialDynamicColors.shadow,
        QPalette.ColorRole.Highlight: MaterialDynamicColors.primary,
        QPalette.ColorRole.Accent: MaterialDynamicColors.primary,
        QPalette.ColorRole.HighlightedText: MaterialDynamicColors.onPrimary,
        QPalette.ColorRole.Link: MaterialDynamicColors.tertiary,
        QPalette.ColorRole.LinkVisited: MaterialDynamicColors.tertiaryContainer,
    }

    EXTENDED_COLORS = {
        "success": "#00c555",
    }

    def __init__(self, sourceColorHex: str, scheme: _TScheme, *, name: str):
        self.material3Scheme = SchemeTonalSpot(
            _hexToHct(sourceColorHex),
            is_dark=scheme == "dark",
            contrast_level=0.0,
        )
        self.name = name

    @property
    def info(self):
        return ThemeInfo(
            series="material3-dynamic",
            name=self.name,
            scheme="dark" if self.material3Scheme.is_dark else "light",
        )

    @property
    def qPalette(self) -> QPalette:
        qPalette = QPalette()

        for role, dynamicColor in self.ACTIVE_COLOR_ROLE_MAPPING.items():
            hct = dynamicColor.get_hct(self.material3Scheme)
            qColor = QColor.fromRgba(hct.to_int())
            qPalette.setColor(QPalette.ColorGroup.Active, role, qColor)

            # TODO: disabled palette seems to work only after a theme reload, needs further investigation
            if role in [QPalette.ColorRole.Button, QPalette.ColorRole.ButtonText]:
                disabledHct = Hct.from_hct(hct.hue, 1.0, hct.tone)
                disabledQColor = QColor.fromRgba(disabledHct.to_int())
                qPalette.setColor(QPalette.ColorGroup.Disabled, role, disabledQColor)

        return qPalette

    @property
    def customPalette(self) -> _TCustomPalette:
        primaryHct = MaterialDynamicColors.primary.get_hct(self.material3Scheme)
        errorHct = MaterialDynamicColors.error.get_hct(self.material3Scheme)

        extendedPalettes: dict[str, DynamicColor] = {}
        for colorName, colorHex in self.EXTENDED_COLORS.items():
            colorHct = _hexToHct(colorHex)
            colorHarmonized = Blend.harmonize(colorHct.to_int(), primaryHct.to_int())

            colorTonalPalette = TonalPalette.from_int(colorHarmonized)

            colorSurfacePaletteOptions = DynamicColor.from_palette(
                FromPaletteOptions(
                    name=f"{colorName}_container",
                    palette=lambda s: colorTonalPalette,
                    tone=lambda s: 30 if s.is_dark else 90,
                    is_background=True,
                    background=lambda s: MaterialDynamicColors.highestSurface(s),
                    contrast_curve=ContrastCurve(1, 1, 3, 4.5),
                )
            )

            extendedPalettes[colorName] = DynamicColor.from_palette(
                FromPaletteOptions(
                    name=colorName,  # pyright: ignore[reportArgumentType]
                    palette=lambda s: colorTonalPalette,
                    tone=lambda s: 80 if s.is_dark else 40,  # pyright: ignore[reportArgumentType]
                    is_background=False,  # pyright: ignore[reportArgumentType]
                    background=lambda s: MaterialDynamicColors.highestSurface(s),
                    contrast_curve=ContrastCurve(3, 4.5, 7, 7),
                )
            )

        return {
            "primary": _hctToQColor(primaryHct),
            "success": _hctToQColor(
                extendedPalettes["success"].get_hct(self.material3Scheme)
            ),
            "error": _hctToQColor(errorHct),
        }
