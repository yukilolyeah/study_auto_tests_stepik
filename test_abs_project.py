# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        first_name_input.send_keys("John")
        last_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        last_name_input.send_keys("Doe")
        email_input = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        email_input.send_keys("test@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text is not correct")
        browser.quit()

    # этот тест должен упасть с ошибкой
    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        first_name_input.send_keys("John")
        last_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        last_name_input.send_keys("Doe")
        email_input = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        email_input.send_keys("test@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text is not correct")
        browser.quit()

if __name__ == "__main__":
    unittest.main()


