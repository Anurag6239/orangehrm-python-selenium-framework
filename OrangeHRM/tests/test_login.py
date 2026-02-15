from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    login_page.login("Admin", "admin123")

    assert home_page.is_dashboard_visible(), "Dashboard not visible"
