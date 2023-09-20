from ui.designer.components.chartAndScoreInput_ui import Ui_ChartAndScoreInput
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui.implements.components.songIdSelector import SongIdSelectorMode

class ChartAndScoreInput(Ui_ChartAndScoreInput, QWidget):
    scoreCommited = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.chartSelector.valueChanged.connect(self.updateScoreEditorChart)
        self.scoreEditor.accepted.connect(self.commit)

    def updateScoreEditorChart(self):
        chart = self.chartSelector.value()
        self.scoreEditor.setChart(chart)

    def commit(self):
        self.scoreCommited.emit()

    def setSongIdSelectorMode(self, mode: SongIdSelectorMode):
        self.chartSelector.setSongIdSelectorMode(mode)
        
    def value(self):
        return self.scoreEditor.value()
