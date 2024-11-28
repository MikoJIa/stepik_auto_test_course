import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestUniqueSelectors(unittest.TestCase):

    link_1 = 'http://suninjuly.github.io/registration1.html'
    link_2 = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    text_task = "Congratulations! You have successfully registered!"

    def fill_form(self, link):
        self.browser.get(link)

        input1 = self.browser.find_element(By.XPATH,
                                           "//div/label[contains(text(), 'First name*')]/following-sibling::input")
        input1.send_keys("Nikolay")

        time.sleep(1)

        input2 = self.browser.find_element(By.XPATH,
                                           "//div/label[contains(text(), 'Last name*')]/following-sibling::input")
        input2.send_keys("Popov")

        time.sleep(1)

        input3 = self.browser.find_element(By.XPATH, "//div/label[contains(text(), 'Email*')]/following-sibling::input")
        input3.send_keys("Kolya_popov_86@tut.by")

        time.sleep(1)

        submit = self.browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit.click()

        text_finished = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        text_at_page = text_finished.text

        return text_at_page

    def test_register_1(self):
        register = self.fill_form(self.link_1)
        self.assertEqual(self.text_task, register), f'Should be {self.text_task}'

    def test_register_2(self):
        register_2 = self.fill_form(self.link_2)
        self.assertEqual(self.text_task, register_2), f'Should be {self.text_task}'

        time.sleep(5)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
