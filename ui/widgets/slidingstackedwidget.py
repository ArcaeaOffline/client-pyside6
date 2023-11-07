"""
Adapted from https://github.com/Qt-Widgets/SlidingStackedWidget-1

    MIT License
    Copyright (c) 2020 Tim Schneeberger (ThePBone) <tim.schneeberger(at)outlook.de>
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""


from enum import IntEnum

from PySide6.QtCore import (
    QAbstractAnimation,
    QEasingCurve,
    QParallelAnimationGroup,
    QPoint,
    QPropertyAnimation,
    Signal,
)
from PySide6.QtWidgets import (
    QGraphicsEffect,
    QGraphicsOpacityEffect,
    QStackedWidget,
    QWidget,
)


class SlidingDirection(IntEnum):
    Auto = 0
    LeftToRight = 1
    RightToLeft = 2
    TopToBottom = 3
    BottomToTop = 4


class SlidingStackedWidget(QStackedWidget):
    slidingDirection = SlidingDirection

    animationFinished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.vertical = False
        self.speedMs = 300
        self.animationEasingCurve = QEasingCurve.Type.OutQuart
        self.animationCurrentIndex = 0
        self.animationNextIndex = 0
        self.animationCurrentPoint = QPoint(0, 0)
        self.animationRunning = False

        self.wrap = False
        self.opacityAnimation = False

    def setVertical(self, vertical: bool):
        self.vertical = vertical

    def setSpeedMs(self, speedMs: int):
        self.speedMs = speedMs

    def setAnimationEasingCurve(self, easingCurve: QEasingCurve.Type):
        self.animationEasingCurve = easingCurve

    def setWrap(self, wrap: bool):
        self.wrap = wrap

    def setOpacityAnimation(self, value: bool):
        self.opacityAnimation = value

    def slideInNext(self) -> bool:
        currentIndex = self.currentIndex()
        if self.wrap or (currentIndex < self.count() - 1):
            self.slideInIdx(currentIndex + 1)
        else:
            return False
        return True

    def slideInPrev(self) -> bool:
        currentIndex = self.currentIndex()
        if self.wrap or (currentIndex > 0):
            self.slideInIdx(currentIndex - 1)
        else:
            return False
        return True

    def slideInIdx(self, idx: int, direction: SlidingDirection = SlidingDirection.Auto):
        if idx > self.count() - 1:
            direction = (
                SlidingDirection.TopToBottom
                if self.vertical
                else SlidingDirection.RightToLeft
            )
            idx %= self.count()
        elif idx < 0:
            direction = (
                SlidingDirection.BottomToTop
                if self.vertical
                else SlidingDirection.LeftToRight
            )
            idx = (idx + self.count()) % self.count()

        self.slideInWgt(self.widget(idx), direction)

    def slideInWgt(self, newwidget: QWidget, direction: SlidingDirection):
        if self.animationRunning:
            return

        self.animationRunning = True

        autoDirection = SlidingDirection.LeftToRight

        currentIndex = self.currentIndex()
        nextIndex = self.indexOf(newwidget)
        if currentIndex == nextIndex:
            self.animationRunning = False
            return
        elif currentIndex < nextIndex:
            autoDirection = (
                SlidingDirection.TopToBottom
                if self.vertical
                else SlidingDirection.RightToLeft
            )
        else:
            autoDirection = (
                SlidingDirection.BottomToTop
                if self.vertical
                else SlidingDirection.LeftToRight
            )

        if direction == SlidingDirection.Auto:
            direction = autoDirection

        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()

        self.widget(nextIndex).setGeometry(0, 0, offsetX, offsetY)
        if direction == SlidingDirection.BottomToTop:
            offsetX = 0
            offsetY = -offsetY
        elif direction == SlidingDirection.TopToBottom:
            offsetX = 0
        elif direction == SlidingDirection.RightToLeft:
            offsetX = -offsetX
            offsetY = 0
        elif direction == SlidingDirection.LeftToRight:
            offsetY = 0

        nextPoint = self.widget(nextIndex).pos()
        currentPoint = self.widget(currentIndex).pos()
        self.animationCurrentPoint = currentPoint
        self.widget(nextIndex).move(nextPoint.x() - offsetX, nextPoint.y() - offsetY)

        self.widget(nextIndex).show()
        self.widget(nextIndex).raise_()

        currentWidgetAnimation = self.widgetPosAnimation(currentIndex)
        currentWidgetAnimation.setStartValue(QPoint(currentPoint.x(), currentPoint.y()))
        currentWidgetAnimation.setEndValue(
            QPoint(offsetX + currentPoint.x(), offsetY + currentPoint.y())
        )

        nextWidgetAnimation = self.widgetPosAnimation(nextIndex)
        nextWidgetAnimation.setStartValue(
            QPoint(-offsetX + nextPoint.x(), offsetY + nextPoint.y())
        )
        nextWidgetAnimation.setEndValue(QPoint(nextPoint.x(), nextPoint.y()))

        animationGroup = QParallelAnimationGroup(self)
        animationGroup.addAnimation(currentWidgetAnimation)
        animationGroup.addAnimation(nextWidgetAnimation)

        if self.opacityAnimation:
            currentWidgetOpacityEffect = QGraphicsOpacityEffect()
            currentWidgetOpacityEffectAnimation = self.widgetOpacityAnimation(
                currentIndex, currentWidgetOpacityEffect, 1, 0
            )

            nextWidgetOpacityEffect = QGraphicsOpacityEffect()
            nextWidgetOpacityEffect.setOpacity(0)
            nextWidgetOpacityEffectAnimation = self.widgetOpacityAnimation(
                nextIndex, nextWidgetOpacityEffect, 0, 1
            )

            animationGroup.addAnimation(currentWidgetOpacityEffectAnimation)
            animationGroup.addAnimation(nextWidgetOpacityEffectAnimation)

        animationGroup.finished.connect(self.animationDoneSlot)
        self.animationNextIndex = nextIndex
        self.animationCurrentIndex = currentIndex
        self.animationRunning = True
        animationGroup.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)

    def widgetPosAnimation(self, widgetIndex: int):
        result = QPropertyAnimation(self.widget(widgetIndex), b"pos")
        result.setDuration(self.speedMs)
        result.setEasingCurve(self.animationEasingCurve)
        return result

    def widgetOpacityAnimation(
        self, widgetIndex: int, graphicEffect: QGraphicsEffect, startValue, endValue
    ):
        self.widget(widgetIndex).setGraphicsEffect(graphicEffect)
        result = QPropertyAnimation(graphicEffect, b"opacity")
        result.setDuration(round(self.speedMs / 2))
        result.setStartValue(startValue)
        result.setEndValue(endValue)
        result.finished.connect(
            lambda: graphicEffect.deleteLater() if graphicEffect is not None else ...
        )
        return result

    def animationDoneSlot(self):
        self.setCurrentIndex(self.animationNextIndex)
        self.widget(self.animationCurrentIndex).hide()
        self.widget(self.animationCurrentIndex).move(self.animationCurrentPoint)
        self.animationRunning = False
        self.animationFinished.emit()
