from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div/label[contains(text(), 'First name*')]/following-sibling::input")
    input1.send_keys("Nikolay")

    time.sleep(1)

    input2 = browser.find_element(By.XPATH, "//div/label[contains(text(), 'Last name*')]/following-sibling::input")
    input2.send_keys("Popov")

    time.sleep(1)

    input3 = browser.find_element(By.XPATH, "//div/label[contains(text(), 'Email*')]/following-sibling::input")
    input3.send_keys("Kolya_popov_86@tut.by")

    time.sleep(1)

    submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit.click()

    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:

    time.sleep(10)
    browser.quit()

