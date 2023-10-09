import logging
import re
import sqlite3
import time
from pathlib import Path

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget

from ui.designer.tabs.tabOcr.tabOcr_BuildPHashDatabase_ui import (
    Ui_tabOcr_BuildPHashDatabase,
)
from ui.extends.ocr import build_image_phash_database

logger = logging.getLogger(__name__)


class BuildDatabaseThread(QThread):
    conn: sqlite3.Connection

    progress = Signal(int, int)
    success = Signal()
    error = Signal(str)
    finished = Signal()

    def __init__(
        self,
        images: list[Path],
        labels: list[str],
        *,
        hashSize: int | None = None,
        highfreqFactor: int | None = None,
    ):
        super().__init__()
        self.images = images
        self.labels = labels
        self.hashSize = hashSize
        self.highfreqFactor = highfreqFactor

    def run(self):
        try:
            progressFunc = lambda i, total: self.progress.emit(i, total)

            kwargsDict = {}
            if self.hashSize is not None:
                kwargsDict["hash_size"] = self.hashSize
            if self.highfreqFactor is not None:
                kwargsDict["highfreq_factor"] = self.highfreqFactor
            self.conn = build_image_phash_database(
                self.images, self.labels, progress_func=progressFunc, **kwargsDict
            )
            self.success.emit()
        except Exception as e:
            logger.exception("Error during pHash database build")
            self.error.emit(str(e))
        finally:
            self.finished.emit()


class TabOcr_BuildPHashDatabase(Ui_tabOcr_BuildPHashDatabase, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.songDirSelector.setMode(self.songDirSelector.getExistingDirectory)
        self.charIconDirSelector.setMode(self.charIconDirSelector.getExistingDirectory)

        self.buildButton.clicked.connect(self.databaseBuildStart)

    @Slot()
    def on_optionsResetButton_clicked(self):
        self.hashSizeSpinBox.setValue(16)
        self.highfreqFactorSpinBox.setValue(4)

    def databaseFileName(self):
        return f"image-phash-{int(time.time() * 1000)}.db"

    def databaseBuildStart(self):
        if not self.songDirSelector.selectedFiles():
            QMessageBox.critical(self, None, "Song directory not selected.")
            return
        if not self.charIconDirSelector.selectedFiles():
            QMessageBox.critical(self, None, "Char icon directory not selected.")
            return

        songDir = self.songDirSelector.selectedFiles()[0]
        charIconDir = self.charIconDirSelector.selectedFiles()[0]

        acceptExts = [".jpg", ".png"]
        songFilePaths = [
            p for p in Path(songDir).glob("**/*") if p.suffix in acceptExts
        ]
        charIconFilePaths = [
            p for p in Path(charIconDir).glob("**/*") if p.suffix in acceptExts
        ]
        songLabels = [re.sub(r"_.*$", "", p.stem) for p in songFilePaths]
        charLabels = [f"character||{p.stem}" for p in charIconFilePaths]

        self.databaseBuildThread = BuildDatabaseThread(
            songFilePaths + charIconFilePaths, songLabels + charLabels
        )
        self.databaseBuildThread.progress.connect(self.databaseBuildProgress)
        self.databaseBuildThread.success.connect(self.databaseBuildSuccess)
        self.databaseBuildThread.error.connect(self.databaseBuildError)
        self.buildButton.setEnabled(False)
        self.databaseBuildThread.start()

    @Slot(int, int)
    def databaseBuildProgress(self, i: int, total: int):
        if i < 5:
            self.progressBar.setMaximum(total)
        self.progressBar.setValue(i)

    @Slot(str)
    def databaseBuildError(self, msg: str):
        QMessageBox.critical(self, "Error", msg)
        self.databaseBuildCleanUp()

    @Slot()
    def databaseBuildSuccess(self):
        dbMemory = self.databaseBuildThread.conn

        dbFileName, _ = QFileDialog.getSaveFileName(self, None, self.databaseFileName())
        if not dbFileName:
            self.databaseBuildCleanUp()
            QMessageBox.information(self, None, "User canceled operation.")
            return

        dbDisk = sqlite3.connect(dbFileName)
        dbMemory.backup(dbDisk)
        self.databaseBuildCleanUp()

    def databaseBuildCleanUp(self):
        self.databaseBuildThread.deleteLater()
        self.databaseBuildThread = None
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.buildButton.setEnabled(True)
