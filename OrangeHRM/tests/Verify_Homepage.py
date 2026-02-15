from pages.home_page import HomePage

def test_smoke_home_page(browser):
    home_page = HomePage(browser)
    home_page.load()