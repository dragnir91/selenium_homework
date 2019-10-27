from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try: 
            browser = webdriver.Chrome()
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)
            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first[required]")
            input1.send_keys("Vladimir")
            input2 = browser.find_element_by_css_selector(".second[required]")
            input2.send_keys("Lenin")
            input3 = browser.find_element_by_css_selector(".third[required]")
            input3.send_keys("USSR_1917@yandex.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be - Congratulations! You have successfully registered!")

    def test_abs2(self):
        try: 
            browser = webdriver.Chrome()
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)
            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first[required]")
            input1.send_keys("Vladimir")
            input2 = browser.find_element_by_css_selector(".second[required]")
            input2.send_keys("Lenin")
            input3 = browser.find_element_by_css_selector(".third[required]")
            input3.send_keys("USSR_1917@yandex.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be - Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
