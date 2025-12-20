from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD

def test_logout_returns_to_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open(BASE_URL)
    login.login(VALID_USER, VALID_PASSWORD)
    assert dashboard.is_loaded()

    dashboard.logout()
    assert page.is_visible("#login-button")
