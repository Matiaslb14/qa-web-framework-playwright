from pages.base_page import BasePage

class DashboardPage(BasePage):
    INVENTORY = ".inventory_list"
    MENU_BTN = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.INVENTORY)

    def logout(self) -> None:
        self.page.click(self.MENU_BTN)
        self.wait_visible(self.LOGOUT_LINK)
        self.page.click(self.LOGOUT_LINK)
