from PySide6.QtCore import QEasingCurve, QObject, QSize, Qt, QTimeLine
from PySide6.QtGui import QIcon, QPainter, QPaintEvent, QPixmap
from PySide6.QtWidgets import (
    QAbstractButton,
    QButtonGroup,
    QGraphicsColorizeEffect,
    QLabel,
    QWidget,
)

from ui.designer.tabs.tabTools.tabTools_StepCalculator_ui import (
    Ui_TabTools_StepCalculator,
)


class MapTypeListWidgetWidget(QLabel):
    def paintEvent(self, e: QPaintEvent) -> None:
        size = self.size()
        painter = QPainter(self)
        scaledPixmap = self.pixmap().scaled(
            size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        x = (size.width() - scaledPixmap.width()) / 2
        y = (size.height() - scaledPixmap.height()) / 2
        painter.drawPixmap(x, y, scaledPixmap)


class ButtonGrayscaleEffectApplier(QObject):
    def __init__(self, parent: QAbstractButton):
        super().__init__(parent)
        self.timeline = QTimeLine(500, self)
        self.timeline.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.timeline.frameChanged.connect(self.applyGrayscaleEffect)

        parent.toggled.connect(self.triggerEffectAnimation)
        self.triggerEffectAnimation(parent.isChecked())

    def triggerEffectAnimation(self, buttonEnabled: bool):
        if self.timeline.state() == QTimeLine.State.Running:
            self.timeline.stop()
        startFrame = self.timeline.currentFrame()
        stopFrame = 0 if buttonEnabled else 100

        self.timeline.setFrameRange(startFrame, stopFrame)
        self.timeline.start()

    def applyGrayscaleEffect(self, frame: int):
        target: QAbstractButton = self.parent()
        value = frame / 100

        effect = QGraphicsColorizeEffect(target)
        effect.setColor("#000000")
        effect.setStrength(value)
        target.setGraphicsEffect(effect)


class TabTools_StepCalculator(Ui_TabTools_StepCalculator, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        staminaIcon = QIcon(":/images/stepCalculator/stamina.png")
        for radioButton in [
            self.legacyPlayPlus_x2StaminaRadioButton,
            self.legacyPlayPlus_x4StaminaRadioButton,
            self.legacyPlayPlus_x6StaminaRadioButton,
        ]:
            radioButton.setIcon(staminaIcon)
            radioButton.setIconSize(QSize(25, 15))

        memoryBoostIcon = QIcon(":/images/stepCalculator/memory-boost.png")
        self.play_memoryBoostCheckBox.setIcon(memoryBoostIcon)
        self.play_memoryBoostCheckBox.setIconSize(QSize(75, 100))

        mapTypeIconSize = QSize(150, 50)

        for button, pixmap in zip(
            [
                self.mapTypeLegacyPlayRadioButton,
                self.mapTypeLegacyPlayPlusRadioButton,
                self.mapTypePlayRadioButton,
            ],
            [
                QPixmap(":/images/stepCalculator/legacy-play.png"),
                QPixmap(":/images/stepCalculator/legacy-play-plus.png"),
                QPixmap(":/images/stepCalculator/play.png"),
            ],
        ):
            button.setIconSize(mapTypeIconSize)
            button.setIcon(pixmap)

        self.buttonGrayscaleEffectAppliers = []
        for button in [
            self.mapTypeLegacyPlayRadioButton,
            self.mapTypeLegacyPlayPlusRadioButton,
            self.mapTypePlayRadioButton,
            self.legacyPlayPlus_x2StaminaRadioButton,
            self.legacyPlayPlus_x4StaminaRadioButton,
            self.legacyPlayPlus_x6StaminaRadioButton,
            self.play_memoryBoostCheckBox,
        ]:
            applier = ButtonGrayscaleEffectApplier(button)
            self.buttonGrayscaleEffectAppliers.append(applier)

        self.mapTypeButtonGroup = QButtonGroup(self)
        self.mapTypeButtonGroup.addButton(self.mapTypeLegacyPlayRadioButton, 0)
        self.mapTypeButtonGroup.addButton(self.mapTypeLegacyPlayPlusRadioButton, 1)
        self.mapTypeButtonGroup.addButton(self.mapTypePlayRadioButton, 2)

        self.mapTypeButtonGroup.idToggled.connect(self.stackedWidget.setCurrentIndex)
        self.mapTypePlayRadioButton.setChecked(True)
