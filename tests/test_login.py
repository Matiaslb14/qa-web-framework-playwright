from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD, INVALID_USER, INVALID_PASSWORD

def test_valid_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open(BASE_URL)
    login.login(VALID_USER, VALID_PASSWORD)

    assert dashboard.is_loaded()

def test_invalid_login_shows_error(page):
    login = LoginPage(page)

    login.open(BASE_URL)
    login.login(INVALID_USER, INVALID_PASSWORD)

    assert "Username and password do not match" in login.get_error_text()
