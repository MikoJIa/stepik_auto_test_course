from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# browser.execute_script("alert(Robots at work);")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('robots at work');")
# time.sleep(10)
# browser.quit()

link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.XPATH, "//label/span[@id='input_value']").text
y = calc(x_element)

# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element(By.XPATH, "//input[@id='answer']")
input.send_keys(y)

check_box = browser.find_element(By.XPATH, "//div/input[@id='robotCheckbox']")
check_box.click()

radio_button = browser.find_element(By.XPATH, "//div/input[@id='robotsRule']")
radio_button.click()

button = browser.find_element(By.TAG_NAME, 'button')

button.click()
time.sleep(5)
browser.quit()