from PySide6.QtCore import Property, QObject, Signal
from PySide6.QtGui import QColor

from .shared import ThemeImpl

QML_IMPORT_NAME = "internal.ui.theme"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0


class ThemeQmlExposer(QObject):
    themeChanged = Signal()

    def __init__(self, *, themeImpl: ThemeImpl, parent: QObject | None = None):
        super().__init__(parent)
        self._themeImpl = themeImpl

    @property
    def themeImpl(self) -> ThemeImpl:
        return self._themeImpl

    @themeImpl.setter
    def themeImpl(self, themeImpl: ThemeImpl):
        self._themeImpl = themeImpl
        self.themeChanged.emit()

    @Property(QColor, notify=themeChanged)
    def primary(self):
        return self._themeImpl.customPalette.primary

    @Property(QColor, notify=themeChanged)
    def secondary(self):
        return self._themeImpl.customPalette.secondary

    @Property(QColor, notify=themeChanged)
    def tertiary(self):
        return self._themeImpl.customPalette.tertiary

    @Property(QColor, notify=themeChanged)
    def success(self):
        return self._themeImpl.customPalette.success

    @Property(QColor, notify=themeChanged)
    def error(self):
        return self._themeImpl.customPalette.error

    @Property(QColor, notify=themeChanged)
    def toolTipBase(self):
        return self._themeImpl.customPalette.toolTipBase

    @Property(QColor, notify=themeChanged)
    def toolTipText(self):
        return self._themeImpl.customPalette.toolTipText
