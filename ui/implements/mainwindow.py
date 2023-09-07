from PySide6.QtWidgets import QMainWindow

from ui.designer.mainwindow_ui import Ui_MainWindow
from ui.extends.shared.language import LanguageChangeEventFilter


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)
