from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(link)
time.sleep(1)

button_click = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

new_window = browser.window_handles[1]
print(new_window)
browser.switch_to.window(new_window)

x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
y = calc(x_element.text)

input_el = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
input_el.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

alert = browser.switch_to.alert
alert_text = alert.text
number_alert = alert_text.split(': ')[-1]
print(number_alert)

time.sleep(5)
browser.quit()