from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.ID, "input_value")
y = calc(x_element.text)

input_res = browser.find_element(By.ID, "answer")
input_res.send_keys(y)

wait = WebDriverWait(browser, 5)
button_finish = wait.until(EC.element_to_be_clickable((By.ID, "solve")))
button_finish.click()

alert = browser.switch_to.alert
alert_text = alert.text
number = alert_text.split(': ')[-1]
print(number)
alert.accept()

browser.quit()
