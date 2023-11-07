from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QFont, QIcon, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ui.navigation.navhost import NavItem, navHost
from ui.widgets.slidingstackedwidget import SlidingStackedWidget


class NavItemListWidget(QListWidget):
    NavItemRole = Qt.ItemDataRole.UserRole

    def __init__(self, parent=None):
        super().__init__(parent)

        font = QFont(self.font())
        font.setPointSize(14)
        self.setFont(font)

        self.clicked.connect(self.activated)

    def setNavItems(self, items: list[NavItem]):
        self.clear()

        for navItem in items:
            if navItem.icon:
                listWidgetItem = QListWidgetItem(QIcon(navItem.icon), navItem.text())
            else:
                listWidgetItem = QListWidgetItem(navItem.text())
            listWidgetItem.setData(self.NavItemRole, navItem)
            listWidgetItem.setTextAlignment(
                Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignVCenter
            )

            self.addItem(listWidgetItem)

    def selectNavItem(self, navItemId: str):
        navItemIds = [
            self.item(r).data(self.NavItemRole).id for r in range(self.count())
        ]
        index = navItemIds.index(navItemId)
        self.setCurrentIndex(self.model().index(index, 0))


class NavigationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.navHost = navHost

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.backButton = QPushButton(QIcon(":/icons/back.svg"), "")
        self.backButton.setFlat(True)
        self.backButton.setFixedHeight(20)
        self.verticalLayout.addWidget(self.backButton)

        self.navListWidget = NavItemListWidget(self)
        self.verticalLayout.addWidget(self.navListWidget)

    def setNavigationItems(self, items: list[NavItem]):
        self.navListWidget.setNavItems(items)


class NavigationSideBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.navHost = navHost

        navHost.navItemsChanged.connect(self.reloadNavWidget)
        navHost.activated.connect(self.navItemActivated)

        self.navigateUpKeyboardShortcut = QShortcut(
            QKeySequence(Qt.Modifier.ALT | Qt.Key.Key_Left),
            self,
            self.navHost.navigateUp,
        )

        self.verticalLayout = QVBoxLayout(self)

        self.navigateUpButton = QPushButton(QIcon(":/icons/back.svg"), "")
        self.navigateUpButton.setFlat(True)
        self.navigateUpButton.setFixedHeight(20)
        self.navigateUpButton.clicked.connect(self.navHost.navigateUp)
        self.verticalLayout.addWidget(self.navigateUpButton)

        self.slidingStackedWidget = SlidingStackedWidget(self)
        self.slidingStackedWidget.animationFinished.connect(
            self.endChangingNavItemListWidget
        )
        self.verticalLayout.addWidget(self.slidingStackedWidget)

        navItemListWidget = NavItemListWidget(self)
        navItemListWidget.activated.connect(self.navItemListWidgetActivatedProxy)
        self.slidingStackedWidget.addWidget(navItemListWidget)

        self.reloadNavWidget()

    @Slot(QModelIndex)
    def navItemListWidgetActivatedProxy(self, index: QModelIndex):
        self.navHost.navigate(index.data(NavItemListWidget.NavItemRole).id)

    def fillNavItemListWidget(
        self, currentNavItem: NavItem, listWidget: NavItemListWidget
    ):
        currentNavItemParent = self.navHost.getNavItemRelatives(
            currentNavItem.id
        ).parent
        currentNavItems = self.navHost.getNavItemRelatives(
            currentNavItemParent.id if currentNavItemParent else ""
        )
        listWidget.setNavItems(currentNavItems.children)
        listWidget.selectNavItem(currentNavItem.id)

    def reloadNavWidget(self):
        self.fillNavItemListWidget(
            self.navHost.currentNavItem, self.slidingStackedWidget.widget(0)
        )
        self.navItemActivated(self.navHost.currentNavItem, self.navHost.currentNavItem)

    @Slot(NavItem, NavItem)
    def navItemActivated(self, oldNavItem: NavItem, newNavItem: NavItem):
        # update navigateUpButton text
        if newNavItemParent := self.navHost.getNavItemRelatives(newNavItem.id).parent:
            self.navigateUpButton.setText(newNavItemParent.text())
        else:
            self.navigateUpButton.setText("Arcaea Offline")

        # update navItemListWidget
        oldNavItemIdSplitted = self.navHost.getNavItemIdSplitted(oldNavItem.id)
        newNavItemIdSplitted = self.navHost.getNavItemIdSplitted(newNavItem.id)

        oldNavItemDepth = len(oldNavItemIdSplitted)
        newNavItemDepth = len(newNavItemIdSplitted)

        if oldNavItemDepth != newNavItemDepth:
            # navItem depth changed, replace current NavItemListWidget
            newNavItemListWidget = NavItemListWidget(self)
            slidingDirection = (
                self.slidingStackedWidget.slidingDirection.RightToLeft
                if newNavItemDepth > oldNavItemDepth
                else self.slidingStackedWidget.slidingDirection.LeftToRight
            )

            self.fillNavItemListWidget(newNavItem, newNavItemListWidget)
            newNavItemListWidget.activated.connect(self.navItemListWidgetActivatedProxy)

            self.startChangingNavItemListWidget(newNavItemListWidget, slidingDirection)

    def startChangingNavItemListWidget(
        self, newNavItemListWidget: NavItemListWidget, slidingDirection
    ):
        newIndex = self.slidingStackedWidget.addWidget(newNavItemListWidget)
        [
            self.slidingStackedWidget.widget(i).setEnabled(False)
            for i in range(self.slidingStackedWidget.count())
        ]
        self.navigateUpButton.setEnabled(False)
        self.navigateUpKeyboardShortcut.setEnabled(False)
        self.slidingStackedWidget.slideInIdx(newIndex, slidingDirection)

    def endChangingNavItemListWidget(self):
        oldWidget = self.slidingStackedWidget.widget(0)
        self.slidingStackedWidget.removeWidget(oldWidget)
        oldWidget.deleteLater()

        newWidget = self.slidingStackedWidget.widget(0)
        newWidget.setEnabled(True)
        self.navigateUpButton.setEnabled(True)
        self.navigateUpKeyboardShortcut.setEnabled(True)
