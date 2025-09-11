import logging
import sys
from pathlib import Path

from PySide6.QtCore import QCoreApplication, QObject, Qt, QUrl
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from ui.resources import resources_rc  # noqa: F401
from ui.utils import url  # noqa: F401
from ui.viewmodels import overview  # noqa: F401

CURRENT_DIRECTORY = Path(__file__).resolve().parent
DEFAULT_FONTS = ["微软雅黑", "Microsoft YaHei UI", "Microsoft YaHei", "Segoe UI"]

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)


def main() -> None:
    app = QGuiApplication(sys.argv)
    app.setFont(DEFAULT_FONTS)
    app.setApplicationName("arcaea-offline-pyside-ui")
    app.setApplicationDisplayName("Arcaea Offline")
    app.setWindowIcon(QIcon(":/images/icon.png"))

    QQuickStyle.setStyle("Fusion")

    engine = QQmlApplicationEngine()

    def onEngineObjectCreated(obj: QObject | None, objUrl: QUrl) -> None:
        if obj is None:
            logger.critical("rootObject is None! Exiting!")
            QCoreApplication.exit(-1)

    engine.objectCreated.connect(
        onEngineObjectCreated,
        Qt.ConnectionType.QueuedConnection,
    )

    engine.load("ui/qmls/App.qml")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
