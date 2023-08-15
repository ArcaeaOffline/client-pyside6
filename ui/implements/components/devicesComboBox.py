from arcaea_offline_ocr.device.v1.definition import DeviceV1
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox

from ui.extends.ocr import load_devices_json
from ui.extends.shared.delegates.descriptionDelegate import DescriptionDelegate


class DevicesComboBox(QComboBox):
    DeviceUuidRole = Qt.ItemDataRole.UserRole + 10

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegate(DescriptionDelegate(self))

    def setDevices(self, devices: list[DeviceV1]):
        self.clear()
        for device in devices:
            self.addItem(f"{device.name} ({device.uuid})", device)
            row = self.count() - 1
            self.setItemData(row, device.uuid, self.DeviceUuidRole)
            self.setItemData(row, device.name, DescriptionDelegate.MainTextRole)
            self.setItemData(row, device.uuid, DescriptionDelegate.DescriptionTextRole)
        self.setCurrentIndex(-1)

    def loadDevicesJson(self, path: str):
        devices = load_devices_json(path)
        self.setDevices(devices)

    def selectDevice(self, deviceUuid: str):
        index = self.findData(deviceUuid, self.DeviceUuidRole)
        self.setCurrentIndex(index)
