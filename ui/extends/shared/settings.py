import sys
from PySide6.QtCore import QSettings, QFileInfo

__all__ = [
    "DATABASE_URL",
    "DEVICES_JSON_FILE",
    "DEVICE_UUID",
    "TESSERACT_FILE",
    "KNN_MODEL_FILE",
    "SIFT_DATABASE_FILE",
    "Settings",
]

# a key without slashes will appear in the "General" section
# see https://doc.qt.io/qt-6/qsettings.html#Format-enum for details
DATABASE_URL = "DatabaseUrl"

DEVICES_JSON_FILE = "Ocr/DevicesJsonFile"
DEVICE_UUID = "Ocr/DeviceUuid"
TESSERACT_FILE = "Ocr/TesseractFile"
KNN_MODEL_FILE = "Ocr/KnnModelFile"
SIFT_DATABASE_FILE = "Ocr/SiftDatabaseFile"

ANDREAL_PATH = "Andreal/AndrealFolderPath"
ANDREAL_EXECUTABLE = "Andreal/AndrealExecutable"


class Settings(QSettings):
    def __init__(self, parent=None):
        super().__init__(
            QFileInfo(sys.argv[0]).dir().absoluteFilePath("arcaea_offline.ini"),
            QSettings.Format.IniFormat,
            parent,
        )

    def _strItem(self, key: str) -> str | None:
        return self.value(key, None, str)

    def _setStrItem(self, key: str, value: str):
        self.setValue(key, value)
        self.sync()

    def _resetStrItem(self, key: str):
        self.setValue(key, None)
        self.sync()

    def databaseUrl(self):
        return self._strItem(DATABASE_URL)

    def setDatabaseUrl(self, value: str):
        self._setStrItem(DATABASE_URL, value)

    def devicesJsonFile(self):
        return self._strItem(DEVICES_JSON_FILE)

    def setDevicesJsonFile(self, value: str):
        self._setStrItem(DEVICES_JSON_FILE, value)

    def resetDevicesJsonFile(self):
        self._resetStrItem(DEVICES_JSON_FILE)

    def deviceUuid(self):
        return self._strItem(DEVICE_UUID)

    def setDeviceUuid(self, value: str):
        self._setStrItem(DEVICE_UUID, value)

    def resetDeviceUuid(self):
        self._resetStrItem(DEVICE_UUID)

    def tesseractPath(self):
        return self._strItem(TESSERACT_FILE)

    def setTesseractPath(self, value: str):
        self._setStrItem(TESSERACT_FILE, value)

    def resetTesseractPath(self):
        self._resetStrItem(TESSERACT_FILE)

    def knnModelFile(self):
        return self._strItem(KNN_MODEL_FILE)

    def setKnnModelFile(self, value: str):
        self._setStrItem(KNN_MODEL_FILE, value)

    def resetKnnModelFile(self):
        self._resetStrItem(KNN_MODEL_FILE)

    def siftDatabaseFile(self):
        return self._strItem(SIFT_DATABASE_FILE)

    def setSiftDatabaseFile(self, value: str):
        self._setStrItem(SIFT_DATABASE_FILE, value)

    def resetSiftDatabaseFile(self):
        self._resetStrItem(SIFT_DATABASE_FILE)
