import random
import string
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, BUTTON_LOGIN_ACCOUNT, INPUT_EMAIL, INPUT_PASSWORD, BUTTON_SIGN_IN

@pytest.fixture
def browser_and_register():
    # Инициализация драйвера Chrome с помощью WebDriverManager
    browser = webdriver.Chrome(service=ChromeDriverManager().install())

    # Открытие страницы регистрации
    browser.get("https://stellarburgers.education-services.ru/register")

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
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Регистрация не прошла успешно, перенаправление на страницу входа не произошло"

    browser.email = email
    browser.password = password

    yield browser  # Возврат браузера для использования в тесте

@pytest.fixture
def registration_and_login():
    # Инициализация драйвера Chrome с помощью WebDriverManager
    browser = webdriver.Chrome(service=ChromeDriverManager().install())

    # Открытие страницы регистрации
    browser.get("https://stellarburgers.education-services.ru/register")

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
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Регистрация не прошла успешно, перенаправление на страницу входа не произошло"

    # Вход на главную страницу
    browser.get("https://stellarburgers.education-services.ru")

    # Нажатие на кнопку "Войти в аккаунт"
    browser.find_element(*BUTTON_LOGIN_ACCOUNT).click()

    # Заполнение полей "Email" и "Пароль"
    email_field = browser.find_element(*INPUT_EMAIL)
    password_field = browser.find_element(*INPUT_PASSWORD)

    email_field.send_keys(email)
    password_field.send_keys(password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка, что мы оказались на главной странице
    assert browser.current_url.startswith("https://stellarburgers.education-services.ru"), "После входа не вернулись на главную страницу"

    yield browser  # Возврат браузера для использования в тесте