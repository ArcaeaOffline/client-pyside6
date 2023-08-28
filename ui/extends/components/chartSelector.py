from arcaea_offline.database import Database
from arcaea_offline.models import Chart
from arcaea_offline.utils.rating import rating_class_to_short_text
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel


class FuzzySearchCompleterModel(QStandardItemModel):
    def fillDbFuzzySearchResults(self, db: Database, kw: str):
        self.clear()

        results = db.fuzzy_search_song_id(kw, limit=10)
        results = sorted(results, key=lambda r: r.confidence, reverse=True)
        songIds = [r.song_id for r in results]
        charts: list[Chart] = []
        for songId in songIds:
            dbChartRows = db.get_charts_by_song_id(songId)
            _charts = [Chart.from_db_row(dbRow) for dbRow in dbChartRows]
            _charts = sorted(_charts, key=lambda c: c.rating_class, reverse=True)
            charts += _charts

        for chart in charts:
            displayText = (
                f"{chart.name_en} [{rating_class_to_short_text(chart.rating_class)}]"
            )
            item = QStandardItem(kw)
            item.setData(kw)
            item.setData(displayText, Qt.ItemDataRole.UserRole + 75)
            item.setData(
                f"{chart.song_id}, {chart.package_id}", Qt.ItemDataRole.UserRole + 76
            )
            item.setData(chart, Qt.ItemDataRole.UserRole + 10)
            self.appendRow(item)
