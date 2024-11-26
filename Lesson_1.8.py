import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://suninjuly.github.io/selects2.html"
browser.get(link)

number_1 = browser.find_element(By.XPATH, "//h2/span[@id='num1']").text
number_2 = browser.find_element(By.XPATH, "//h2/span[@id='num2']").text
result = int(number_1) + int(number_2)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(result))

submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
submit.click()

time.sleep(5)
browser.quit()
