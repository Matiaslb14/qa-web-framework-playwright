from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> None:
        self.page.goto(url)

    def wait_visible(self, selector: str) -> None:
        self.page.wait_for_selector(selector, state="visible")
