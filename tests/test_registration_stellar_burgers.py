import random
import string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, ERROR_MESSAGE

def test_successful_registration(browser_and_register):
    browser = browser_and_register

    # Проверка URL после регистрации
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Регистрация не прошла успешно, перенаправление на страницу входа не произошло"

    # Закрытие браузера после теста
    browser.quit()

def test_incorrect_password_error():
    # Инициализация драйвера Chrome с помощью WebDriverManager
    browser = webdriver.Chrome(service=ChromeDriverManager().install())

    # Открытие страницы регистрации
    browser.get("https://stellarburgers.education-services.ru/register")

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

    # Закрытие браузера после теста
    browser.quit()