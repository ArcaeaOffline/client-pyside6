from PySide6.QtCore import QCoreApplication, Slot
from PySide6.QtWidgets import QListWidgetItem, QWidget

from ui.designer.tabs.tabSettings_ui import Ui_TabSettings
from ui.extends.shared.language import LanguageChangeEventFilter
from ui.implements.settings.settingsAndreal import SettingsAndreal
from ui.implements.settings.settingsGeneral import SettingsGeneral
from ui.implements.settings.settingsOcr import SettingsOcr


class SettingsLabelItem(QListWidgetItem):
    def __init__(self, translatorKey: str):
        super().__init__()
        self.translatorKey = translatorKey
        self.retranslateUi()

    def retranslateUi(self):
        self.setText(QCoreApplication.translate("Settings", self.translatorKey))


class TabSettings(Ui_TabSettings, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.listWidget.itemClicked.connect(self.switchPage)

        self.listWidget.addItem(self.settingsGeneralLabel)
        self.stackedWidget.addWidget(self.settingsGeneral)

        self.listWidget.addItem(self.settingsOcrLabel)
        self.stackedWidget.addWidget(self.settingsOcr)

        self.listWidget.addItem(self.settingsAndrealLabel)
        self.stackedWidget.addWidget(self.settingsAndreal)

        self.listWidget.setCurrentRow(self.stackedWidget.currentIndex())

    @Slot(QListWidgetItem)
    def switchPage(self, item: QListWidgetItem):
        item.setSelected(True)
        self.stackedWidget.setCurrentIndex(self.listWidget.indexFromItem(item).row())

    def setupUi(self, *args):
        self.settingsGeneralLabel = SettingsLabelItem("general.title")
        self.settingsGeneral = SettingsGeneral(self)
        self.settingsOcrLabel = SettingsLabelItem("ocr.title")
        self.settingsOcr = SettingsOcr(self)
        self.settingsAndrealLabel = SettingsLabelItem("andreal.title")
        self.settingsAndreal = SettingsAndreal(self)
        super().setupUi(self)

    def retranslateUi(self, *args):
        super().retranslateUi(self)

        self.settingsGeneralLabel.retranslateUi()
        self.settingsGeneral.retranslateUi()
        self.settingsOcrLabel.retranslateUi()
        self.settingsOcr.retranslateUi()
        self.settingsAndrealLabel.retranslateUi()
        self.settingsAndreal.retranslateUi()
