from typing import Union

from arcaea_offline.database import Database
from PySide6.QtCore import QAbstractTableModel, Qt


class DbTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._horizontalHeaders = []
        self.retranslateHeaders()

        self._db = Database()

    def retranslateHeaders(self):
        ...

    def syncDb(self):
        ...

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if (
            orientation == Qt.Orientation.Horizontal
            and self._horizontalHeaders
            and 0 <= section < len(self._horizontalHeaders)
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self._horizontalHeaders[section]
        return super().headerData(section, orientation, role)

    def columnCount(self, parent=None):
        if self._horizontalHeaders:
            return len(self._horizontalHeaders)
        return super().columnCount(parent)
