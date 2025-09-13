from pathlib import Path

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from core.settings import SettingsKeys, settings

from .utils import create_engine, db_path_to_sqlite_url


class Database:
    def __init__(self):
        if settings.stringValue(SettingsKeys.General.DatabaseType) != "file":
            raise ValueError("DatabaseType is not file")

        db_path = settings.stringValue(SettingsKeys.General.DatabaseConn)
        if not db_path:
            raise ValueError("DatabaseConn is empty")

        self.engine = create_engine(db_path_to_sqlite_url(Path(db_path)))
        self.sessionmaker = sessionmaker(bind=self.engine)

    @property
    def b30(self) -> float | None:
        with self.sessionmaker() as session:
            result = session.execute(
                text("SELECT b30 FROM calculated_potential")
            ).fetchone()
            return result[0] if result else None
