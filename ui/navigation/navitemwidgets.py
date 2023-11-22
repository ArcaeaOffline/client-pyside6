from PySide6.QtCore import QObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from ui.navigation.navhost import NavHost, navHost
from ui.navigation.navitem import NavItem
from ui.navigation.navsidebar import NavigationSideBar


class DefaultParentNavItemWidget(QWidget):
    def __init__(self, navItem: NavItem, navItemChildren: list[NavItem], parent=None):
        super().__init__(parent)

        self.navItem = navItem

        self.partialNavHost = NavHost(self)
        self.partialNavHost.registerNavItem(navItem)
        for _navItem in navItemChildren:
            self.partialNavHost.registerNavItem(_navItem)
        self.partialNavHost.navigate(navItem.id)

        self.verticalLayout = QVBoxLayout(self)

        self.navItemLabelFont = QFont(self.font())
        self.navItemLabelFont.setPointSize(14)
        self.navItemLabel = QLabel(self)
        self.navItemLabel.setFont(self.navItemLabelFont)

        spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addSpacerItem(spacer)

        self.navSideBar = NavigationSideBar(self, self.partialNavHost)
        self.navSideBar.navigateUpButton.setEnabled(False)
        self.verticalLayout.addWidget(self.navSideBar)

        self.verticalLayout.addSpacerItem(spacer)

        self.retranslateUi()

    def retranslateUi(self):
        self.navItemLabel.setText(self.navItem.text())


class NavItemWidgets(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__map: dict[str, QWidget] = {}
        # this reference holds all the `DefaultParentNavItemWidget`s
        # since these widgets are created with no parents, not keeping a reference to
        # them may result in errors, even a silent app crash that is hard to debug
        self.__defaultParentWidgetRefs: dict[str, QWidget] = {}

    def register(self, navItemId: str, widget: QWidget):
        self.__map[navItemId] = widget

    def unregister(self, navItemId: str) -> bool:
        try:
            widget = self.__map.pop(navItemId)
            widget.deleteLater()
            return True
        except KeyError:
            return False

    def get(self, navItemId: str) -> QWidget | None:
        widget = self.__map.get(navItemId)
        if widget is not None:
            return widget
        elif navItemChildren := navHost.getNavItemRelatives(navItemId).children:
            if self.__defaultParentWidgetRefs.get(navItemId) is None:
                defaultParentNavItemWidget = DefaultParentNavItemWidget(
                    navHost.findNavItem(navItemId), navItemChildren
                )
                self.__defaultParentWidgetRefs[navItemId] = defaultParentNavItemWidget
                defaultParentNavItemWidget.partialNavHost.activated.connect(
                    lambda o, n: navHost.navigate(n.id)
                )

            return self.__defaultParentWidgetRefs.get(navItemId)
        else:
            return None
