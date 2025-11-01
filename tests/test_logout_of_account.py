from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import BUTTON_EXIT, BUTTON_PERSONAL_ACCOUNT
from urls import MAIN_PAGE_URL, PERSONAL_ACCOUNT_URL, LOGIN_URL

# Выход из аккаунта после входа
@pytest.mark.usefixture("registration", "login")
def test_logout_of_account(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    WebDriverWait(browser, 10).until(EC.url_to_be(PERSONAL_ACCOUNT_URL))

    # Нажатие на кнопку "Выход"
    browser.find_element(*BUTTON_EXIT).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == LOGIN_URL, "Переход на страницу входа не произошёл"