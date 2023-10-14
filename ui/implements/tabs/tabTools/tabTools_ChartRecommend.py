import logging

from arcaea_offline.calculate import calculate_constants_from_play_rating
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, ScoreBest
from arcaea_offline.utils.rating import rating_class_to_text
from arcaea_offline.utils.score import score_to_grade_text
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabTools.tabTools_ChartRecommend_ui import (
    Ui_TabTools_ChartRecommend,
)
from ui.extends.tabs.tabTools.tabTools_ChartRecommend import (
    ChartsModel,
    ChartsWithScoreBestModel,
    CustomChartDelegate,
    CustomScoreBestDelegate,
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

        self.chartsByConstantModel = ChartsModel(self)
        self.chartsRecommendFromPlayRatingModel = ChartsWithScoreBestModel(self)

        self.numLabelFormatString = "{} charts"

        self.chartDelegate = CustomChartDelegate(self)
        self.scoreBestDelegate = CustomScoreBestDelegate(self)
        self.chartsByConstant_modelView.setModel(self.chartsByConstantModel)
        self.chartsByConstant_modelView.setItemDelegate(self.chartDelegate)
        self.chartsRecommendFromPlayRating_modelView.setModel(
            self.chartsRecommendFromPlayRatingModel
        )
        self.chartsRecommendFromPlayRating_modelView.setItemDelegateForColumn(
            0, self.chartDelegate
        )
        self.chartsRecommendFromPlayRating_modelView.setItemDelegateForColumn(
            1, self.scoreBestDelegate
        )

        self.chartsRecommendFromPlayRating_playRatingSpinBox.valueChanged.connect(
            self.updateChartsRecommendFromPlayRating
        )
        self.chartsRecommendFromPlayRating_boundsSpinBox.valueChanged.connect(
            self.updateChartsRecommendFromPlayRating
        )

    @Slot(float)
    def on_rangeFromPlayRating_playRatingSpinBox_valueChanged(self, value: float):
        try:
            constant = round(
                value, self.rangeFromPlayRating_playRatingSpinBox.decimals()
            )
            result = calculate_constants_from_play_rating(constant)
            labels = [
                self.rangeFromPlayRating_ExPlusLabel,
                self.rangeFromPlayRating_ExLabel,
                self.rangeFromPlayRating_AaLabel,
                self.rangeFromPlayRating_ALabel,
                self.rangeFromPlayRating_BLabel,
                self.rangeFromPlayRating_CLabel,
            ]

            for label, constantRange in zip(
                labels,
                [result.EXPlus, result.EX, result.AA, result.A, result.B, result.C],
            ):
                label.setText(f"{constantRange[0]:.3f}~{constantRange[1]:.3f}")
        except Exception:
            logging.exception("Cannot calculate constant from play rating:")
            self.rangeFromPlayRating_ExPlusLabel.setText("...")
            self.rangeFromPlayRating_ExLabel.setText("...")
            self.rangeFromPlayRating_AaLabel.setText("...")

    @Slot(float)
    def on_chartsByConstant_constantSpinBox_valueChanged(self, value: float):
        constant = round(value, self.chartsByConstant_constantSpinBox.decimals())
        charts = self.db.get_charts_by_constant(int(constant * 10))
        chartsNum = len(charts)
        self.chartsByConstant_numLabel.setText(
            self.numLabelFormatString.format(chartsNum)
        )
        self.chartsByConstantModel.setCharts(charts)

    def updateChartsRecommendFromPlayRating(self):
        playRating = self.chartsRecommendFromPlayRating_playRatingSpinBox.value()
        bounds = self.chartsRecommendFromPlayRating_boundsSpinBox.value()
        charts = self.db.recommend_charts(
            round(
                playRating,
                self.chartsRecommendFromPlayRating_playRatingSpinBox.decimals(),
            ),
            round(
                bounds,
                self.chartsRecommendFromPlayRating_boundsSpinBox.decimals(),
            ),
        )
        chartsNum = len(charts)
        self.chartsRecommendFromPlayRating_numLabel.setText(
            self.numLabelFormatString.format(chartsNum)
        )
        scores = [self.db.get_score_best(c.song_id, c.rating_class) for c in charts]
        self.chartsRecommendFromPlayRatingModel.setChartAndScore(charts, scores)
        self.chartsRecommendFromPlayRating_modelView.resizeRowsToContents()
        self.chartsRecommendFromPlayRating_modelView.resizeColumnsToContents()
