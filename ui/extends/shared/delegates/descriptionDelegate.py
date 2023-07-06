from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtWidgets import QStyle, QStyleOptionViewItem

from .base import TextSegmentDelegate


class DescriptionDelegate(TextSegmentDelegate):
    MainTextRole = Qt.ItemDataRole.UserRole + 75
    DescriptionTextRole = Qt.ItemDataRole.UserRole + 76

    def getMainText(self, index: QModelIndex) -> str | None:
        return index.data(self.MainTextRole)

    def getDescriptionText(self, index: QModelIndex) -> str | None:
        return index.data(self.DescriptionTextRole)

    def getTextSegments(self, index: QModelIndex, option):
        return [
            [
                {self.TextRole: self.getMainText(index) or ""},
                {self.TextRole: " "},
                {
                    self.TextRole: self.getDescriptionText(index) or "",
                    self.ColorRole: option.widget.palette().placeholderText().color(),
                },
            ]
        ]

    def paint(self, painter, option, index):
        super().paint(painter, option, index)

        optionNoText = QStyleOptionViewItem(option)
        optionNoText.text = ""
        style = option.widget.style()  # type: QStyle
        style.drawControl(QStyle.ControlElement.CE_ItemViewItem, optionNoText, painter)
