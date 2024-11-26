import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys(''.join(random.choice(string.ascii_letters) for _ in range(10)))

    button_browser = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_browser.click()

finally:
    time.sleep(30)
    browser.quit()
