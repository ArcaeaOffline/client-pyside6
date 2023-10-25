import logging

from arcaea_offline.calculate import calculate_constants_from_play_rating
from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Score
from arcaea_offline.utils.rating import rating_class_to_text
from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget

from ui.designer.tabs.tabTools.tabTools_ChartRecommend_ui import (
    Ui_TabTools_ChartRecommend,
)
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.extends.tabs.tabTools.tabTools_ChartRecommend import (
    ChartsModel,
    ChartsWithScoreBestModel,
    CustomChartDelegate,
    CustomScoreBestDelegate,
)
from ui.implements.components.playRatingCalculator import PlayRatingCalculator

logger = logging.getLogger(__name__)


class QuickPlayRatingCalculatorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.verticalLayout = QVBoxLayout(self)

        self.chartLabel = QLabel(self)
        self.verticalLayout.addWidget(self.chartLabel)

        self.playRatingCalculator = PlayRatingCalculator(self)
        self.verticalLayout.addWidget(self.playRatingCalculator)

        self.setMinimumWidth(400)

        self.playRatingCalculator.arcaeaScoreLineEdit.setFocus(
            Qt.FocusReason.PopupFocusReason
        )

    def setChart(self, chart: Chart):
        self.chartLabel.setText(
            f"{chart.title} {rating_class_to_text(chart.rating_class)} {chart.constant / 10}"
        )
        self.playRatingCalculator.setConstant(chart.constant)

    def setScore(self, score: Score):
        self.playRatingCalculator.arcaeaScoreLineEdit.setText(str(score))


class TabTools_ChartRecommend(Ui_TabTools_ChartRecommend, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

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

        self.chartsByConstant_modelView.doubleClicked.connect(
            self.openQuickPlayRatingCalculator_chartsByConstant
        )
        self.chartsRecommendFromPlayRating_modelView.doubleClicked.connect(
            self.openQuickPlayRatingCalculator_chartsRecommendFromPlayRating
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

    @Slot(QModelIndex)
    def openQuickPlayRatingCalculator_chartsByConstant(self, index: QModelIndex):
        dialog = QuickPlayRatingCalculatorDialog(self)
        chart = index.data(ChartsModel.ChartRole)
        dialog.setChart(chart)
        dialog.show()

    @Slot(QModelIndex)
    def openQuickPlayRatingCalculator_chartsRecommendFromPlayRating(
        self, index: QModelIndex
    ):
        dialog = QuickPlayRatingCalculatorDialog(self)

        row = index.row()
        chartIndex = self.chartsRecommendFromPlayRatingModel.item(row, 0)
        scoreIndex = self.chartsRecommendFromPlayRatingModel.item(row, 1)

        chart = chartIndex.data(ChartsWithScoreBestModel.ChartRole)
        score: Score = scoreIndex.data(ChartsWithScoreBestModel.ScoreBestRole)
        dialog.setChart(chart)
        dialog.setScore(score.score)
        dialog.show()
