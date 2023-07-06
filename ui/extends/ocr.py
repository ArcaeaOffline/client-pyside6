try:
    import json

    from arcaea_offline_ocr.device import Device

    def load_devices_json(filepath: str) -> list[Device]:
        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()
            if len(file_content) == 0:
                return []
            content = json.loads(file_content)
            assert isinstance(content, list)
            return [Device.from_json_object(item) for item in content]

except Exception:

    def load_devices_json(*args, **kwargs):
        pass
