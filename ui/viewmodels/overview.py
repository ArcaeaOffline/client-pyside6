from PySide6.QtCore import Property, QObject, Signal
from PySide6.QtQml import QmlElement

from .common import VM_QML_IMPORT_NAME

QML_IMPORT_NAME = VM_QML_IMPORT_NAME
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0


@QmlElement
class OverviewViewModel(QObject):
    _void = Signal()

    def __init__(self):
        super().__init__()

    def get_b30(self):
        return 0

    b30 = Property(float, get_b30, None, notify=_void)
