import pytest
from locators import BUTTON_CONSTRUCTOR, BUTTON_PERSONAL_ACCOUNT, LOGO_STELLAR_BURGERS

# Переход из личного кабинета в Конструктор через кнопку "Конструктор"
@pytest.mark.usefixture("registration_and_login")
def test_tap_constructor_button_from_profile(registration_and_login):
    browser = registration_and_login  # Получаем объект браузера из фикстуры

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    assert browser.current_url == "https://stellarburgers.education-services.ru/account/profile", "Переход в личный кабинет не произошёл"

    # Нажатие на кнопку "Конструктор"
    browser.find_element(*BUTTON_CONSTRUCTOR).click()

    # Проверка перехода в Конструктор
    assert browser.current_url == "https://stellarburgers.education-services.ru", "Переход в Конструктор не произошёл"
    
    # Закрытие браузера после теста
    browser.quit()

# Переход из личного кабинета в Конструктор через лого "Stellar Burgers"
@pytest.mark.usefixture("registration_and_login")
def test_tap_logo_button_from_profile(registration_and_login):
    browser = registration_and_login  # Получаем объект браузера из фикстуры

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    assert browser.current_url == "https://stellarburgers.education-services.ru/account/profile", "Переход в личный кабинет не произошёл"

    # Нажатие на лого "Stellar Burgers"
    browser.find_element(*LOGO_STELLAR_BURGERS).click()

    # Проверка перехода в Конструктор
    assert browser.current_url == "https://stellarburgers.education-services.ru", "Переход в Конструктор не произошёл"
    
    # Закрытие браузера после теста
    browser.quit()