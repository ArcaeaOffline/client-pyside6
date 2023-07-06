from PySide6.QtWidgets import QLineEdit


class FocusSelectAllLineEdit(QLineEdit):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.deselect()
