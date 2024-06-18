from PySide6.QtCore import Signal
from PySide6.QtWidgets import QButtonGroup, QDialog

from ui.designer.components.ocrQueueOptionsDialog_ui import Ui_OcrQueueOptionsDialog
from ui.extends.shared.settings import Settings


class OcrQueueOptionsDialog(QDialog, Ui_OcrQueueOptionsDialog):
    iccOptionsChanged = Signal(int)

    def __init__(self, parent=None):
        super(OcrQueueOptionsDialog, self).__init__(parent)
        self.setupUi(self)

        self.iccOptionButtonGroup = QButtonGroup(self)
        self.iccOptionButtonGroup.buttonToggled.connect(
            lambda: self.iccOptionsChanged.emit(self.iccOptionButtonGroup.checkedId())
        )
        self.iccOptionButtonGroup.addButton(self.iccUseQtRadioButton, 0)
        self.iccOptionButtonGroup.addButton(self.iccUsePILRadioButton, 1)
        self.iccOptionButtonGroup.addButton(self.iccTryFixRadioButton, 2)

        self.scoreDateSourceButtonGroup = QButtonGroup(self)
        self.scoreDateSourceButtonGroup.addButton(
            self.dateUseCreationDateRadioButton, 0
        )
        self.scoreDateSourceButtonGroup.addButton(self.dateUseModifyDateRadioButton, 1)
        self.scoreDateSourceButtonGroup.buttonClicked.connect(
            self.on_scoreDateSourceButtonGroup_buttonClicked
        )

        self.settings = Settings()
        self.settings.updated.connect(self.syncCheckboxesFromSettings)
        self.syncCheckboxesFromSettings()

    def syncCheckboxesFromSettings(self):
        scoreDateSource = self.settings.scoreDateSource()
        if scoreDateSource == "lastModified":
            self.dateUseModifyDateRadioButton.setChecked(True)
        else:
            self.dateUseCreationDateRadioButton.setChecked(True)

    def on_scoreDateSourceButtonGroup_buttonClicked(self, button):
        buttonId = self.scoreDateSourceButtonGroup.id(button)
        if buttonId == 1:
            self.settings.setScoreDateSource("lastModified")
        else:
            self.settings.setScoreDateSource("birthTime")
