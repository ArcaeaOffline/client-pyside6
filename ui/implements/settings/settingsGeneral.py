import sys

from PySide6.QtCore import QCoreApplication, QDir, QLocale, QProcess
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QMessageBox,
    QPushButton,
)

from ui.extends.shared.language import changeAppLanguage, localeToCode, localeToFullName
from ui.extends.shared.settings import DATABASE_URL, LANGUAGE
from ui.implements.settings.settingsBaseWidget import SettingsBaseWidget


class SettingsGeneral(SettingsBaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        availableLanguageFiles = QDir(":/lang").entryInfoList(QDir.Filter.Files)
        for fileInfo in availableLanguageFiles:
            languageCode = fileInfo.baseName()
            locale = QLocale(languageCode)
            self.languageValueWidget.addItem(localeToFullName(locale), locale)
            self.languageValueWidget.setCurrentIndex(-1)
        self.languageValueWidget.currentIndexChanged.connect(self.changeLanguage)
        self.languageFollowSystemCheckBox.toggled.connect(
            self.changeLanguageFollowSystem
        )
        if self.settings.language():
            locale = QLocale(self.settings.language())
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
            QLabel(self.settings.databaseUrl()),
            self.dbUrlResetButton,
        )

    def changeLanguage(self):
        locale = self.languageValueWidget.currentData()
        if locale:
            changeAppLanguage(locale)
            self.settings.setLanguage(localeToCode(locale))

    def changeLanguageFollowSystem(self):
        followSystem = self.languageFollowSystemCheckBox.isChecked()
        self.languageValueWidget.setCurrentIndex(-1)
        if followSystem:
            self.settings.remove(LANGUAGE)
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
            self.settings.remove(DATABASE_URL)
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
