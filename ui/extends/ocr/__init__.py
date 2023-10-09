from .build_phash import build_image_phash_database

try:
    import json

    from arcaea_offline_ocr.device.v1.definition import DeviceV1
    from arcaea_offline_ocr.device.v2.definition import DeviceV2

    def load_devices_json(filepath: str) -> list[DeviceV1]:
        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()
            if len(file_content) == 0:
                return []
            content = json.loads(file_content)
            assert isinstance(content, list)
            devices = []
            for item in content:
                version = item["version"]
                if version == 1:
                    devices.append(DeviceV1(**item))
                elif version == 2:
                    devices.append(DeviceV2(**item))
            return devices

except Exception:

    def load_devices_json(*args, **kwargs):
        pass
