from ui.navigation.navhost import NavHost
from ui.navigation.navitem import NavItem


class TestNavHost:
    def test_auto_append_parent(self):
        navHost = NavHost()

        navHost.registerNavItem(NavItem(id="aaa.bbb.ccc.ddd"))

        navItems = navHost.navItems

        assert NavItem(id="aaa.bbb.ccc.ddd") in navItems
        assert NavItem(id="aaa.bbb.ccc") in navItems
        assert NavItem(id="aaa.bbb") in navItems
        assert NavItem(id="aaa") in navItems

    def test_auto_select_child(self):
        navHost = NavHost()

        navHost.registerNavItem(NavItem(id="aaa"))
        navHost.registerNavItem(NavItem(id="bbb"))

        assert navHost.currentNavItem.id == "aaa"

        navHost.registerNavItem(NavItem(id="aaa.bbb"))
        navHost.registerNavItem(NavItem(id="aaa.ccc"))

        navHost.navigate("aaa")

        assert navHost.currentNavItem.id == "aaa.bbb"
