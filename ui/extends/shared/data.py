import json
import sys
from functools import cached_property
from pathlib import Path
from typing import Literal, Optional, overload

from arcaea_offline.models import Chart, Difficulty, Song
from PySide6.QtCore import QFile

from core.singleton import Singleton

TPartnerModifier = dict[str, Literal[0, 1, 2]]


class Data(metaclass=Singleton):
    def __init__(self):
        root = Path(sys.argv[0]).parent
        self.__dataPath = (root / "data").resolve()

    @property
    def dataPath(self):
        return self.__dataPath

    @cached_property
    def partnerModifiers(self) -> TPartnerModifier:
        data = {}
        builtinFile = QFile(":/partnerModifiers.json")
        builtinFile.open(QFile.OpenModeFlag.ReadOnly)
        builtinData = json.loads(str(builtinFile.readAll(), encoding="utf-8"))
        builtinFile.close()
        data |= builtinData

        customFile = self.dataPath / "partnerModifiers.json"
        if customFile.exists():
            with open(customFile, "r", encoding="utf-8") as f:
                customData = json.loads(f.read())
                data |= customData

        return data

    def expirePartnerModifiersCache(self):
        # expire property caches
        # https://stackoverflow.com/a/69367025/16484891, CC BY-SA 4.0
        self.__dict__.pop("partnerModifiers", None)

    @property
    def arcaeaPath(self):
        return self.dataPath / "Arcaea"

    @overload
    def getJacketPath(self, chart: Chart, /) -> Path | None: ...

    @overload
    def getJacketPath(
        self, song: Song, difficulty: Optional[Difficulty] = None, /
    ) -> Path | None: ...

    def getJacketPath(self, *args) -> Path | None:
        if isinstance(args[0], Chart):
            chart = args[0]
            ratingSpecified = f"{chart.song_id}_{chart.rating_class}"
            base = chart.song_id
        elif isinstance(args[0], Song):
            song = args[0]
            difficulty = args[1]
            ratingSpecified = (
                f"{song.id}_{difficulty.rating_class}"
                if isinstance(difficulty, Difficulty)
                else song.id
            )
            base = song.id
        else:
            raise ValueError()

        ratingSpecified += ".jpg"
        base += ".jpg"

        jacketsPath = self.arcaeaPath / "Song"
        if (jacketsPath / ratingSpecified).exists():
            return jacketsPath / ratingSpecified
        elif (jacketsPath / base).exists():
            return jacketsPath / base
        else:
            return None
