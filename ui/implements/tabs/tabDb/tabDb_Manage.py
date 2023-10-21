import csv
import json
import logging
import traceback
import zipfile

from arcaea_offline.database import Database
from arcaea_offline.external.arcaea import (
    ArcaeaOnlineParser,
    PacklistParser,
    SonglistDifficultiesParser,
    SonglistParser,
    St3ScoreParser,
)
from arcaea_offline.external.arcaea.common import ArcaeaParser
from arcaea_offline.external.arcsong import ArcsongDbParser
from arcaea_offline.external.smartrte import SmartRteB30CsvConverter
from arcaea_offline.models import Difficulty, Pack, Song
from PySide6.QtCore import QDir, Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget

from ui.designer.tabs.tabDb.tabDb_Manage_ui import Ui_TabDb_Manage
from ui.extends.shared.database import databaseUpdateSignals
from ui.extends.shared.language import LanguageChangeEventFilter

logger = logging.getLogger(__name__)


class TabDb_Manage(Ui_TabDb_Manage, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

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
                databaseUpdateSignals.chartInfoUpdated.emit()
            QMessageBox.information(self, None, "OK")
        except Exception as e:
            logging.exception("Sync arcsong.db error")
            QMessageBox.critical(
                self, "Sync Error", "\n".join(traceback.format_exception(e))
            )

    def importFromArcaeaParser(
        self, parser: ArcaeaParser, instance, logName, path
    ) -> int:
        # extracted by sourcery
        db = Database()
        with db.sessionmaker() as session:
            parser.write_database(session)
            session.commit()
            databaseUpdateSignals.songAddOrDelete.emit()
        itemNum = len([item for item in parser.parse() if isinstance(item, instance)])
        logger.info(f"updated {itemNum} {logName} from {path}")
        return itemNum

    def importPacklist(self, packlistPath):
        packlistParser = PacklistParser(packlistPath)
        return self.importFromArcaeaParser(packlistParser, Pack, "packs", packlistPath)

    def importSonglist(self, songlistPath):
        songlistParser = SonglistParser(songlistPath)
        return self.importFromArcaeaParser(songlistParser, Song, "songs", songlistPath)

    def importSonglistDifficulties(self, songlistPath):
        songlistDifficultiesParser = SonglistDifficultiesParser(songlistPath)
        return self.importFromArcaeaParser(
            songlistDifficultiesParser, Difficulty, "difficulties", songlistPath
        )

    @Slot()
    def on_importPacklistButton_clicked(self):
        try:
            packlistFile, filter = QFileDialog.getOpenFileName(
                self, "Select packlist file"
            )

            if not packlistFile:
                return

            packNum = self.importPacklist(packlistFile)
            QMessageBox.information(
                self, None, f"Updated {packNum} packs from<br>{packlistFile}"
            )
        except Exception as e:
            logger.exception("import packlist error")
            QMessageBox.critical(
                self, "Import Error", "\n".join(traceback.format_exception(e))
            )

    @Slot()
    def on_importSonglistButton_clicked(self):
        try:
            songlistFile, filter = QFileDialog.getOpenFileName(
                self, "Select songlist file"
            )

            if not songlistFile:
                return

            songNum = self.importSonglist(songlistFile)
            difficultyNum = self.importSonglistDifficulties(songlistFile)
            QMessageBox.information(
                self,
                None,
                f"Updated {songNum} songs and {difficultyNum} difficulties from<br>{songlistFile}",
            )
        except Exception as e:
            logger.exception("import songlist error")
            QMessageBox.critical(
                self, "Import Error", "\n".join(traceback.format_exception(e))
            )

    @Slot()
    def on_importApkButton_clicked(self):
        apkFile, filter = QFileDialog.getOpenFileName(
            self, "Select APK file", "", "APK File (*.apk);;*"
        )

        if not apkFile:
            return

        try:
            logger.info(f"Importing {apkFile}")

            with zipfile.ZipFile(apkFile) as zf:
                packlistPath = zipfile.Path(zf) / "assets" / "songs" / "packlist"
                songlistPath = zipfile.Path(zf) / "assets" / "songs" / "songlist"

                packsNum = self.importPacklist(packlistPath)
                songsNum = self.importSonglist(songlistPath)
                difficultyNum = self.importSonglistDifficulties(songlistPath)

            message = [
                f"{packsNum} packs, {songsNum} songs and {difficultyNum} difficulties updated from",
                str(apkFile),
            ]
            QMessageBox.information(self, None, "<br>".join(message))
        except Exception as e:
            logging.exception("import apk error")
            QMessageBox.critical(
                self, "Import Error", "\n".join(traceback.format_exception(e))
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

    @Slot()
    def on_importOnlineButton_clicked(self):
        apiResultFile, filter = QFileDialog.getOpenFileName(
            self, "Select API result JSON file"
        )

        if not apiResultFile:
            return

        try:
            db = Database()
            parser = ArcaeaOnlineParser(apiResultFile)
            logger.info(
                f"Got {len(parser.parse())} items from {apiResultFile}, writing into database..."
            )
            with db.sessionmaker() as session:
                parser.write_database(session)
                session.commit()
            QMessageBox.information(self, None, "OK")
        except Exception as e:
            logging.exception("import Arcaea Online error")
            QMessageBox.critical(
                self, "Import Error", "\n".join(traceback.format_exception(e))
            )

    @Slot()
    def on_exportScoresButton_clicked(self):
        scores = Database().export_scores()
        version = Database().version()
        content = json.dumps(scores, ensure_ascii=False)

        exportLocation, _filter = QFileDialog.getSaveFileName(
            self,
            "Save your scores to...",
            QDir.current().filePath(f"arcaea-offline-scores-v{version}.json"),
            "JSON (*.json);;*",
        )
        with open(exportLocation, "w", encoding="utf-8") as f:
            f.write(content)

    @Slot()
    def on_exportArcsongJsonButton_clicked(self):
        scores = Database().generate_arcsong()
        content = json.dumps(scores, ensure_ascii=False)

        exportLocation, _filter = QFileDialog.getSaveFileName(
            self,
            "Export arcsong.json",
            QDir.current().filePath("arcsong.json"),
            "JSON (*.json);;*",
        )
        with open(exportLocation, "w", encoding="utf-8") as f:
            f.write(content)

    @Slot()
    def on_exportSmartRteB30Button_clicked(self):
        try:
            with Database().sessionmaker() as session:
                converter = SmartRteB30CsvConverter(session)
                csvRows = converter.rows()

            exportLocation, _filter = QFileDialog.getSaveFileName(
                self,
                "Export CSV file",
                QDir.current().filePath("smartrte_scores.csv"),
                "CSV (*.csv);;*",
            )
            with open(exportLocation, "w", encoding="utf-8", newline="") as f:
                csvWriter = csv.writer(f)
                csvWriter.writerows(csvRows)

            QMessageBox.information(self, None, "OK")
        except Exception as e:
            logging.exception("Export SmartRTE csv error:")
            QMessageBox.critical(
                self, "Export Error", "\n".join(traceback.format_exception(e))
            )
