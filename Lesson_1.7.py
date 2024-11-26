import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    number1 = browser.find_element(By.XPATH, "//h2/span[@id='num1']").text
    number2 = browser.find_element(By.XPATH, "//h2/span[@id='num2']").text
    result = int(number1) + int(number2)
    result1 = str(result)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))

    # browser.find_element(By.XPATH, "//select[@id='dropdown']").click()

    time.sleep(1)

    find_elements = browser.find_elements(By.XPATH, '//option')
    for x in find_elements:
        if x.text == result1:
            y = x.text
            select.select_by_value(y)
            time.sleep(2)
            submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
            submit.click()

finally:
    time.sleep(5)
    browser.quit()
