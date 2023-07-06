from PySide6.QtCore import QDir, QSettings

__all__ = [
    "DATABASE_PATH",
    "DEVICES_JSON_FILE",
    "DEVICE_UUID",
    "TESSERACT_FILE",
    "Settings",
]

DATABASE_PATH = "General/DatabasePath"

DEVICES_JSON_FILE = "Ocr/DevicesJsonFile"
DEVICE_UUID = "Ocr/DeviceUuid"
TESSERACT_FILE = "Ocr/TesseractFile"


class Settings(QSettings):
    def __init__(self, parent=None):
        super().__init__(
            QDir.current().absoluteFilePath("arcaea_offline.ini"),
            QSettings.Format.IniFormat,
            parent,
        )

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
