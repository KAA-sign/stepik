import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number_link', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, number_link):
    link = f"https://stepik.org/lesson/{number_link}/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")