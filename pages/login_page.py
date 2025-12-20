from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR = '[data-test="error"]'

    def open(self, base_url: str) -> None:
        self.goto(base_url)

    def login(self, username: str, password: str) -> None:
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def get_error_text(self) -> str:
        self.wait_visible(self.ERROR)
        return self.page.inner_text(self.ERROR)
