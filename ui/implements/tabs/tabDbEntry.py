from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabDbEntry_ui import Ui_TabDbEntry
from ui.implements.tabs.tabDb.tabDb_ScoreTableViewer import DbScoreTableViewer


class TabDbEntry(Ui_TabDbEntry, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.tabWidget.addTab(
            DbScoreTableViewer(self),
            QCoreApplication.translate("TabDbEntry", "tab.scoreTableViewer"),
        )
