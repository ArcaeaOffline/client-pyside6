from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget

from ui.designer.tabs.tabOverview_ui import Ui_TabOverview
from ui.extends.shared.language import LanguageChangeEventFilter


class TabOverview(Ui_TabOverview, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.db = Database()

    def showEvent(self, event: QShowEvent) -> None:
        self.updateOverview()
        return super().showEvent(event)

    def updateOverview(self):
        b30 = self.db.get_b30() or 0.00
        self.b30Label.setText(str(f"{b30:.3f}"))
        self.databaseDescribeLabel.setText(
            self.describeFormatString.format(
                self.db.count_packs(),
                self.db.count_songs(),
                self.db.count_difficulties(),
                self.db.count_chart_infos(),
                self.db.count_complete_chart_infos(),
                self.db.count_scores(),
            )
        )

    def retranslateUi(self, *args):
        super().retranslateUi(self)
        # fmt: off
        self.describeFormatString = QCoreApplication.translate("TabOverview", "databaseDescribeLabel {} {} {} {} {} {}")
        # fmt: on
