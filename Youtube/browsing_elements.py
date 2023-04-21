from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(3)
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(progress_element.text)

WebDriverWait(driver, 30).until(
    expected_conditions.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), #Element filtration
        'Complete!' #The expected text
    )
)
