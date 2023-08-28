from arcaea_offline.database import Database
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabOverview_ui import Ui_TabOverview


class TabOverview(Ui_TabOverview, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.db = Database()
        # self.db.register_update_hook(self.updateOverview)
        # self.updateOverview()

    def showEvent(self, event: QShowEvent) -> None:
        self.updateOverview()
        return super().showEvent(event)

    def updateOverview(self):
        b30 = self.db.get_b30() or 0.00
        self.b30Label.setText(str(f"{b30:.3f}"))
