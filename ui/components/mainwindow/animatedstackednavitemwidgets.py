from PySide6.QtWidgets import QWidget

from ui.navigation.navhost import NavHost, navHost
from ui.navigation.navitem import NavItem
from ui.navigation.navitemwidgets import NavItemWidgets
from ui.widgets.slidingstackedwidget import SlidingStackedWidget


class AnimatedStackedNavItemsWidgets(SlidingStackedWidget):
    def __init__(
        self, navItemWidgets: NavItemWidgets, navHost: NavHost = navHost, parent=None
    ):
        super().__init__(parent)

        self.navItemWidgets = navItemWidgets
        self.navHost = navHost

        self.navHost.activated.connect(self.__switchTo)
        self.animationFinished.connect(self.endChangingWidget)

    def __switchTo(self, oldNavItem: NavItem, newNavItem: NavItem):
        oldNavItemDepth = self.navHost.getNavItemDepth(oldNavItem.id)
        newNavItemDepth = self.navHost.getNavItemDepth(newNavItem.id)

        if oldNavItemDepth != newNavItemDepth:
            slidingDirection = (
                self.slidingDirection.RightToLeft
                if newNavItemDepth > oldNavItemDepth
                else self.slidingDirection.LeftToRight
            )
        else:
            slidingDirection = self.slidingDirection.TopToBottom

        newWidget = self.navItemWidgets.get(newNavItem.id) or QWidget()
        self.startChangingWidget(newWidget, slidingDirection)

    def startChangingWidget(self, newWidget: QWidget, slidingDirection):
        newIndex = self.addWidget(newWidget)
        [self.widget(i).setEnabled(False) for i in range(self.count())]
        self.slideInIdx(newIndex, slidingDirection)

    def endChangingWidget(self):
        oldWidget = self.widget(0)
        self.removeWidget(oldWidget)

        newWidget = self.widget(0)
        newWidget.setEnabled(True)
