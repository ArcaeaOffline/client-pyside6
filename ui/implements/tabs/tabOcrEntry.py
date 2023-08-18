from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabOcrEntry_ui import Ui_TabOcrEntry


class TabOcrEntry(Ui_TabOcrEntry, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
