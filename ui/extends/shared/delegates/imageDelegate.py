from PySide6.QtCore import QFileInfo, QModelIndex, QRect, QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QStyledItemDelegate, QWidget


class ImageDelegate(QStyledItemDelegate):
    def getPixmap(self, index: QModelIndex):
        raise NotImplementedError("getPixmap not implemented.")

    def getImagePath(self, index: QModelIndex):
        raise NotImplementedError("getImagePath not implemented.")

    def scalePixmap(self, pixmap: QPixmap):
        return pixmap.scaled(
            100,
            100,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def paint(self, painter, option, index):
        pixmap = self.getPixmap(index)
        if not isinstance(pixmap, QPixmap):
            imagePath = self.getImagePath(index)
            option.text = imagePath
            super().paint(painter, option, index)
        else:
            pixmap = self.scalePixmap(pixmap)
            # https://stackoverflow.com/a/32047499/16484891
            # CC BY-SA 3.0
            x = option.rect.center().x() - pixmap.rect().width() / 2
            y = option.rect.center().y() - pixmap.rect().height() / 2

            painter.drawPixmap(
                QRect(x, y, pixmap.rect().width(), pixmap.rect().height()), pixmap
            )

    def sizeHint(self, option, index) -> QSize:
        pixmap = self.getPixmap(index)
        if isinstance(pixmap, QPixmap):
            pixmap = self.scalePixmap(pixmap)
            return pixmap.size()
        else:
            return QSize(100, 75)

    def createEditor(self, parent, option, index) -> QWidget:
        pixmap = self.getPixmap(index)
        if isinstance(pixmap, QPixmap):
            label = QLabel(parent)
            label.setWindowFlags(Qt.WindowType.Window)
            label.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
            label.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
            label.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, True)
            label.setWindowTitle(QFileInfo(self.getImagePath(index)).fileName())
            pixmap = pixmap.scaled(
                800,
                800,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            label.setMinimumSize(pixmap.size())
            label.setPixmap(pixmap)
            label.move(parent.mapToGlobal(parent.pos()))
            return label

    def setModelData(self, *args):
        ...

    def updateEditorGeometry(self, *args):
        ...
