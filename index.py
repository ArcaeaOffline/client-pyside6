import logging
import sys
import traceback

from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication, QLocale
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

import ui.resources.resources_rc
from ui.extends.shared.language import changeAppLanguage
from ui.extends.shared.settings import Settings
from ui.implements.mainwindow import MainWindow
from ui.startup.databaseChecker import DatabaseChecker

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    force=True,
    format="[{levelname}]{asctime}|{name}: {msg}",
    datefmt="%m-%d %H:%M:%S",
    style="{",
)

if __name__ == "__main__":
    QCoreApplication.setApplicationName("Arcaea Offline")

    app = QApplication(sys.argv)
    locale = (
        QLocale(Settings().language()) if Settings().language() else QLocale.system()
    )
    changeAppLanguage(locale)

    databaseChecker = DatabaseChecker()
    result = databaseChecker.exec()

    if result == QDialog.DialogCode.Accepted:
        try:
            Database()
        except Exception as e:
            QMessageBox.critical(
                None, "Database Error", "\n".join(traceback.format_exception(e))
            )
            sys.exit(1)

        window = MainWindow()
        window.setWindowIcon(QIcon(":/images/icon.png"))
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit(1)
