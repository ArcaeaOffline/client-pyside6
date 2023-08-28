from typing import Type

from PySide6.QtCore import QUrl
from sqlalchemy import Engine
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.pool import NullPool, Pool


def create_engine(_url: str | QUrl, pool: Type[Pool] = NullPool) -> Engine:
    url = _url.toString() if isinstance(_url, QUrl) else _url
    return sa_create_engine(url, poolclass=pool)
