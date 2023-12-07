from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/registration1.html')
    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control.first[required]')
    input1.send_keys('Olesya')
    input2 = browser.find_element(By.CSS_SELECTOR, '.form-control.second[required]')
    input2.send_keys('Ovchinnikova')
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.third[required]')
    input3.send_keys('Good')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(3)

    elem = browser.find_element(By.TAG_NAME, 'h1')
    text_prov = elem.text
    assert "Congratulations! You have successfully registered!" == text_prov

finally:
    time.sleep(30)
    browser.quit()


