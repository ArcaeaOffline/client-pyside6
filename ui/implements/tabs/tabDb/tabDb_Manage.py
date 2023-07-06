import logging
import traceback

from arcaea_offline.database import Database
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget

from ui.designer.tabs.tabDb.tabDb_Manage_ui import Ui_TabDb_Manage

logger = logging.getLogger(__name__)


class TabDb_Manage(Ui_TabDb_Manage, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    @Slot()
    def on_syncArcSongDbButton_clicked(self):
        dbFile, filter = QFileDialog.getOpenFileName(
            self, None, "", "DB File (*.db);;*"
        )
        try:
            Database().update_arcsong_db(dbFile)
            QMessageBox.information(self, "OK", "OK")
        except Exception as e:
            logging.exception("Sync arcsong.db error")
            QMessageBox.critical(
                self, "Sync Error", "\n".join(traceback.format_exception(e))
            )
