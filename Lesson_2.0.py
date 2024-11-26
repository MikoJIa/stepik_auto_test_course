import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(link)


with open("file.txt", 'w+') as file:

    input_1 = browser.find_element(By.XPATH, "//div/label[text()='First name* ']/following-sibling::input[1]")
    input_1.send_keys("Nikolay")
    file.write(f"First name: {input_1.get_attribute("value")}\n")

    input_2 = browser.find_element(By.XPATH, "//div/label[text()='First name* ']/following-sibling::input[2]")
    input_2.send_keys("Popov")
    file.write(f"Last name: {input_2.get_attribute("value")}\n")

    input_3 = browser.find_element(By.XPATH, "//div/label[text()='First name* ']/following-sibling::input[3]")
    input_3.send_keys("Kolya_popov_86@tut.by")
    file.write(f"Email: {input_3.get_attribute("value")}\n")


current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'file.txt'
file_path = os.path.join(current_dir, file_name)


element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)


submit = browser.find_element(By.XPATH, "//button[@type='submit']")
submit.click()

time.sleep(2)

alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()

time.sleep(5)
browser.quit()
