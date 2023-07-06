from PySide6.QtWidgets import QWidget

from ui.designer.components.dbTableViewer_ui import Ui_DbTableViewer


class DbTableViewer(Ui_DbTableViewer, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
