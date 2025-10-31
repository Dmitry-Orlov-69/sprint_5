import pytest
from locators import BUTTON_CONSTRUCTOR, BUTTON_PERSONAL_ACCOUNT, LOGO_STELLAR_BURGERS
from urls import PERSONAL_ACCOUNT_URL, MAIN_PAGE_URL

# Переход из личного кабинета в Конструктор через кнопку "Конструктор"
@pytest.mark.usefixture("registration", "login")
def test_tap_constructor_button_from_profile(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    if not browser.current_url.startswith(MAIN_PAGE_URL):
        print("После входа не вернулись на главную страницу")

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    if browser.current_url != PERSONAL_ACCOUNT_URL:
        print("Переход в личный кабинет не произошёл")

    # Нажатие на кнопку "Конструктор"
    browser.find_element(*BUTTON_CONSTRUCTOR).click()

    # Проверка перехода в Конструктор
    assert browser.current_url == MAIN_PAGE_URL, "Переход в Конструктор не произошёл"

# Переход из личного кабинета в Конструктор через лого "Stellar Burgers"
@pytest.mark.usefixture("registration", "login")
def test_tap_logo_button_from_profile(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    if not browser.current_url.startswith(MAIN_PAGE_URL):
        print("После входа не вернулись на главную страницу")

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    if browser.current_url != PERSONAL_ACCOUNT_URL:
        print("Переход в личный кабинет не произошёл")

    # Нажатие на лого "Stellar Burgers"
    browser.find_element(*LOGO_STELLAR_BURGERS).click()

    # Проверка перехода в Конструктор
    assert browser.current_url == MAIN_PAGE_URL, "Переход в Конструктор не произошёл"