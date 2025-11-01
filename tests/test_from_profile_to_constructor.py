from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import BUTTON_CONSTRUCTOR, BUTTON_PERSONAL_ACCOUNT, LOGO_STELLAR_BURGERS
from urls import PERSONAL_ACCOUNT_URL, MAIN_PAGE_URL

# Переход из личного кабинета в Конструктор через кнопку "Конструктор"
@pytest.mark.usefixture("registration", "login")
def test_tap_constructor_button_from_profile(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    WebDriverWait(browser, 10).until(EC.url_to_be(PERSONAL_ACCOUNT_URL))

    # Нажатие на кнопку "Конструктор"
    browser.find_element(*BUTTON_CONSTRUCTOR).click()

    # Проверка перехода в Конструктор
    assert browser.current_url == MAIN_PAGE_URL, "Переход в Конструктор не произошёл"

# Переход из личного кабинета в Конструктор через лого "Stellar Burgers"
@pytest.mark.usefixture("registration", "login")
def test_tap_logo_button_from_profile(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    WebDriverWait(browser, 10).until(EC.url_to_be(PERSONAL_ACCOUNT_URL))

    # Нажатие на лого "Stellar Burgers"
    browser.find_element(*LOGO_STELLAR_BURGERS).click()

    # Проверка перехода в Конструктор
    assert browser.current_url == MAIN_PAGE_URL, "Переход в Конструктор не произошёл"