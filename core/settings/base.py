import sys
from enum import Enum
from typing import Any

from PySide6.QtCore import QFileInfo, QSettings, Signal

from core.singleton import QSingleton

__all__ = ["Settings"]

TSettingsKey = str | Enum


class Settings(QSettings, metaclass=QSingleton):
    updated = Signal(str)

    def __init__(self, parent=None):
        super().__init__(
            QFileInfo(sys.argv[0]).dir().absoluteFilePath("arcaea_offline.ini"),
            QSettings.Format.IniFormat,
            parent,
        )

    def __settingsKey(self, key: TSettingsKey) -> str:
        if isinstance(key, Enum):
            return self.__settingsKey(key.value)

        if isinstance(key, str):
            return key

        raise TypeError(f"{key!r} is not a valid key")

    def setValue(self, key: TSettingsKey, value: Any) -> None:
        _key = self.__settingsKey(key)

        super().setValue(_key, value)
        self.updated.emit(_key)

    def stringValue(self, key: TSettingsKey) -> str | None:
        _key = self.__settingsKey(key)
        return self.value(_key, None, type=str)


settings = Settings()
