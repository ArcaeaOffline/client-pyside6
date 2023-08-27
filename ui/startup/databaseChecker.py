import logging
import traceback
from typing import Literal, Optional, Union

from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication, QDir, QFileInfo, Qt, QTimer, QUrl, Slot
from PySide6.QtWidgets import QDialog, QMessageBox

from ui.extends.shared.database import create_engine
from ui.extends.shared.settings import Settings

from .databaseChecker_ui import Ui_DatabaseChecker

logger = logging.getLogger(__name__)


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
        dbUrlString = self.settings.databaseUrl()

        if dbUrlString:
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

    def updateLabels(
        self,
        version: Union[Optional[int], Literal["reset"]],
        init_status: Union[Optional[bool], Literal["reset"]],
    ):
        if version is not None:
            self.dbVersionLabel.setText(str(version))
        elif version == "reset":
            self.dbVersionLabel.setText("-")

        if init_status is not None:
            if init_status:
                self.dbCheckConnLabel.setText('<font color="green">OK</font>')
                self.continueButton.setEnabled(True)
            else:
                self.dbCheckConnLabel.setText('<font color="red">Error</font>')
                self.continueButton.setEnabled(False)
        elif init_status == "reset":
            self.dbCheckConnLabel.setText("-")
            self.continueButton.setEnabled(False)

    @Slot()
    def on_confirmDbPathButton_clicked(self):
        dbPath = QDir(self.dbDirSelector.selectedFiles()[0])
        dbFileInfo = QFileInfo(
            QDir.cleanPath(dbPath.absoluteFilePath(self.dbFilenameLineEdit.text()))
        )
        dbFileUrl = QUrl.fromLocalFile(dbFileInfo.filePath())
        # dbSqliteUrl.setScheme("sqlite")
        dbSqliteUrl = QUrl(dbFileUrl.toString().replace("file://", "sqlite://"))
        if not dbFileInfo.exists():
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
                self.on_confirmDbPathButton_clicked()
        else:
            db = Database(create_engine(dbSqliteUrl))
            if db.check_init():
                self.updateLabels(db.version(), True)
                if self.confirmDbByExistingSettings:
                    QTimer.singleShot(25, self.accept)
                else:
                    self.settings.setDatabaseUrl(dbSqliteUrl.toString())
            else:
                confirm_try_init = QMessageBox.question(
                    self,
                    None,
                    # fmt: off
                    QCoreApplication.translate("DatabaseChecker", "dialog.tryInit"),
                    # fmt: on
                )
                if confirm_try_init == QMessageBox.StandardButton.Yes:
                    try:
                        db.init(checkfirst=True)
                    except Exception as e:
                        logger.exception(
                            "Error while initializing an existing database"
                        )
                        QMessageBox.critical(
                            self, None, "\n".join(traceback.format_exception(e))
                        )
                        self.updateLabels("reset", False)
                    finally:
                        self.on_confirmDbPathButton_clicked()

    @Slot()
    def on_continueButton_clicked(self):
        self.accept()
