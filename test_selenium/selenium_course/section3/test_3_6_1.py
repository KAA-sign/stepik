import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link_list = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number_link', link_list)
def test_link_list(browser, number_link):
    feedback_text = ''
    link = f"https://stepik.org/lesson/{number_link}/step/1"
    browser.implicitly_wait(5)
    browser.get(link)

    # говорим WebDriver искать каждый элемент в течение 10 секунд
    

    # Расчет значения
    answer = math.log(int(time.time() + 28.1))

    # Вводим значение в поле
    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(str(answer))

    # Отправляем ответ
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()

    time.sleep(5)

    # находим элемент, содержащий текст
    feedback = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    # записываем в переменную feedback_text текст из элемента feedback

    if feedback != 'Correct!':
        feedback_text += str(feedback)
        print(feedback)

    # assert feedback == False


    print(feedback_text)

