from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(a, b):
    return int(a)+int(b)


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')
    num1 = browser.find_element(By.ID, 'num1')
    a = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    b = num2.text
    print('Элементы\n', a, b)

    summ = calc(a, b)
    print(type(summ))

    drop = Select(browser.find_element(By.TAG_NAME, 'select'))
    drop.select_by_value(str(summ))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(5)
    browser.quit()
