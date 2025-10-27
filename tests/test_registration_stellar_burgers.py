import random
import string
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, ERROR_MESSAGE
from urls import REGISTER_URL, LOGIN_URL

def test_successful_registration(browser_start_end):
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

def test_incorrect_password_error(browser_start_end):
    browser = browser_start_end

    # Открытие страницы регистрации
    browser.get(REGISTER_URL)

    # Генерация и ввод данных
    name = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    email = f"{name}_{random.randint(1, 100)}@yandex.ru"  # Примерный номер когорты

    # Ввод некорректного пароля (менее 6 символов)
    password = "123"

    browser.find_element(*NAME_INPUT).send_keys(name)
    browser.find_element(*EMAIL_INPUT).send_keys(email)
    browser.find_element(*PASSWORD_INPUT).send_keys(password)

    # Нажатие на кнопку регистрации
    browser.find_element(*REGISTER_BUTTON).click()

    # Проверка появления сообщения об ошибке
    error_message = browser.find_element(*ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_message, "Сообщение об ошибке для некорректного пароля не найдено"