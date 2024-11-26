import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


link = "http://127.0.0.1:8000"
try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    text_django = browser.find_element(By.CSS_SELECTOR, "a.logo")
    print(text_django.text)

    assert "Django" in text_django.text

finally:
    time.sleep(5)
    browser.quit()

