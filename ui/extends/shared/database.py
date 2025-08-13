from PySide6.QtCore import QObject, Signal


class DatabaseUpdateSignals(QObject):
    songAddOrDelete = Signal()
    chartInfoUpdated = Signal()


databaseUpdateSignals = DatabaseUpdateSignals()
