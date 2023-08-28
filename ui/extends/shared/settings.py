from PySide6.QtCore import QDir, QSettings, QUrl

__all__ = [
    "DATABASE_URL",
    "DEVICES_JSON_FILE",
    "DEVICE_UUID",
    "TESSERACT_FILE",
    "KNN_MODEL_FILE",
    "SIFT_DATABASE_FILE",
    "Settings",
]

DATABASE_URL = "General/DatabaseUrl"

DEVICES_JSON_FILE = "Ocr/DevicesJsonFile"
DEVICE_UUID = "Ocr/DeviceUuid"
TESSERACT_FILE = "Ocr/TesseractFile"
KNN_MODEL_FILE = "Ocr/KnnModelFile"
SIFT_DATABASE_FILE = "Ocr/SiftDatabaseFile"


class Settings(QSettings):
    def __init__(self, parent=None):
        super().__init__(
            QDir.current().absoluteFilePath("arcaea_offline.ini"),
            QSettings.Format.IniFormat,
            parent,
        )

    def databaseUrl(self) -> str | None:
        return self.value(DATABASE_URL, None, str)

    def setDatabaseUrl(self, value: str):
        self.setValue(DATABASE_URL, value)
        self.sync()

    def devicesJsonFile(self) -> str | None:
        return self.value(DEVICES_JSON_FILE, None, str)

    def setDevicesJsonFile(self, path: str):
        self.setValue(DEVICES_JSON_FILE, path)
        self.sync()

    def resetDevicesJsonFile(self):
        self.setValue(DEVICES_JSON_FILE, None)
        self.sync()

    def deviceUuid(self) -> str | None:
        return self.value(DEVICE_UUID, None, str)

    def setDeviceUuid(self, uuid: str):
        self.setValue(DEVICE_UUID, uuid)
        self.sync()

    def resetDeviceUuid(self):
        self.setValue(DEVICE_UUID, None)
        self.sync()

    def tesseractPath(self):
        return self.value(TESSERACT_FILE, None, str)

    def setTesseractPath(self, path: str):
        self.setValue(TESSERACT_FILE, path)
        self.sync()

    def resetTesseractPath(self):
        self.setValue(TESSERACT_FILE, None)
        self.sync()

    def knnModelFile(self) -> str | None:
        return self.value(KNN_MODEL_FILE, None, str)

    def setKnnModelFile(self, path: str):
        self.setValue(KNN_MODEL_FILE, path)
        self.sync()

    def resetKnnModelFile(self):
        self.setValue(KNN_MODEL_FILE, None)
        self.sync()

    def siftDatabaseFile(self) -> str | None:
        return self.value(SIFT_DATABASE_FILE, None, str)

    def setSiftDatabaseFile(self, path: str):
        self.setValue(SIFT_DATABASE_FILE, path)
        self.sync()

    def resetSiftDatabaseFile(self):
        self.setValue(SIFT_DATABASE_FILE, None)
        self.sync()
