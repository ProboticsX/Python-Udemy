from tests.acceptance.locators.base_page import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def url(self):
        return 'http://127.0.0.1:5000'

    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)  # passes the tuple as two arguments

    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)