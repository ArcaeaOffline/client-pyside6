from typing import TypedDict

from .shared import _TScheme

# region material3


class TMaterial3ThemeDataExtendedColorItem(TypedDict):
    name: str
    color: str
    description: str
    harmonized: bool


TMaterial3ThemeDataSchemes = TypedDict(
    "TMaterial3ThemeDataSchemes",
    {
        "light": dict[str, str],
        "light-medium-contrast": dict[str, str],
        "light-high-contrast": dict[str, str],
        "dark": dict[str, str],
        "dark-medium-contrast": dict[str, str],
        "dark-high-contrast": dict[str, str],
    },
)

TMaterial3ThemeDataPalettes = TypedDict(
    "TMaterial3ThemeDataPalettes",
    {
        "primary": dict[str, str],
        "secondary": dict[str, str],
        "tertiary": dict[str, str],
        "neutral": dict[str, str],
        "neutral-variant": dict[str, str],
    },
)


class TMaterial3ThemeData(TypedDict):
    id: str
    name: str
    description: str
    seed: str
    coreColors: dict[str, str]
    extendedColors: list[TMaterial3ThemeDataExtendedColorItem]
    schemes: TMaterial3ThemeDataSchemes
    palettes: TMaterial3ThemeDataPalettes


# endregion

# region material3-dynamic


class TMaterial3DynamicThemeDataColors(TypedDict):
    primary: str
    secondary: str | None
    tertiary: str | None


class TMaterial3DynamicThemeDataOptions(TypedDict):
    forceScheme: _TScheme | None


class TMaterial3DynamicThemeData(TypedDict):
    id: str
    name: str
    colors: TMaterial3DynamicThemeDataColors
    options: TMaterial3DynamicThemeDataOptions


# endregion
