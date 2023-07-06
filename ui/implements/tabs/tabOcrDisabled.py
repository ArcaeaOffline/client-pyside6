from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabOcrDisabled_ui import Ui_TabOcrDisabled


class TabOcrDisabled(Ui_TabOcrDisabled, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
