import random
import string
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, BUTTON_LOGIN_ACCOUNT, INPUT_EMAIL, INPUT_PASSWORD, BUTTON_SIGN_IN
from urls import REGISTER_URL, LOGIN_URL, MAIN_PAGE_URL

@pytest.fixture
def browser_start_end():
    # Инициализация драйвера Chrome с помощью WebDriverManager
    browser = webdriver.Chrome(service=ChromeDriverManager().install())
    yield browser
    # Закрытие браузера после теста
    browser.quit()

@pytest.fixture
def registration(browser_start_end):
    browser = browser_start_end

    # Открытие страницы регистрации
    browser.get(REGISTER_URL)

    # Генерация и ввод данных
    name = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    email = f"{name}_{random.randint(1, 100)}@yandex.ru"  # Примерный номер когорты
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    browser.find_element(*NAME_INPUT).send_keys(name)
    browser.find_element(*EMAIL_INPUT).send_keys(email)
    browser.find_element(*PASSWORD_INPUT).send_keys(password)

    # Нажатие кнопки регистрации
    browser.find_element(*REGISTER_BUTTON).click()

    # Проверка URL после регистрации
    assert browser.current_url == LOGIN_URL, "Регистрация не прошла успешно, перенаправление на страницу входа не произошло"

    browser.email = email
    browser.password = password

    yield browser  # Возврат браузера для использования в тесте

@pytest.fixture
def login(registration):
    browser = registration

    # Вход на главную страницу
    browser.get(MAIN_PAGE_URL)

    # Нажатие на кнопку "Войти в аккаунт"
    browser.find_element(*BUTTON_LOGIN_ACCOUNT).click()

    # Заполнение полей "Email" и "Пароль"
    email_field = browser.find_element(*INPUT_EMAIL)
    password_field = browser.find_element(*INPUT_PASSWORD)

    email_field.send_keys(browser.email)
    password_field.send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка, что мы оказались на главной странице
    assert browser.current_url.startswith(MAIN_PAGE_URL), "После входа не вернулись на главную страницу"

    yield browser  # Возврат браузера для использования в тесте