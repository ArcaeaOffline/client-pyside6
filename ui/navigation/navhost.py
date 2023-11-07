import logging
from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import QObject, Signal

from .navitem import NavItem

logger = logging.getLogger(__name__)


@dataclass
class NavItemRelatives:
    parent: Optional[NavItem]
    children: list[NavItem]


class NavHost(QObject):
    activated = Signal(NavItem, NavItem)

    navItemsChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__navItems: list[NavItem] = []
        self.__currentNavItem: NavItem = None

    @property
    def navItems(self) -> list[NavItem]:
        return self.__navItems

    @property
    def currentNavItem(self) -> NavItem:
        if self.__currentNavItem:
            return self.__currentNavItem

        if self.__navItems:
            self.__currentNavItem = self.__navItems[0]
            return self.__currentNavItem

    def findNavItem(self, navItemId: str) -> Optional[NavItem]:
        navItemIds = [item.id for item in self.__navItems]
        try:
            index = navItemIds.index(navItemId)
            return self.__navItems[index]
        except IndexError:
            return None

    def isNavigatingBack(self, oldNavItemId: str, newNavItemId: str) -> bool:
        # sourcery skip: class-extract-method
        # |     oldNavItemId      |    newNavItemId    | back? |
        # |-----------------------|--------------------|-------|
        # | database.manage.packs |      database      | True  |
        # |      ocr.device       |        ocr         | True  |
        # | database.manage.songs |      ocr.b30       | False |
        # |       database        |      database      | False |

        oldNavItemIdSplitted = self.getNavItemIdSplitted(oldNavItemId)
        newNavItemIdSplitted = self.getNavItemIdSplitted(newNavItemId)

        return self.getNavItemDepth(newNavItemId) < self.getNavItemDepth(
            oldNavItemId
        ) and all((idFrag in oldNavItemIdSplitted) for idFrag in newNavItemIdSplitted)

    def isChild(self, childNavItemId: str, parentNavItemId: str) -> bool:
        childNavItemIdSplitted = self.getNavItemIdSplitted(childNavItemId)
        parentNavItemIdSplitted = self.getNavItemIdSplitted(parentNavItemId)

        return all(
            (idFrag in childNavItemIdSplitted) for idFrag in parentNavItemIdSplitted
        )

    def getNavItemIdSplitted(self, navItemId: str) -> list[str]:
        return navItemId.split(".")

    def getNavItemDepth(self, navItemId: str) -> int:
        return len(self.getNavItemIdSplitted(navItemId))

    def getNavItemRelatives(self, navItemId: str) -> NavItemRelatives:
        parent = None
        if "." in navItemId:
            navItemIdSplitted = navItemId.split(".")
            parentId = navItemIdSplitted[:-1]
            parent = self.findNavItem(".".join(parentId))

        if not navItemId:
            # return root navItems
            children = [navItem for navItem in self.__navItems if "." not in navItem.id]
        else:
            children = [
                navItem
                for navItem in self.__navItems
                if navItem.id.startswith(navItemId)
                and navItem.id != navItemId
                and self.getNavItemDepth(navItem.id)
                == self.getNavItemDepth(navItemId) + 1
            ]

        return NavItemRelatives(parent=parent, children=children)

    def registerNavItem(self, item: NavItem):
        self.__navItems.append(item)
        self.navItemsChanged.emit()

    def navigate(self, navItemId: str):
        oldNavItem = self.__currentNavItem or NavItem("")
        newNavItem = self.findNavItem(navItemId)

        if newNavItem is None:
            raise IndexError(
                f"Cannot find '{navItemId}' in {repr(self)}. "
                "Maybe try registering it?"
            )

        # if the navItem have children, navigate to first child
        # but if the navItem is going back, e.g. 'database.manage' -> 'database'
        # then don't navigate to it's child.
        if self.isNavigatingBack(oldNavItem.id, newNavItem.id):
            # navItem is going back
            currentNavItem = newNavItem
        else:
            newNavItemRelatives = self.getNavItemRelatives(newNavItem.id)
            if newNavItemRelatives.children:
                currentNavItem = newNavItemRelatives.children[0]
            else:
                currentNavItem = newNavItem

        self.__currentNavItem = currentNavItem
        self.activated.emit(oldNavItem, self.currentNavItem)

    def navigateUp(self):
        navItemRelatives = self.getNavItemRelatives(self.currentNavItem.id)
        if navItemRelatives.parent:
            self.navigate(navItemRelatives.parent.id)


navHost = NavHost()
