from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

link = 'https://profile.w3schools.com/login?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fcssref%2Fcss_selectors.php'

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(link)

find_name = 'puk'

assert find_name in browser.current_url, f'Is not {find_name}'

browser.quit()


# s = "My Name is Julia"
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')