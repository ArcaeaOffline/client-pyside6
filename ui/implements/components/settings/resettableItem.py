from PySide6.QtWidgets import QSizePolicy, QWidget

from ui.designer.components.settings.resettableItem_ui import Ui_ResettableItem


class ResettableItem(Ui_ResettableItem, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setWidget(self, widget: QWidget):
        firstItem = self.horizontalLayout.itemAt(0)
        if firstItem.objectName() != "resetButton":
            self.horizontalLayout.removeItem(firstItem)

        sizePolicy = widget.sizePolicy()
        sizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        widget.setSizePolicy(sizePolicy)
        self.horizontalLayout.insertWidget(0, widget)
