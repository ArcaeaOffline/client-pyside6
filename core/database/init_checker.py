from enum import Flag, auto
from pathlib import Path

from arcaea_offline.database import Database

from .utils import create_engine, db_path_to_sqlite_url


class DatabaseInitCheckResult(Flag):
    NONE = 0
    FILE_EXISTS = auto()
    INITIALIZED = auto()

    OK = FILE_EXISTS | INITIALIZED


def check_db_init(file: Path) -> DatabaseInitCheckResult:
    flags = DatabaseInitCheckResult.NONE

    if not file.exists():
        return flags

    flags |= DatabaseInitCheckResult.FILE_EXISTS

    db_url = db_path_to_sqlite_url(file)
    db = Database(create_engine(db_url))
    if db.check_init():
        flags |= DatabaseInitCheckResult.INITIALIZED

    return flags
