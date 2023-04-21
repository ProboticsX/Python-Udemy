from selenium import webdriver
import bot.booking.constants as const
from selenium.webdriver.common.by import By

class Booking():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def change_currency(self):
        currency_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Prices in U.S. Dollar"]')
        currency_element.click()
        #cant do further but got the idea

    def select_place_to_go(self, place_to_go):
        search_field = self.driver.find_element(By.ID, ':Ra9:')
        search_field.clear()
        search_field.send_keys(place_to_go)