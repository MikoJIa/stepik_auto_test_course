import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import (By)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element(By.XPATH, "//h2/img[@id='treasure']")
    y = calc(x.get_attribute("valuex"))

    input1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input1.send_keys(y)

    time.sleep(0.5)

    check_box = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    check_box.click()

    time.sleep(0.5)

    radio_button = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    radio_button.click()

    time.sleep(0.5)

    submit = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()