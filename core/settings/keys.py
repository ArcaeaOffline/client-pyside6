from dataclasses import dataclass
from enum import StrEnum


class _General(StrEnum):
    Language = "Language"
    DatabaseUrl = "DatabaseUrl"


class _Ocr(StrEnum):
    KnnModelFile = "Ocr/KnnModelFile"
    B30KnnModelFile = "Ocr/B30KnnModelFile"
    PhashDatabaseFile = "Ocr/PHashDatabaseFile"
    DateSource = "Ocr/DateSource"


class _Andreal(StrEnum):
    Folder = "Andreal/AndrealFolder"
    Executable = "Andreal/AndrealExecutable"


@dataclass(frozen=True)
class SettingsKeys:
    General = _General
    Ocr = _Ocr
    Andreal = _Andreal
