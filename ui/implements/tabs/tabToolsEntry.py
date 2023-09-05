from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabToolsEntry_ui import Ui_TabToolsEntry


class TabToolsEntry(Ui_TabToolsEntry, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
