from PySide6.QtCore import QFile, Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QTextBrowser, QWidget

from ui.designer.tabs.tabAbout_ui import Ui_TabAbout
from ui.extends.shared.language import LanguageChangeEventFilter


class TabAbout(Ui_TabAbout, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        logoPixmap = QPixmap(":/images/logo.png").scaled(
            300,
            300,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.logoLabel.setPixmap(logoPixmap)

    @Slot()
    def on_aboutQtButton_clicked(self):
        QMessageBox.aboutQt(self)

    @Slot()
    def on_versionInfoButton_clicked(self):
        textBrowser = QTextBrowser(self)
        textBrowser.setWindowFlag(Qt.WindowType.Dialog, True)
        textBrowser.setWindowTitle("version")
        versionFile = QFile(":/VERSION")
        versionFile.open(QFile.OpenModeFlag.ReadOnly)
        versionText = str(versionFile.readAll(), encoding="utf-8")
        versionFile.close()
        textBrowser.setText(versionText)
        textBrowser.show()

    @Slot()
    def on_licenseButton_clicked(self):
        textBrowser = QTextBrowser(self)
        textBrowser.setWindowFlag(Qt.WindowType.Dialog, True)
        textBrowser.setWindowTitle("LICENSE")
        licenseFile = QFile(":/LICENSE")
        licenseFile.open(QFile.OpenModeFlag.ReadOnly)
        licenseText = str(licenseFile.readAll(), encoding="utf-8")
        licenseFile.close()
        textBrowser.setText(licenseText)
        textBrowser.setMinimumSize(500, 400)
        textBrowser.show()
