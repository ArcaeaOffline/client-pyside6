from typing import Generic, TypeVar

from PySide6.QtCore import QObject

T = TypeVar("T")


class Singleton(type, Generic[T]):
    _instance = None

    def __call__(cls, *args, **kwargs) -> T:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class QSingleton(type(QObject), Singleton):
    pass
