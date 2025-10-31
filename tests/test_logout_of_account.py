import pytest
from locators import BUTTON_EXIT, BUTTON_PERSONAL_ACCOUNT
from urls import MAIN_PAGE_URL, PERSONAL_ACCOUNT_URL, LOGIN_URL

# Выход из аккаунта после входа
@pytest.mark.usefixture("registration", "login")
def test_logout_of_account(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    if not browser.current_url.startswith(MAIN_PAGE_URL):
        print("После входа не вернулись на главную страницу")

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    if browser.current_url != PERSONAL_ACCOUNT_URL:
        print("Переход в личный кабинет не произошёл")

    # Нажатие на кнопку "Выход"
    browser.find_element(*BUTTON_EXIT).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == LOGIN_URL, "Переход на страницу входа не произошёл"