import dataclasses
import json
from typing import overload

import structlog
from PySide6.QtCore import Property, QObject, QResource, Qt, Signal
from PySide6.QtGui import QGuiApplication, QPalette

from .material3 import Material3DynamicThemeImpl, Material3ThemeImpl
from .qml import ThemeQmlExposer
from .shared import CustomPalette, ThemeImpl, ThemeInfo, TThemeInfoCacheKey, _TScheme

QML_IMPORT_NAME = "internal.ui.theme"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0

_THEME_CACHES: dict[TThemeInfoCacheKey, ThemeImpl] = {}

logger: structlog.stdlib.BoundLogger = structlog.get_logger()


class ThemeManager(QObject):
    _void = Signal()
    themeChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self._qPalette = QPalette()
        self._customPalette: CustomPalette = ThemeImpl.DEFAULT_CUSTOM_PALETTE

        self._lastThemeInfo = ThemeImpl().info
        self._qmlExposer = ThemeQmlExposer(themeImpl=ThemeImpl())

        self._cacheMaterial3DynamicTheme(themeId="default")
        self._cacheMaterial3DynamicTheme(themeId="tempest")

        self._cacheMaterial3DynamicTheme(themeId="devilun")
        self._cacheMaterial3DynamicTheme(themeId="kupya")

        self.setTheme("material3-dynamic", "devilun")

    def getCurrentScheme(self) -> _TScheme:
        qApp: QGuiApplication = QGuiApplication.instance()  # pyright: ignore[reportAssignmentType]
        return (
            "dark"
            if qApp.styleHints().colorScheme() == Qt.ColorScheme.Dark
            else "light"
        )

    def _loadQResourceJson(self, resourcePath: str):
        resource = QResource(resourcePath)
        if not resource.isValid():
            raise ValueError(f"Resource {resourcePath!r} invalid")

        return json.loads(resource.uncompressedData().data().decode("utf-8"))

    def getMaterial3Theme(self, themeId: str, scheme: _TScheme) -> Material3ThemeImpl:
        themeData = self._loadQResourceJson(f":/themes/m3_{themeId}.json")
        return Material3ThemeImpl(themeData=themeData, scheme=scheme)

    def getMaterial3DynamicTheme(
        self, themeId: str, scheme: _TScheme
    ) -> Material3DynamicThemeImpl:
        themeData = self._loadQResourceJson(f":/themes/m3-dynamic_{themeId}.json")
        return Material3DynamicThemeImpl(themeData=themeData, scheme=scheme)

    def _cacheTheme(self, *, themeImpl: ThemeImpl):
        _THEME_CACHES[themeImpl.info.cacheKey()] = themeImpl
        logger.debug("Theme %r cached", themeImpl.info)

    def _getCachedTheme(self, *, key: TThemeInfoCacheKey):
        cachedTheme = _THEME_CACHES.get(key)
        if cachedTheme is None:
            raise KeyError(f"Theme {key!r} not cached")
        return cachedTheme

    def _cacheMaterial3Theme(self, *, themeId: str):
        self._cacheTheme(
            themeImpl=self.getMaterial3Theme(themeId=themeId, scheme="light"),
        )
        self._cacheTheme(
            themeImpl=self.getMaterial3Theme(themeId=themeId, scheme="dark"),
        )

    def _cacheMaterial3DynamicTheme(self, *, themeId: str):
        self._cacheTheme(
            themeImpl=self.getMaterial3DynamicTheme(themeId=themeId, scheme="light")
        )
        self._cacheTheme(
            themeImpl=self.getMaterial3DynamicTheme(themeId=themeId, scheme="dark")
        )

    @overload
    def setTheme(self, *, themeInfo: ThemeInfo): ...

    @overload
    def setTheme(
        self, themeSeries: str, themeId: str, scheme: _TScheme | None = None, /
    ): ...

    def setTheme(self, *args, **kwargs):
        if "themeInfo" in kwargs:
            cacheKey = kwargs["themeInfo"].cacheKey()
        elif 2 <= len(args) <= 3:
            themeSeries = args[0]
            themeId = args[1]
            schemeArg = args[2] if len(args) > 2 else None
            scheme = schemeArg or self.getCurrentScheme()

            cacheKey: TThemeInfoCacheKey = (themeSeries, themeId, scheme)
        else:
            raise TypeError("Invalid setTheme() call")

        logger.debug("Preparing to set theme %r", cacheKey)

        cachedTheme = self._getCachedTheme(key=cacheKey)

        self._qPalette = cachedTheme.qPalette
        self._customPalette = cachedTheme.customPalette
        self._lastThemeInfo = cachedTheme.info
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
    def customPalette(self) -> CustomPalette:
        return self._customPalette

    @Property(ThemeQmlExposer, notify=themeChanged)
    def qmlExposer(self) -> ThemeQmlExposer:
        return self._qmlExposer
