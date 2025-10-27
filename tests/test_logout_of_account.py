import pytest
from locators import BUTTON_EXIT, BUTTON_PERSONAL_ACCOUNT
from urls import PERSONAL_ACCOUNT_URL, LOGIN_URL

# Выход из аккаунта после входа
@pytest.mark.usefixture("registration", "login")
def test_logout_of_account(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    assert browser.current_url == PERSONAL_ACCOUNT_URL, "Переход в личный кабинет не произошёл"

    # Нажатие на кнопку "Выход"
    browser.find_element(*BUTTON_EXIT).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == LOGIN_URL, "Переход на страницу входа не произошёл"