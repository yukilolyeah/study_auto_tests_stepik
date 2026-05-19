# Задание: переход на новую вкладку
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    new_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    new_submit.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
