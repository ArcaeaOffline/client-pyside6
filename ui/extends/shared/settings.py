import sys

from PySide6.QtCore import QFileInfo, QSettings, Signal

from .singleton import QObjectSingleton

__all__ = [
    "LANGUAGE",
    "DATABASE_URL",
    "KNN_MODEL_FILE",
    "B30_KNN_MODEL_FILE",
    "PHASH_DATABASE_FILE",
    "ANDREAL_FOLDER",
    "ANDREAL_EXECUTABLE",
    "Settings",
]

# a key without slashes will appear in the "General" section
# see https://doc.qt.io/qt-6/qsettings.html#Format-enum for details
LANGUAGE = "Language"
DATABASE_URL = "DatabaseUrl"

KNN_MODEL_FILE = "Ocr/KnnModelFile"
B30_KNN_MODEL_FILE = "Ocr/B30KnnModelFile"
PHASH_DATABASE_FILE = "Ocr/PHashDatabaseFile"

ANDREAL_FOLDER = "Andreal/AndrealFolder"
ANDREAL_EXECUTABLE = "Andreal/AndrealExecutable"


class Settings(QSettings, metaclass=QObjectSingleton):
    updated = Signal(str)

    def __init__(self, parent=None):
        super().__init__(
            QFileInfo(sys.argv[0]).dir().absoluteFilePath("arcaea_offline.ini"),
            QSettings.Format.IniFormat,
            parent,
        )

    def setValue(self, key: str, value) -> None:
        super().setValue(key, value)
        self.updated.emit(key)

    def _strItem(self, key: str) -> str | None:
        return self.value(key, None, str)

    def _setStrItem(self, key: str, value: str):
        self.setValue(key, value)
        self.sync()

    def _resetStrItem(self, key: str):
        self.setValue(key, None)
        self.sync()

    def language(self):
        return self._strItem(LANGUAGE)

    def setLanguage(self, value: str):
        self._setStrItem(LANGUAGE, value)

    def databaseUrl(self):
        return self._strItem(DATABASE_URL)

    def setDatabaseUrl(self, value: str):
        self._setStrItem(DATABASE_URL, value)

    def knnModelFile(self):
        return self._strItem(KNN_MODEL_FILE)

    def setKnnModelFile(self, value: str):
        self._setStrItem(KNN_MODEL_FILE, value)

    def resetKnnModelFile(self):
        self._resetStrItem(KNN_MODEL_FILE)

    def b30KnnModelFile(self):
        return self._strItem(B30_KNN_MODEL_FILE)

    def setB30KnnModelFile(self, value: str):
        self._setStrItem(B30_KNN_MODEL_FILE, value)

    def resetB30KnnModelFile(self):
        self._resetStrItem(B30_KNN_MODEL_FILE)

    def phashDatabaseFile(self):
        return self._strItem(PHASH_DATABASE_FILE)

    def setPHashDatabaseFile(self, value: str):
        self._setStrItem(PHASH_DATABASE_FILE, value)

    def resetPHashDatabaseFile(self):
        self._resetStrItem(PHASH_DATABASE_FILE)

    def andrealFolder(self):
        return self._strItem(ANDREAL_FOLDER)

    def setAndrealFolder(self, value: str):
        self._setStrItem(ANDREAL_FOLDER, value)

    def resetAndrealFolder(self):
        self._resetStrItem(ANDREAL_FOLDER)

    def andrealExecutable(self):
        return self._strItem(ANDREAL_EXECUTABLE)

    def setAndrealExecutable(self, value: str):
        self._setStrItem(ANDREAL_EXECUTABLE, value)

    def resetAndrealExecutable(self):
        self._resetStrItem(ANDREAL_EXECUTABLE)
