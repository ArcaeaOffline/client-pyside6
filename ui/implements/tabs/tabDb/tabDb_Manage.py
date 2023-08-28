import logging
import traceback

from arcaea_offline.database import Database
from arcaea_offline.external.arcaea.st3 import St3ScoreParser
from arcaea_offline.external.arcsong import ArcsongDbParser
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

        if not dbFile:
            return

        try:
            db = Database()
            parser = ArcsongDbParser(dbFile)
            with db.sessionmaker() as session:
                parser.write_database(session)
                session.commit()
            QMessageBox.information(self, None, "OK")
        except Exception as e:
            logging.exception("Sync arcsong.db error")
            QMessageBox.critical(
                self, "Sync Error", "\n".join(traceback.format_exception(e))
            )

    @Slot()
    def on_importSt3Button_clicked(self):
        dbFile, filter = QFileDialog.getOpenFileName(self, "Select st3 file")

        if not dbFile:
            return

        try:
            db = Database()
            parser = St3ScoreParser(dbFile)
            logger.info(
                f"Got {len(parser.parse())} items from {dbFile}, writing into database..."
            )
            with db.sessionmaker() as session:
                parser.write_database(session)
                session.commit()
            QMessageBox.information(self, None, "OK")
        except Exception as e:
            logging.exception("import st3 error")
            QMessageBox.critical(
                self, "Import Error", "\n".join(traceback.format_exception(e))
            )
