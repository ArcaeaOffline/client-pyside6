from pathlib import Path

from arcaea_offline.models import CalculatedPotential
from sqlalchemy import select
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

        db_path = Path(db_path)
        if not db_path.exists():
            raise FileNotFoundError(f"{db_path} does not exist")

        self.engine = create_engine(db_path_to_sqlite_url(db_path))
        self.sessionmaker = sessionmaker(bind=self.engine)

    @property
    def b30(self) -> float | None:
        with self.sessionmaker() as session:
            return session.scalar(select(CalculatedPotential.b30))
