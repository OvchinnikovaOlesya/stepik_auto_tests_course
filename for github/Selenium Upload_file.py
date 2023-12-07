from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Овчинников')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Егор')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('ovchinnikov815@mail.xru')

    file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname('methods_selenium'))
    file_path = os.path.join(current_dir, '../methods_selenium/file.txt')
    file.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(6)
    browser.quit()