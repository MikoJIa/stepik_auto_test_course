from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input_1 = browser.find_element(By.NAME, 'first_name')
    input_1.send_keys('Nikolay')

    input_2 = browser.find_element(By.NAME, 'last_name')
    input_2.send_keys('Popov')

    input_3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input_3.send_keys('Minsk')

    input_4 = browser.find_element(By.ID, 'country')
    input_4.send_keys('Belarus')

    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
