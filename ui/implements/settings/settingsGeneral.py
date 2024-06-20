from PySide6.QtCore import QCoreApplication, QDir, QLocale
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QMessageBox,
    QPushButton,
)

from core.settings import SettingsKeys, settings
from ui.extends.shared.language import changeAppLanguage, localeToCode, localeToFullName
from ui.implements.settings.settingsBaseWidget import SettingsBaseWidget


class SettingsGeneral(SettingsBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        availableLanguageFiles = QDir(":/lang").entryInfoList()
        for fileInfo in availableLanguageFiles:
            if not fileInfo.isFile() or fileInfo.suffix() != "qm":
                continue
            languageCode = fileInfo.baseName()
            locale = QLocale(languageCode)
            self.languageValueWidget.addItem(localeToFullName(locale), locale)
            self.languageValueWidget.setCurrentIndex(-1)
        self.languageValueWidget.currentIndexChanged.connect(self.changeLanguage)
        self.languageFollowSystemCheckBox.toggled.connect(
            self.changeLanguageFollowSystem
        )
        if language := settings.stringValue(SettingsKeys.General.Language):
            locale = QLocale(language)
            index = self.languageValueWidget.findData(locale)
            if index > -1:
                self.languageValueWidget.setCurrentIndex(index)
        else:
            self.languageFollowSystemCheckBox.setChecked(True)
        self.insertItem("language", self.languageLabel, self.languageValueWidget)
        self.gridLayout.addWidget(
            self.languageFollowSystemCheckBox,
            self.gridLayout.rowCount() - 1,
            self.gridLayout.columnCount(),
        )

        self.dbUrlResetButton.clicked.connect(self.resetDbUrl)
        self.insertItem(
            "dbUrl",
            self.dbUrlLabel,
            QLabel(settings.stringValue(SettingsKeys.General.DatabaseUrl)),
            self.dbUrlResetButton,
        )

    def changeLanguage(self):
        locale = self.languageValueWidget.currentData()
        if locale:
            changeAppLanguage(locale)
            settings.setValue(SettingsKeys.General.Language, localeToCode(locale))

    def changeLanguageFollowSystem(self):
        followSystem = self.languageFollowSystemCheckBox.isChecked()
        self.languageValueWidget.setCurrentIndex(-1)
        if followSystem:
            settings.remove(SettingsKeys.General.Language)
            changeAppLanguage(QLocale.system())
            self.languageValueWidget.setEnabled(False)
        else:
            self.languageValueWidget.setEnabled(True)

    def resetDbUrl(self):
        userConfirm = QMessageBox.warning(
            self,
            None,
            QCoreApplication.translate("Settings", "general.dbUrlResetWarning"),
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.No,
        )
        if userConfirm == QMessageBox.StandardButton.Yes:
            settings.remove(SettingsKeys.General.DatabaseUrl)
            QApplication.instance().quit()

    def setupUi(self, *args):
        self.languageLabel = QLabel(self)
        self.languageValueWidget = QComboBox(self)
        self.languageFollowSystemCheckBox = QCheckBox(self)

        self.dbUrlLabel = QLabel(self)
        self.dbUrlResetButton = QPushButton(self)

        super().setupUi(self)
        self.retranslateUi()

    def retranslateUi(self, *args):
        super().retranslateUi(self)

        # fmt: off
        self.setTitle(QCoreApplication.translate("Settings", "general.title"))

        self.languageLabel.setText(QCoreApplication.translate("Settings", "general.language.label"))
        self.languageFollowSystemCheckBox.setText(QCoreApplication.translate("Settings", "general.language.followSystem"))

        self.dbUrlLabel.setText(QCoreApplication.translate("Settings", "general.dbUrl.label"))
        self.dbUrlResetButton.setText(QCoreApplication.translate("Settings", "resetButton"))
        # fmt: on
