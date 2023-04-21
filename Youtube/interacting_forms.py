from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(10)

sum1 = driver.find_element(By.ID, 'value1')
sum2 = driver.find_element(By.ID, 'value2')

sum1.send_keys(10)
sum2.send_keys(20)

btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()

sum2 = driver.find_element(By.ID, 'value32')