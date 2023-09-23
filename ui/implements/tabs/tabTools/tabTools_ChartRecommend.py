import logging
import random

from arcaea_offline.calculate import calculate_constants_from_play_rating
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, ScoreBest
from arcaea_offline.utils.rating import rating_class_to_text
from arcaea_offline.utils.score import score_to_grade_text
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QWidget

from ui.designer.tabs.tabTools.tabTools_ChartRecommend_ui import (
    Ui_TabTools_ChartRecommend,
)

logger = logging.getLogger(__name__)


def chartToText(chart: Chart):
    return f"{chart.artist} - {chart.title}<br>({chart.song_id}) {rating_class_to_text(chart.rating_class)}"


def scoreBestToText(score: ScoreBest):
    return f"{score_to_grade_text(score.score)} {score.score} > {score.potential:.4f}"


class TabTools_ChartRecommend(Ui_TabTools_ChartRecommend, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.db = Database()

        self.chartsByConstant = []
        self.chartsRecommendFromPlayRating = []

        self.numLabelFormatString = "{} charts"

        self.chartsRecommendFromPlayRating_playRatingSpinBox.valueChanged.connect(
            self.updateChartsRecommendFromPlayRating
        )
        self.chartsRecommendFromPlayRating_boundsSpinBox.valueChanged.connect(
            self.updateChartsRecommendFromPlayRating
        )

        self.chartsByConstant_refreshButton.clicked.connect(self.fillChartsByConstant)
        self.chartsRecommendFromPlayRating_refreshButton.clicked.connect(
            self.fillChartsRecommendFromPlayRating
        )

    @Slot(float)
    def on_rangeFromPlayRating_playRatingSpinBox_valueChanged(self, value: float):
        try:
            result = calculate_constants_from_play_rating(value)
            exPlusLower, exPlusUpper = result.EXPlus
            exLower, exUpper = result.EX
            aaLower, aaUpper = result.AA

            self.rangeFromPlayRating_ExPlusLabel.setText(
                f"{exPlusLower:.3f}~{exPlusUpper:.3f}"
            )
            self.rangeFromPlayRating_ExLabel.setText(f"{exLower:.3f}~{exUpper:.3f}")
            self.rangeFromPlayRating_AaLabel.setText(f"{aaLower:.3f}~{aaUpper:.3f}")
        except Exception:
            logging.exception("cannot calculate constant from play rating")
            self.rangeFromPlayRating_ExPlusLabel.setText("...")
            self.rangeFromPlayRating_ExLabel.setText("...")
            self.rangeFromPlayRating_AaLabel.setText("...")

    def fillChartsByConstant(self):
        while item := self.chartsByConstant_gridLayout.takeAt(0):
            item.widget().deleteLater()

        charts = random.sample(
            self.chartsByConstant, k=min(len(self.chartsByConstant), 6)
        )
        row = 0
        for i, chart in enumerate(charts):
            if i % 3 == 0:
                row += 1
            label = QLabel(self)
            label.setText(chartToText(chart))
            self.chartsByConstant_gridLayout.addWidget(label, row, i % 3)

    @Slot(float)
    def on_chartsByConstant_constantSpinBox_valueChanged(self, value: float):
        self.chartsByConstant = self.db.get_charts_by_constant(int(value * 10))
        chartsNum = len(self.chartsByConstant)
        self.chartsByConstant_refreshButton.setEnabled(chartsNum > 6)
        self.chartsByConstant_numLabel.setText(
            self.numLabelFormatString.format(chartsNum)
        )
        self.fillChartsByConstant()

    def fillChartsRecommendFromPlayRating(self):
        while item := self.chartsRecommendFromPlayRating_gridLayout.takeAt(0):
            item.widget().deleteLater()

        charts = random.sample(
            self.chartsRecommendFromPlayRating,
            k=min(len(self.chartsRecommendFromPlayRating), 6),
        )
        row = 0
        for i, chart in enumerate(charts):
            if i % 3 == 0:
                row += 1
            scoreBest = self.db.get_score_best(chart.song_id, chart.rating_class)
            label = QLabel(self)
            label.setText(f"{chartToText(chart)}<br>-<br>{scoreBestToText(scoreBest)}")
            self.chartsRecommendFromPlayRating_gridLayout.addWidget(label, row, i % 3)

    def updateChartsRecommendFromPlayRating(self):
        playRating = self.chartsRecommendFromPlayRating_playRatingSpinBox.value()
        bounds = self.chartsRecommendFromPlayRating_boundsSpinBox.value()
        self.chartsRecommendFromPlayRating = self.db.recommend_charts(
            playRating, bounds
        )
        chartsNum = len(self.chartsRecommendFromPlayRating)
        self.chartsRecommendFromPlayRating_refreshButton.setEnabled(chartsNum > 6)
        self.chartsRecommendFromPlayRating_numLabel.setText(
            self.numLabelFormatString.format(chartsNum)
        )
        self.fillChartsRecommendFromPlayRating()
