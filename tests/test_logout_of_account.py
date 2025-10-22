import pytest
from locators import BUTTON_EXIT, BUTTON_PERSONAL_ACCOUNT

# Выход из аккаунта после входа
@pytest.mark.usefixture("registration_and_login")
def test_tap_constructor_button_from_profile(registration_and_login):
    browser = registration_and_login  # Получаем объект браузера из фикстуры

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    assert browser.current_url == "https://stellarburgers.education-services.ru/account/profile", "Переход в личный кабинет не произошёл"

    # Нажатие на кнопку "Выход"
    browser.find_element(*BUTTON_EXIT).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Переход на страницу входа не произошёл"
    
    # Закрытие браузера после теста
    browser.quit()