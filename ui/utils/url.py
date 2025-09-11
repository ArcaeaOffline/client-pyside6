from pathlib import Path

from PySide6.QtCore import QFileInfo, QObject, QUrl, Slot
from PySide6.QtQml import QmlElement, QmlSingleton

from .common import UTILS_QML_IMPORT_NAME

QML_IMPORT_NAME = UTILS_QML_IMPORT_NAME
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0


@QmlElement
@QmlSingleton
class UrlUtils(QObject):
    @Slot(str, result=bool)
    @staticmethod
    def isDir(url: str):
        return QFileInfo(QUrl(url).toLocalFile()).isDir()

    @Slot(str, result=bool)
    @staticmethod
    def isFile(url: str):
        return QFileInfo(QUrl(url).toLocalFile()).isFile()

    @Slot(str, result=str)
    @staticmethod
    def stem(url: str):
        return Path(QUrl(url).toLocalFile()).stem

    @Slot(str, result=str)
    @staticmethod
    def name(url: str):
        return Path(QUrl(url).toLocalFile()).name

    @Slot(str, result=QUrl)
    @staticmethod
    def parent(url: str):
        return QUrl.fromLocalFile(Path(QUrl(url).toLocalFile()).parent)


@QmlElement
@QmlSingleton
class UrlFormatUtils(QObject):
    @Slot(str, result=str)
    @staticmethod
    def toLocalFile(url: str):
        return QUrl(url).toLocalFile()
