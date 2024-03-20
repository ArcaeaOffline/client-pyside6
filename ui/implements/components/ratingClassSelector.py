from typing import Type

from PySide6.QtCore import Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QHBoxLayout, QSizePolicy, QVBoxLayout, QWidget

from ui.implements.components.ratingClassRadioButton import RatingClassRadioButton


class RatingClassSelector(QWidget):
    valueChanged = Signal()
    selected = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.preferredLayout = QHBoxLayout(self)
        self.preferredLayout.setSpacing(0)

        self.pstButton = RatingClassRadioButton(self)
        self.pstButton.setObjectName("pstButton")
        self.pstButton.setText("PAST")
        self.pstButton.setAutoExclusive(False)
        self.preferredLayout.addWidget(self.pstButton)

        self.prsButton = RatingClassRadioButton(self)
        self.prsButton.setObjectName("prsButton")
        self.prsButton.setText("PRESENT")
        self.prsButton.setAutoExclusive(False)
        self.preferredLayout.addWidget(self.prsButton)

        self.ftrButton = RatingClassRadioButton(self)
        self.ftrButton.setObjectName("ftrButton")
        self.ftrButton.setText("FUTURE")
        self.ftrButton.setAutoExclusive(False)
        self.preferredLayout.addWidget(self.ftrButton)

        self.bydButton = RatingClassRadioButton(self)
        self.bydButton.setObjectName("bydButton")
        self.bydButton.setText("BEYOND")
        self.bydButton.setAutoExclusive(False)
        self.preferredLayout.addWidget(self.bydButton)

        self.etrButton = RatingClassRadioButton(self)
        self.etrButton.setObjectName("etrButton")
        self.etrButton.setText("ETERNAL")
        self.etrButton.setAutoExclusive(False)
        self.preferredLayout.addWidget(self.etrButton)

        self.buttons = [
            self.pstButton,
            self.prsButton,
            self.ftrButton,
            self.bydButton,
            self.etrButton,
        ]
        self.pstButton.setColors(QColor("#399bb2"), QColor("#f0f8fa"))
        self.prsButton.setColors(QColor("#809955"), QColor("#f7f9f4"))
        self.ftrButton.setColors(QColor("#702d60"), QColor("#f7ebf4"))
        self.bydButton.setColors(QColor("#710f25"), QColor("#f9ced8"))
        self.etrButton.setColors(QColor("#4f2c7a"), QColor("#e4daf1"))

        self.pstButton.clicked.connect(self.select)
        self.prsButton.clicked.connect(self.select)
        self.ftrButton.clicked.connect(self.select)
        self.bydButton.clicked.connect(self.select)
        self.etrButton.clicked.connect(self.select)
        self.reset()
        self.setButtonsEnabled([])

    def setLayout(self, layoutType: Type[QVBoxLayout] | Type[QHBoxLayout]):
        while self.preferredLayout.takeAt(0):
            ...
        self.preferredLayout.destroyed.connect(lambda: self.__setLayout(layoutType))
        self.preferredLayout.deleteLater()

    def __setLayout(self, layoutType: Type[QVBoxLayout] | Type[QHBoxLayout]):
        self.preferredLayout = layoutType(self)
        self.preferredLayout.setSpacing(0)
        for button in self.buttons:
            if layoutType == QVBoxLayout:
                sizePolicy = QSizePolicy(
                    QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
                )
            else:
                sizePolicy = QSizePolicy(
                    QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
                )
            button.setSizePolicy(sizePolicy)
            self.preferredLayout.addWidget(button)
        self.update()

    def value(self):
        for i, button in enumerate(self.buttons):
            if button.isChecked():
                return i
        return None

    def reset(self):
        for button in self.buttons:
            button.setChecked(False)
        self.valueChanged.emit()

    def setButtonsEnabled(self, ratingClasses: list[int]):
        for i, button in enumerate(self.buttons):
            if i in ratingClasses:
                button.setEnabled(True)
            else:
                button.setChecked(False)
                button.setEnabled(False)
                self.valueChanged.emit()

    def select(self, ratingClass: int | bool | None = None):
        if not (
            type(ratingClass) == int
            or type(ratingClass) == bool
            or ratingClass is not None
        ):
            return

        if ratingClass is None or isinstance(ratingClass, bool):
            button = self.sender()
        elif ratingClass in range(4):
            button = self.buttons[ratingClass]
        else:
            return

        if not button.isEnabled():
            return

        self.reset()
        button.setChecked(True)
        self.valueChanged.emit()
        self.selected.emit(self.buttons.index(button))
