import logging
import sys
import traceback
from datetime import datetime
from pathlib import Path

from arcaea_offline.database import Database
from PySide6.QtCore import QCoreApplication, QLocale
from PySide6.QtGui import QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

import ui.resources.resources_rc
from ui.extends.shared.language import changeAppLanguage
from ui.extends.shared.settings import Settings
from ui.implements.mainwindow import MainWindow
from ui.startup.databaseChecker import DatabaseChecker, DatabaseCheckerResult

rootLogger = logging.getLogger("root")
rootLogger.setLevel(logging.DEBUG)

rootLoggerFormatter = logging.Formatter(
    "[{levelname}]{asctime}|{name}: {msg}", "%m-%d %H:%M:%S", "{"
)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    rootLogger.critical(
        "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
    )


sys.excepthook = handle_exception


if __name__ == "__main__":
    QCoreApplication.setApplicationName("Arcaea Offline")

    logFolder = (Path(sys.argv[0]).parent / "logs").resolve()
    logFolder.mkdir(exist_ok=True)

    now = datetime.now()
    ymd = now.strftime("%Y%m%d")
    hms = now.strftime("%H%M%S")

    rootLoggerFileHandler = logging.FileHandler(
        str(logFolder / f"arcaea-offline-pyside-ui-{ymd}-{hms}_debug.log"),
        encoding="utf-8",
    )
    rootLoggerFileHandler.setLevel(logging.DEBUG)
    rootLoggerFileHandler.setFormatter(rootLoggerFormatter)
    rootLogger.addHandler(rootLoggerFileHandler)
    rootLoggerStdOutHandler = logging.StreamHandler(sys.stdout)
    rootLoggerStdOutHandler.setLevel(logging.INFO)
    rootLoggerStdOutHandler.setFormatter(rootLoggerFormatter)
    rootLogger.addHandler(rootLoggerStdOutHandler)

    app = QApplication(sys.argv)
    locale = (
        QLocale(Settings().language()) if Settings().language() else QLocale.system()
    )
    changeAppLanguage(locale)

    QFontDatabase.addApplicationFont(":/fonts/GeosansLight.ttf")

    databaseChecker = DatabaseChecker()
    databaseChecker.setWindowIcon(QIcon(":/images/icon.png"))
    databaseCheckResult = databaseChecker.confirmDb() if Settings().databaseUrl() else 0

    if not databaseCheckResult & DatabaseCheckerResult.Initted:
        result = databaseChecker.exec()

        if result == QDialog.DialogCode.Accepted:
            try:
                Database()
            except Exception as e:
                QMessageBox.critical(
                    None, "Database Error", "\n".join(traceback.format_exception(e))
                )
                sys.exit(1)
        else:
            sys.exit(1)

    window = MainWindow()
    window.setWindowIcon(QIcon(":/images/icon.png"))
    window.show()
    sys.exit(app.exec())
