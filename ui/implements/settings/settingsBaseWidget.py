from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

from ui.designer.settings.settingsBaseWidget_ui import Ui_SettingsBaseWidget
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.extends.shared.settings import Settings


class SettingsBaseWidget(Ui_SettingsBaseWidget, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = Settings()

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

    def setTitle(self, title: str):
        self.titleLabel.setText(title)

    def insertItem(
        self,
        prefix: str,
        label: QLabel,
        valueWidget: QWidget,
        resetButton: QPushButton | None = None,
    ):
        row = self.gridLayout.rowCount()

        label.setObjectName(f"{prefix}Label")
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(label, row, 0)

        valueWidget.setObjectName(f"{prefix}ValueWidget")
        self.gridLayout.addWidget(valueWidget, row, 1)

        if resetButton:
            resetButton.setObjectName(f"{prefix}ResetButton")
            self.gridLayout.addWidget(resetButton, row, 2)

    def setupUi(self, widget):
        super().setupUi(widget)
        self.gridLayout.setColumnStretch(1, 1)

    def retranslateUi(self, widget):
        super().retranslateUi(widget)
