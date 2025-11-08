from materialyoucolor.blend import Blend
from materialyoucolor.dynamiccolor.contrast_curve import ContrastCurve
from materialyoucolor.dynamiccolor.dynamic_color import DynamicColor, FromPaletteOptions
from materialyoucolor.dynamiccolor.material_dynamic_colors import MaterialDynamicColors
from materialyoucolor.hct import Hct
from materialyoucolor.palettes.tonal_palette import TonalPalette
from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot
from PySide6.QtGui import QColor, QPalette

from .shared import ThemeImpl, ThemeInfo, _TCustomPalette, _TScheme
from .types import (
    TMaterial3DynamicThemeData,
    TMaterial3ThemeData,
    TMaterial3ThemeDataExtendedColorItem,
)


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

    def __init__(self, *, themeData: TMaterial3ThemeData, scheme: _TScheme):
        self.themeData = themeData
        self.scheme: _TScheme = scheme

        if self.themeData["schemes"].get(scheme) is None:
            raise ValueError(f"Invalid scheme: {scheme}")

    def _findExtendedColor(
        self, colorName: str
    ) -> TMaterial3ThemeDataExtendedColorItem | None:
        return next(
            (it for it in self.themeData["extendedColors"] if it["name"] == colorName),
            None,
        )

    @property
    def info(self):
        return ThemeInfo(
            series="material3",
            id=self.themeData["id"],
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
            "toolTipBase": self.qPalette.color(QPalette.ColorRole.ToolTipBase),
            "toolTipText": self.qPalette.color(QPalette.ColorRole.ToolTipText),
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

    def __init__(self, themeData: TMaterial3DynamicThemeData, scheme: _TScheme):
        force_scheme = themeData["options"].get("forceScheme")
        if force_scheme:
            is_dark = force_scheme == "dark"
        else:
            is_dark = scheme == "dark"

        # TODO: more elegant way?
        self.preferredScheme: _TScheme = scheme  # for theme caching
        self.actualScheme = "dark" if is_dark else "light"

        self.themeId = themeData["id"]
        self.themeName = themeData["name"]

        self.material3Scheme = SchemeTonalSpot(
            _hexToHct(themeData["colors"]["primary"]),
            is_dark=is_dark,
            contrast_level=0.0,
        )

        secondary_color = themeData["colors"].get("secondary")
        if secondary_color:
            self.material3Scheme.secondary_palette = TonalPalette.from_hct(
                _hexToHct(secondary_color)
            )

        tertiary_color = themeData["colors"].get("tertiary")
        if tertiary_color:
            self.material3Scheme.tertiary_palette = TonalPalette.from_hct(
                _hexToHct(tertiary_color)
            )

    @property
    def info(self):
        return ThemeInfo(
            series="material3-dynamic",
            id=self.themeId,
            name=self.themeName,
            scheme=self.preferredScheme,
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
            "toolTipBase": self.qPalette.color(QPalette.ColorRole.ToolTipBase),
            "toolTipText": self.qPalette.color(QPalette.ColorRole.ToolTipText),
        }
