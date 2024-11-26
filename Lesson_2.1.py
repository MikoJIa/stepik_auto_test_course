from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)


time.sleep(2)
button = browser.find_element(By.XPATH, "//button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.XPATH, "//label/span[@id='input_value']").text
y = calc(x_element)

input_1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input_1.send_keys(y)

submit = browser.find_element(By.XPATH, "//button")
submit.click()

alert = browser.switch_to.alert
time.sleep(3)
alert_text = alert.text
number_to_alert = alert_text.split(": ")[-1]
print(number_to_alert)
alert.accept()

time.sleep(5)
browser.quit()

# browser_2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# link_2 = "https://stepik.org/lesson/184253/step/4?unit=158843"
# browser_2.get(link_2)

# current_url = str(browser.current_url)
# print(current_url)
# if 'promo' in current_url:
#     browser.get(current_url + '?auth=login')
#     time.sleep(3)


# button_entrance_to_stepik = browser_2.find_element(By.CSS_SELECTOR, "a#ember483")
# button_entrance_to_stepik.click()



#     input_login = browser_2.find_element(By.XPATH, "//div/input[@id='id_login_email']")
#     input_login.send_keys('Kolya_popov_86@tut.by')
#
#     time.sleep(1)
#
#     input_password = browser_2.find_element(By.XPATH, "//div/input[@id='id_login_password']")
#     input_password.send_keys("80292788064np")
#
#     time.sleep(1)
#
#     button_login = browser_2.find_element(By.XPATH, "//button[@class='sign-form__btn button_with-loader ']")
#     button_login.click()
#
#     time.sleep(2)
#
# browser_2.get(link_2)
#
# input_stepik = browser.find_element(By.XPATH, "//div/textarea")
# input_stepik.send_keys(number_to_alert)
#
# time.sleep(1)
#
# submit_stepik = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
# submit_stepik.click()
#
# time.sleep(5)
# browser.quit()

