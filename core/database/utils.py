from pathlib import Path

from PySide6.QtCore import QSysInfo, QUrl
from sqlalchemy import Engine
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.pool import NullPool, Pool


def db_path_to_sqlite_url(file: Path) -> QUrl:
    kernelType = QSysInfo.kernelType()

    # the slash count varies depending on the kernel
    # https://docs.sqlalchemy.org/en/20/core/engines.html#sqlite
    uri = file.resolve().as_uri()
    if kernelType == "winnt":
        return QUrl(uri.replace("file://", "sqlite://"))
    else:
        return QUrl(uri.replace("file://", "sqlite:///"))


def sqlite_url_to_db_path(url: str) -> Path:
    db_file_url = url.replace("sqlite://", "file://")
    return Path(QUrl(db_file_url).toLocalFile()).resolve()


def create_engine(_url: str | QUrl, pool: type[Pool] = NullPool) -> Engine:
    url = _url.toString() if isinstance(_url, QUrl) else _url
    return sa_create_engine(url, poolclass=pool)
