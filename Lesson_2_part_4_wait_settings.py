# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
# browser.implicitly_wait(5)      # теперь у нас неявное ожидание 5 сек
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# Задание: Про Exceptions

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = 'https://suninjuly.github.io/cats.html'
# browser = webdriver.Chrome()
# browser.get(link)
# browser.find_element(By.ID, "button") -> NoSuchElementException


# Неявное ожидание

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# Явное ожидание
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# Задание: ждем нужный текст на странице

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
book_btn = browser.find_element(By.CSS_SELECTOR, "#book")
book_btn.click()
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
