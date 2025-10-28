import sys
from pathlib import Path

import structlog
from PySide6.QtCore import QCoreApplication, QEvent, QObject, Qt, QUrl
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from ui.resources import resources_rc  # noqa: F401
from ui.theme import ThemeManager
from ui.utils import url  # noqa: F401
from ui.viewmodels import overview  # noqa: F401

CURRENT_DIRECTORY = Path(__file__).resolve().parent
DEFAULT_FONTS = ["微软雅黑", "Microsoft YaHei UI", "Microsoft YaHei", "Segoe UI"]


logger: structlog.stdlib.BoundLogger = structlog.get_logger()


class ThemeChangeEventFilter(QObject):
    logger: structlog.stdlib.BoundLogger = structlog.get_logger(
        tag="ThemeChangeEventFilter",
    )

    def __init__(self, *, themeManager: ThemeManager):
        super().__init__(None)
        self.themeManager = themeManager

        self.scheme = self.themeManager.getCurrentScheme()

    def doSomething(self) -> None:
        scheme = self.themeManager.getCurrentScheme()
        if scheme == self.scheme:
            self.logger.debug("Ignored same scheme event (%r)", scheme)
            return

        self.scheme = scheme
        self.themeManager.updateTheme()
        self.logger.debug("something done")

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.ThemeChange:
            self.doSomething()

        return False


def main() -> None:
    app = QGuiApplication(sys.argv)
    app.setFont(DEFAULT_FONTS)
    app.setApplicationName("arcaea-offline-pyside-ui")
    app.setApplicationDisplayName("Arcaea Offline")
    app.setWindowIcon(QIcon(":/images/icon.png"))

    engine = QQmlApplicationEngine()

    themeManager = ThemeManager(parent=app)

    def onThemeManagerThemeChanged():
        logger.debug("App palette changed")
        app.setPalette(themeManager.qPalette)  # pyright: ignore[reportArgumentType]
        engine.rootContext().setContextProperty("appTheme", themeManager.qmlExposer)

    onThemeManagerThemeChanged()
    themeManager.themeChanged.connect(onThemeManagerThemeChanged)

    QQuickStyle.setStyle("Fusion")

    def onEngineObjectCreated(obj: QObject | None, objUrl: QUrl) -> None:
        if obj is None:
            logger.critical("rootObject is None! Exiting!")
            QCoreApplication.exit(-1)

    engine.objectCreated.connect(
        onEngineObjectCreated,
        Qt.ConnectionType.QueuedConnection,
    )

    engine.load("ui/qmls/App.qml")

    rootObject = engine.rootObjects()[0]
    ef = ThemeChangeEventFilter(themeManager=themeManager)
    rootObject.installEventFilter(ef)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
