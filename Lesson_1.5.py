from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    variable_x = browser.find_element(By.XPATH, "//div/label/span[@id='input_value']")
    print(variable_x.text)
    y = calc(variable_x.text)
    print(y)
    input_text = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input_text.send_keys(y)

    check_box = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    check_box.click()

    radio_button = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    radio_button.click()

    submit = browser.find_element(By.CSS_SELECTOR, "div button")
    submit.click()

    # x_element = browser.find_element(By.CSS_SELECTOR, "div label > span[id='input_value']")
    # x = x_element.text
    # print(x)

finally:
    time.sleep(5)
    browser.quit()