from arcaea_offline.database import Database
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabInputScore_ui import Ui_TabInputScore
from ui.extends.shared.language import LanguageChangeEventFilter


class TabInputScore(Ui_TabInputScore, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.chartAndScoreInput.scoreCommited.connect(self.commit)

    def commit(self):
        score = self.chartAndScoreInput.score()
        if not score:
            return
        Database().insert_score(score)
        self.chartAndScoreInput.scoreEditor.reset()
        self.chartAndScoreInput.scoreEditor.setChart(
            self.chartAndScoreInput.chartSelector.value()
        )
