from dataclasses import dataclass


@dataclass(frozen=True)
class _Ocr_ScoreDateSource:
    FileCreated: str = "FileCreated"
    FileLastModified: str = "FileLastModified"


@dataclass(frozen=True)
class _Ocr:
    DateSource = _Ocr_ScoreDateSource()


@dataclass(frozen=True)
class SettingsValues:
    Ocr = _Ocr()
