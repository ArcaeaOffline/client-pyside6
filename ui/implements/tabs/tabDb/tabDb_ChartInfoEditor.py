import logging

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, ChartInfo, Difficulty, Song
from arcaea_offline.utils.rating import rating_class_to_text
from PySide6.QtCore import QCoreApplication, QModelIndex, Qt, Slot
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QStandardItem
from PySide6.QtWidgets import QApplication, QMessageBox, QStyledItemDelegate, QWidget
from sqlalchemy import select

from ui.designer.tabs.tabDb.tabDb_ChartInfoEditor_ui import Ui_TabDb_ChartInfoEditor
from ui.extends.shared.data import Data
from ui.extends.shared.database import databaseUpdateSignals
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.extends.tabs.tabDb.tabDb_ChartInfoEditor import (
    ChartInfoAbsentModel,
    ListViewDelegate,
)
from ui.implements.components.songIdSelector import SongIdSelectorMode

logger = logging.getLogger(__name__)


class TabDb_ChartInfoEditor(Ui_TabDb_ChartInfoEditor, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.db = Database()

        self.numberRegexValidator = QRegularExpressionValidator(r"^\d+$", self)
        self.constantLineEdit.setValidator(self.numberRegexValidator)
        self.notesLineEdit.setValidator(self.numberRegexValidator)

        self.constantLineEdit.textChanged.connect(self.updateConstantPreviewLabel)

        self.chartInfoAbsentModel = ChartInfoAbsentModel(self)
        self.listView.setModel(self.chartInfoAbsentModel)
        self.listViewDelegate = ListViewDelegate(self)

        self.listView.selectionModel().currentChanged.connect(
            self.listViewSelectionChanged
        )

        self.chartSelector.setSongIdSelectorMode(SongIdSelectorMode.SongId)
        self.chartSelector.valueChanged.connect(self.chartSelectorValueChanged)

        databaseUpdateSignals.songDataUpdated.connect(self.updateChartInfoAbsentModel)
        self.updateChartInfoAbsentModel()

        self.commitButton.clicked.connect(self.commitChartInfo)
        self.deleteButton.clicked.connect(self.deleteChartInfo)

    def updateConstantPreviewLabel(self):
        text = self.constantLineEdit.text()
        if self.constantLineEdit.hasAcceptableInput():
            self.constantPreviewLabel.setText(f"> {int(text) / 10:.1f}")
        else:
            self.constantPreviewLabel.setText("> ...")

    def reset(self):
        self.jacketLabel.clear()
        self.titleLabel.setText("...")
        self.ratingLabel.setText("...")
        self.constantLineEdit.setText("")
        self.notesLineEdit.setText("")

    def updateChartInfoAbsentModel(self):
        self.listView.setItemDelegate(QStyledItemDelegate())
        self.chartInfoAbsentModel.clear()
        self.chartInfoAbsentModel.appendRow(QStandardItem("Loading..."))
        QApplication.processEvents()

        with self.db.sessionmaker() as session:
            stmt = (
                select(Difficulty)
                .join(
                    ChartInfo,
                    (Difficulty.song_id == ChartInfo.song_id)
                    & (Difficulty.rating_class == ChartInfo.rating_class),
                    isouter=True,
                )
                .where(ChartInfo.notes.is_(None))
            )
            absentInfoDifficulties = sorted(
                list(session.scalars(stmt)),
                key=lambda d: f"{d.song_id},{d.rating_class}",
            )
            songIds = sorted(list(set(d.song_id for d in absentInfoDifficulties)))
            songsStmt = select(Song).where(Song.id.in_(songIds))
            songs = sorted(list(session.scalars(songsStmt)), key=lambda s: s.id)

        modelSongs = []
        for difficulty in absentInfoDifficulties:
            songIndex = songIds.index(difficulty.song_id)
            modelSongs.append(songs[songIndex])
        self.chartInfoAbsentModel.setCustomData(modelSongs, absentInfoDifficulties)
        self.listView.setItemDelegate(self.listViewDelegate)

    @Slot(QModelIndex)
    def listViewSelectionChanged(self, current: QModelIndex):
        if current.row() < 0 or current.column() < 0:
            return

        song: Song = current.data(ChartInfoAbsentModel.SongRole)
        difficulty: Difficulty = current.data(ChartInfoAbsentModel.DifficultyRole)
        self.chartSelector.selectChart(
            Chart(
                song_id=difficulty.song_id,
                rating_class=difficulty.rating_class,
                set=song.set,
            )
        )

    def chartSelectorValueChanged(self):
        if chart := self.chartSelector.value():
            self.fillChartInfo(chart.song_id, chart.rating_class)
        else:
            self.reset()

    def fillChartInfo(self, songId: str, ratingClass: int):
        song = self.db.get_song(songId)
        difficulty = self.db.get_difficulty(songId, ratingClass)

        self.titleLabel.setText(difficulty.title or song.title)
        self.ratingLabel.setText(
            rating_class_to_text(difficulty.rating_class)
            + " "
            + str(difficulty.rating)
            + ("+" if difficulty.rating_plus else "")
        )

        jacketPath = Data().getJacketPath(song, difficulty)
        if not jacketPath:
            pixmap = QPixmap(":/images/jacket-placeholder.png")
        else:
            pixmap = QPixmap(str(jacketPath.resolve()))
        self.jacketLabel.setPixmap(
            pixmap.scaled(
                self.jacketLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

        chartInfo = self.db.get_chart_info(songId, ratingClass)
        if chartInfo is not None:
            if chartInfo.constant is not None:
                self.constantLineEdit.setText(str(chartInfo.constant))
            if chartInfo.notes is not None:
                self.notesLineEdit.setText(str(chartInfo.notes))
        else:
            self.constantLineEdit.setText("")
            self.notesLineEdit.setText("")

    def commitChartInfo(self):
        chart = self.chartSelector.value()

        if not chart:
            QMessageBox.critical(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("TabDb_ChartInfoEditor", "commit.chartNotSelected"),
                # fmt: on
            )
            return
        if not self.constantLineEdit.hasAcceptableInput():
            QMessageBox.critical(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("TabDb_ChartInfoEditor", "commit.constantRequired"),
                # fmt: on
            )
            return

        constant = int(self.constantLineEdit.text())
        notes = (
            int(self.notesLineEdit.text())
            if self.notesLineEdit.hasAcceptableInput()
            else None
        )
        chartInfo = ChartInfo(
            song_id=chart.song_id,
            rating_class=chart.rating_class,
            constant=constant,
            notes=notes,
        )
        with self.db.sessionmaker() as session:
            session.merge(chartInfo)
            session.commit()
        databaseUpdateSignals.songDataUpdated.emit()

    def deleteChartInfo(self):
        chart = self.chartSelector.value()

        if not chart:
            QMessageBox.critical(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("TabDb_ChartInfoEditor", "commit.chartNotSelected"),
                # fmt: on
            )
            return

        chartInfo = self.db.get_chart_info(chart.song_id, chart.rating_class)
        if chartInfo:
            result = QMessageBox.warning(
                self,
                None,
                # fmt: off
                QCoreApplication.translate("TabDb_ChartInfoEditor", "deleteConfirm"),
                # fmt: on
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No,
            )
            if result == QMessageBox.StandardButton.Yes:
                with self.db.sessionmaker() as session:
                    session.delete(chartInfo)
                    session.commit()
                databaseUpdateSignals.songDataUpdated.emit()
