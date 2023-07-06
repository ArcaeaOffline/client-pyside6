import traceback

from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication, QModelIndex
from PySide6.QtWidgets import QMessageBox, QWidget

from ui.designer.tabs.tabInputScore_ui import Ui_TabInputScore


class TabInputScore(Ui_TabInputScore, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.chartSelector.valueChanged.connect(self.updateScoreEditorChart)
        self.scoreEditor.accepted.connect(self.commit)

    def updateScoreEditorChart(self):
        chart = self.chartSelector.value()
        self.scoreEditor.setChart(chart)

    def commit(self):
        try:
            Database().insert_score(self.scoreEditor.value())
            self.scoreEditor.reset()
        except Exception as e:
            QMessageBox.critical(
                self,
                # fmt: off
                QCoreApplication.translate("General", "tracebackFormatExceptionOnly.title"),
                QCoreApplication.translate("General", "tracebackFormatExceptionOnly.content").format(traceback.format_exception_only(e))
                # fmt: on
            )
