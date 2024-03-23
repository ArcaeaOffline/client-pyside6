import logging
import traceback
from enum import IntEnum

from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication, QDir, QFileInfo, QSysInfo, Qt, QUrl, Slot
from PySide6.QtWidgets import QDialog, QMessageBox

from ui.extends.shared.database import create_engine
from ui.extends.shared.settings import Settings

from .databaseChecker_ui import Ui_DatabaseChecker

logger = logging.getLogger(__name__)


class DatabaseCheckerResult(IntEnum):
    FileExist = 0x001
    Initted = 0x002


class DatabaseChecker(Ui_DatabaseChecker, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
        self.dbDirSelector.setMode(self.dbDirSelector.getExistingDirectory)

        self.confirmDbByExistingSettings = False
        self.settings = Settings(self)
        if dbUrlString := self.settings.databaseUrl():
            dbFileUrl = QUrl(dbUrlString.replace("sqlite://", "file://"))
            dbFileInfo = QFileInfo(dbFileUrl.toLocalFile())
            if dbFileInfo.exists():
                self.dbDirSelector.selectFile(dbFileInfo.path())
                self.dbFilenameLineEdit.setText(dbFileInfo.fileName())
                self.confirmDbByExistingSettings = True
                self.confirmDbPathButton.click()
            else:
                self.dbDirSelector.selectFile(QDir.currentPath())
                self.dbFilenameLineEdit.setText("arcaea_offline.db")
        else:
            self.dbDirSelector.selectFile(QDir.currentPath())
            self.dbFilenameLineEdit.setText("arcaea_offline.db")

    def dbPath(self):
        return QDir(self.dbDirSelector.selectedFiles()[0])

    def dbFileInfo(self):
        return QFileInfo(
            QDir.cleanPath(
                self.dbPath().absoluteFilePath(self.dbFilenameLineEdit.text())
            )
        )

    def dbFileUrl(self):
        return QUrl.fromLocalFile(self.dbFileInfo().filePath())

    def dbSqliteUrl(self):
        kernelType = QSysInfo.kernelType()
        # the slash count varies depending on the kernel
        # https://docs.sqlalchemy.org/en/20/core/engines.html#sqlite
        if kernelType == "winnt":
            return QUrl(self.dbFileUrl().toString().replace("file://", "sqlite://"))
        else:
            return QUrl(self.dbFileUrl().toString().replace("file://", "sqlite:///"))

    def confirmDb(self) -> DatabaseCheckerResult:
        flags = 0x000

        dbFileInfo = self.dbFileInfo()
        dbSqliteUrl = self.dbSqliteUrl()
        if not dbFileInfo.exists():
            return flags

        flags |= DatabaseCheckerResult.FileExist
        db = Database(create_engine(dbSqliteUrl))
        if db.check_init():
            flags |= DatabaseCheckerResult.Initted
            self.settings.setDatabaseUrl(self.dbSqliteUrl().toString())

        return flags

    def updateLabels(self):
        result = self.confirmDb()
        try:
            db = Database()
            version = db.version()
            initted = db.check_init()
            self.dbVersionLabel.setText(str(version))
            self.dbCheckConnLabel.setText(
                '<font color="green">OK</font>'
                if initted
                else '<font color="red">Not initted</font>'
            )
            self.continueButton.setEnabled(initted)
        except Exception as e:
            self.dbVersionLabel.setText("-")
            self.dbCheckConnLabel.setText(
                f'<font color="red">Error: {e}</font>'
                if result & DatabaseCheckerResult.FileExist
                else "-"
            )
            self.continueButton.setEnabled(False)

    @Slot()
    def on_confirmDbPathButton_clicked(self):
        dbSqliteUrl = self.dbSqliteUrl()
        self.settings.setDatabaseUrl(dbSqliteUrl.toString())

        result = self.confirmDb()
        if result & DatabaseCheckerResult.Initted:
            if not self.confirmDbByExistingSettings:
                self.settings.setDatabaseUrl(dbSqliteUrl.toString())
        elif result & DatabaseCheckerResult.FileExist:
            confirm_try_init = QMessageBox.question(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("DatabaseChecker", "dialog.tryInitExistingDatabase"),
                # fmt: on
            )
            if confirm_try_init == QMessageBox.StandardButton.Yes:
                try:
                    Database().init(checkfirst=True)
                except Exception as e:
                    logger.exception("Error while initializing an existing database")
                    QMessageBox.critical(
                        self, None, "\n".join(traceback.format_exception(e))
                    )
        else:
            confirm_new_database = QMessageBox.question(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("DatabaseChecker", "dialog.confirmNewDatabase"),
                # fmt: on
            )
            if confirm_new_database == QMessageBox.StandardButton.Yes:
                db = Database(create_engine(dbSqliteUrl))
                db.init()
        self.updateLabels()

    @Slot()
    def on_dbReInitButton_clicked(self):
        Database().init(checkfirst=True)
        QMessageBox.information(self, None, "OK")

    @Slot()
    def on_continueButton_clicked(self):
        self.accept()
