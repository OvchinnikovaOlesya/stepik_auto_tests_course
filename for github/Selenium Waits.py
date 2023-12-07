# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100
# Нажать на кнопку "Book"
# Решить математическую задачу и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/explicit_wait2.html')
    price_100 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, 'book').click()

    input_val = browser.find_element(By.ID, 'input_value')
    num_text = input_val.text
    result = calc(num_text)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(result)
    browser.find_element(By.ID, 'solve').click()

finally:
    browser.quit()
