import traceback

from arcaea_offline.database import Database
from PySide6.QtCore import QDir, QFile, Qt, QTimer, Slot
from PySide6.QtWidgets import QDialog, QMessageBox

from ui.extends.settings import Settings

from .databaseChecker_ui import Ui_DatabaseChecker


class DatabaseChecker(Ui_DatabaseChecker, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
        self.dbFileSelector.setMode(self.dbFileSelector.getExistingDirectory)
        self.dbFileSelector.filesSelected.connect(self.fileSelected)

        self.settings = Settings(self)
        dbDir = self.settings.value("Default/DbDir", None, str)
        if dbDir and QFile(QDir(dbDir).filePath(Database.dbFilename)).exists():
            self.dbFileSelector.selectFile(dbDir)
            result = self.checkDbVersion()
            if result:
                QTimer.singleShot(50, self.accept)
        else:
            self.dbFileSelector.selectFile(QDir.currentPath())

    def fileSelected(self):
        self.checkDbVersion()

    def checkDbVersion(self) -> str | None:
        dbQDir = QDir(self.dbFileSelector.selectedFiles()[0])
        dbDir = dbQDir.absolutePath()

        dbDir = self.dbFileSelector.selectedFiles()[0]
        dbQFile = QFile(QDir(dbDir).filePath(Database.dbFilename))
        if not dbQFile.exists():
            result = QMessageBox.question(self, "Database", "Create database file now?")
            if result != QMessageBox.StandardButton.Yes:
                return
            dbQFile.open(QFile.OpenModeFlag.WriteOnly)
            dbQFile.close()

        Database.dbDir = dbDir

        try:
            with Database().conn as conn:
                version = conn.execute(
                    "SELECT value FROM properties WHERE key = 'db_version'"
                ).fetchone()[0]
                self.dbVersionLabel.setText(version)
                self.continueButton.setEnabled(True)

                self.dbCheckConnLabel.setText('<font color="green">OK</font>')
                self.settings.setValue("Default/DbDir", dbDir)
            return version
        except Exception as e:
            QMessageBox.critical(
                self, "Database Error", "\n".join(traceback.format_exception(e))
            )
            self.dbInitButton.setEnabled(True)
            self.continueButton.setEnabled(False)
            self.dbCheckConnLabel.setText('<font color="red">Error</font>')
            return False

    @Slot()
    def on_dbInitButton_clicked(self):
        try:
            Database().init()
        except Exception as e:
            QMessageBox.critical(
                self, "Database Error", "\n".join(traceback.format_exception(e))
            )
        finally:
            self.checkDbVersion()

    @Slot()
    def on_continueButton_clicked(self):
        self.accept()
