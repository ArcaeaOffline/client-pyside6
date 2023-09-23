from PySide6.QtCore import QPoint
from PySide6.QtGui import QGuiApplication, QScreen
from PySide6.QtWidgets import QWidget


def keepWidgetInScreen(widget: QWidget, screen: QScreen = None):
    """ensure your widget is visible"""

    # see https://doc.qt.io/qt-6/application-windows.html
    # for why using frameGeometry.width() / frameGeometry.height()
    # instead of width() / height().

    # https://stackoverflow.com/questions/49700394/qt-unable-to-set-geometry
    widget.adjustSize()

    screen = screen or QGuiApplication.primaryScreen()
    screenAvailableGeometry = screen.availableGeometry()

    # X boundary
    if widget.pos().x() < screenAvailableGeometry.x():
        pos = QPoint(widget.pos())
        pos.setX(screenAvailableGeometry.x())
        widget.move(pos)
    elif (
        widget.pos().x() + widget.frameGeometry().width()
        > screenAvailableGeometry.width()
    ):
        pos = QPoint(widget.pos())
        pos.setX(
            pos.x()
            - (
                pos.x()
                + widget.frameGeometry().width()
                - screenAvailableGeometry.width()
            )
        )
        widget.move(pos)

    # Y boundary
    if widget.pos().y() < screenAvailableGeometry.y():
        pos = QPoint(widget.pos())
        pos.setY(screenAvailableGeometry.y())
        widget.move(pos)
    elif (
        widget.pos().y() + widget.frameGeometry().height()
        > screenAvailableGeometry.height()
    ):
        pos = QPoint(widget.pos())
        pos.setY(
            pos.y()
            - (
                pos.y()
                + widget.frameGeometry().height()
                - screenAvailableGeometry.height()
            )
        )
        widget.move(pos)
