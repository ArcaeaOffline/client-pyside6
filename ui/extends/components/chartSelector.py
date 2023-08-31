from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from arcaea_offline.searcher import Searcher
from arcaea_offline.utils.rating import rating_class_to_short_text
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel


class SearchCompleterModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.searcher = Searcher()
        self.db = Database()

    def updateSearcherSongs(self):
        with self.db.sessionmaker() as session:
            self.searcher.import_songs(session)

    def getSearchResult(self, kw: str):
        self.clear()

        songIds = self.searcher.search(kw)

        charts: list[Chart] = []
        for songId in songIds:
            _charts = self.db.get_charts_by_song_id(songId)
            _charts = sorted(_charts, key=lambda c: c.rating_class, reverse=True)
            charts += _charts

        for chart in charts:
            displayText = (
                f"{chart.title} [{rating_class_to_short_text(chart.rating_class)}]"
            )
            item = QStandardItem(kw)
            item.setData(kw)
            item.setData(displayText, Qt.ItemDataRole.UserRole + 75)
            item.setData(f"{chart.song_id}, {chart.set}", Qt.ItemDataRole.UserRole + 76)
            item.setData(chart, Qt.ItemDataRole.UserRole + 10)
            self.appendRow(item)
