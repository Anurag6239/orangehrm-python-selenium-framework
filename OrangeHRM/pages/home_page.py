from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_visible(self):
        return self.driver.find_element(*self.DASHBOARD_HEADER).is_displayed()