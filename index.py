import logging
import sys
import traceback

from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication, QLibraryInfo, QLocale, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

import ui.resources.images.images_rc
import ui.resources.translations.translations_rc
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

    locale = QLocale.system()
    translator = QTranslator()
    translator_load_success = translator.load(QLocale.system(), "", "", ":/lang/")
    if not translator_load_success:
        translator.load(":/lang/en_US.qm")
    baseTranslator = QTranslator()
    baseTranslator.load(
        QLocale.system(),
        "qt",
        "_",
        QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath),
    )
    app = QApplication(sys.argv)

    app.installTranslator(translator)
    app.installTranslator(baseTranslator)

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
