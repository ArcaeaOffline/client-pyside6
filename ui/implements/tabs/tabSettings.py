from PySide6.QtCore import QModelIndex, Slot
from PySide6.QtWidgets import QListWidgetItem, QWidget

from ui.designer.tabs.tabSettings_ui import Ui_TabSettings


class SettingsEntryItem(QListWidgetItem):
    pass


class TabSettings(Ui_TabSettings, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.listWidget.addItem("Default")
        self.listWidget.activated.connect(self.switchPage)

        self.listWidget.setCurrentRow(self.stackedWidget.currentIndex())

    @Slot(QModelIndex)
    def switchPage(self, index: QModelIndex):
        self.stackedWidget.setCurrentIndex(index.row())
