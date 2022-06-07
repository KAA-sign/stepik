from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.set_window_size(1055, 1000)
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element_value((By.ID, "price", "$100"))
        )
    button.click()
    
    message = browser.find_element(By.ID, "verify_message")

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # Выбираем вторую вкладку
    new_window = browser.window_handles[1]

    # Переключамся на новую вкладку
    browser.switch_to.window(new_window)

    # Получение значения и расчет
    value = int(browser.find_element_by_id("input_value").text)
    func = math.log(abs(12 * math.sin(value)))

    # Вводим значение в поле
    input = browser.find_element_by_id("answer")
    input.send_keys(str(func))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # # ждем загрузки страницы
    # time.sleep(5)


finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




    

    assert "successful" in message.text