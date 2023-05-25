from selenium import webdriver
from pyvirtualdisplay import Display
import time
import unittest



class Test_registration(unittest.TestCase):
    def test_registration1(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block > .first_class > input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block > .second_class > input')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block > .third_class > input')
        input3.send_keys("q@q.ru")


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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        assert "Congratulations! You have successfully registered!" == welcome_text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_registration2(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block > .first_class > input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block > .second_class > input')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block > .third_class > input')
        input3.send_keys("q@q.ru")


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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        assert "Congratulations! You have successfully registered!" == welcome_text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
if __name__ == "__main__":
    unittest.main()