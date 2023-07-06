from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget

from ui.designer.tabs.tabAbout_ui import Ui_TabAbout


class TabAbout(Ui_TabAbout, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

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
