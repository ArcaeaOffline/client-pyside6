import dataclasses
import json
from typing import overload

import structlog
from PySide6.QtCore import Property, QObject, QResource, Qt, Signal
from PySide6.QtGui import QColor, QGuiApplication, QPalette

from .material3 import Material3DynamicThemeImpl, Material3ThemeImpl
from .qml import ThemeQmlExposer
from .shared import ThemeImpl, ThemeInfo, _TCustomPalette, _TScheme

QML_IMPORT_NAME = "internal.ui.theme"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0

_THEME_CACHES: dict[ThemeInfo, ThemeImpl] = {}

logger: structlog.stdlib.BoundLogger = structlog.get_logger()


class ThemeManager(QObject):
    _void = Signal()
    themeChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self._qPalette = QPalette()
        self._customPalette: _TCustomPalette = {
            "primary": QColor.fromString("#616161"),
            "success": QColor.fromString("#616161"),
            "error": QColor.fromString("#616161"),
        }

        self._lastThemeInfo = ThemeInfo(
            series="material3",
            name="default",
            scheme=self.getCurrentScheme(),
        )
        self._qmlExposer = ThemeQmlExposer(themeImpl=ThemeImpl())

        self._cacheMaterial3Theme(themeName="default", scheme="light")
        self._cacheMaterial3Theme(themeName="default", scheme="dark")
        self._cacheMaterial3Theme(themeName="tempest", scheme="light")
        self._cacheMaterial3Theme(themeName="tempest", scheme="dark")

        self._cacheMaterial3DynamicTheme(themeName="default", scheme="light")
        self._cacheMaterial3DynamicTheme(themeName="default", scheme="dark")
        self._cacheMaterial3DynamicTheme(themeName="tempest", scheme="light")
        self._cacheMaterial3DynamicTheme(themeName="tempest", scheme="dark")

        self.setTheme("material3-dynamic", "default")

    def getCurrentScheme(self) -> _TScheme:
        qApp: QGuiApplication = QGuiApplication.instance()  # pyright: ignore[reportAssignmentType]
        return (
            "dark"
            if qApp.styleHints().colorScheme() == Qt.ColorScheme.Dark
            else "light"
        )

    def getMaterial3Theme(self, themeName: str, scheme: _TScheme) -> Material3ThemeImpl:
        themeDataResource = QResource(f":/themes/{themeName}.json")
        if not themeDataResource.isValid():
            raise ValueError(f"Material3 theme {themeName!r} not found")

        themeData = json.loads(
            themeDataResource.uncompressedData().data().decode("utf-8")
        )

        return Material3ThemeImpl(themeData=themeData, scheme=scheme)

    def getMaterial3DynamicTheme(
        self, themeName: str, scheme: _TScheme
    ) -> Material3DynamicThemeImpl:
        themeDataResource = QResource(f":/themes/{themeName}.json")
        if not themeDataResource.isValid():
            raise ValueError(f"Material3 theme {themeName!r} not found")

        themeData = json.loads(
            themeDataResource.uncompressedData().data().decode("utf-8")
        )

        return Material3DynamicThemeImpl(
            sourceColorHex=themeData["seed"],
            scheme=scheme,
            name=themeName,
        )

    def _cacheTheme(self, *, themeImpl: ThemeImpl):
        _THEME_CACHES[themeImpl.info] = themeImpl
        logger.debug("Theme %r cached", themeImpl.info)

    def _getCachedTheme(self, *, themeInfo: ThemeInfo):
        cachedTheme = _THEME_CACHES.get(themeInfo)
        if cachedTheme is None:
            raise KeyError(f"Theme {themeInfo!r} not cached")
        return cachedTheme

    def _cacheMaterial3Theme(self, *, themeName: str, scheme: _TScheme):
        self._cacheTheme(
            themeImpl=self.getMaterial3Theme(themeName=themeName, scheme=scheme),
        )

    def _cacheMaterial3DynamicTheme(self, *, themeName: str, scheme: _TScheme):
        self._cacheTheme(
            themeImpl=self.getMaterial3DynamicTheme(themeName=themeName, scheme=scheme)
        )

    @overload
    def setTheme(self, *, themeInfo: ThemeInfo): ...

    @overload
    def setTheme(
        self, themeSeries: str, themeName: str, scheme: _TScheme | None = None, /
    ): ...

    def setTheme(self, *args, **kwargs):
        if "themeInfo" in kwargs:
            themeInfo = kwargs["themeInfo"]
        elif 2 <= len(args) <= 3:
            themeSeries = args[0]
            themeName = args[1]
            schemeArg = args[2] if len(args) > 2 else None
            scheme = schemeArg or self.getCurrentScheme()

            themeInfo = ThemeInfo(series=themeSeries, name=themeName, scheme=scheme)
        else:
            raise TypeError("Invalid setTheme() call")

        logger.debug("Preparing to set theme %r", themeInfo)

        cachedTheme = self._getCachedTheme(themeInfo=themeInfo)

        self._qPalette = cachedTheme.qPalette
        self._customPalette = cachedTheme.customPalette
        self._lastThemeInfo = themeInfo
        self._qmlExposer.themeImpl = cachedTheme

        self.themeChanged.emit()

    def updateTheme(self, scheme: _TScheme | None = None):
        themeInfo = dataclasses.replace(self._lastThemeInfo)  # make a copy
        scheme = scheme or self.getCurrentScheme()
        themeInfo.scheme = scheme

        self.setTheme(themeInfo=themeInfo)

    @Property(QPalette, notify=themeChanged)
    def qPalette(self) -> QPalette:
        return self._qPalette

    @Property(dict, notify=themeChanged)
    def customPalette(self) -> _TCustomPalette:
        return self._customPalette

    @Property(ThemeQmlExposer, notify=themeChanged)
    def qmlExposer(self) -> ThemeQmlExposer:
        return self._qmlExposer
