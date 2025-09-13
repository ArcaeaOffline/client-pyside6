from PySide6.QtCore import Property, QObject, Signal, Slot
from PySide6.QtQml import QmlElement

from core.database import Database

from .common import VM_QML_IMPORT_NAME

QML_IMPORT_NAME = VM_QML_IMPORT_NAME
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0


@QmlElement
class OverviewViewModel(QObject):
    _void = Signal()
    b30Changed = Signal()

    def __init__(self):
        super().__init__()

        self._b30 = -1.0
        self.reload()

    @Slot()
    def reload(self):
        conn = Database()
        b30 = conn.b30
        self._b30 = b30 if b30 is not None else -1.0
        self.b30Changed.emit()

    def getB30(self):
        return self._b30

    b30 = Property(float, getB30, None, notify=b30Changed)
