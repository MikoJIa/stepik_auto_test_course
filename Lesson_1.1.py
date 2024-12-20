import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(5)

    res = str(math.ceil(math.pow(math.pi, math.e)*10000))
    search_link_text = browser.find_element(By.LINK_TEXT, res)

    time.sleep(5)

    search_link_text.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys('Petrov')

    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys('Smolensk')

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys('Russia')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(15)
    browse.quit()