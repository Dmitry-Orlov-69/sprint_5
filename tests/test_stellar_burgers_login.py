import pytest
from locators import BUTTON_PERSONAL_ACCOUNT, BUTTON_SIGN_IN_FROM_REGISTRATION, INPUT_EMAIL, INPUT_PASSWORD, BUTTON_SIGN_IN

# вход по кнопке «Войти в аккаунт» на главной
@pytest.mark.usefixture("registration_and_login")
def test_login(registration_and_login):
    browser = registration_and_login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    assert browser.current_url.startswith("https://stellarburgers.education-services.ru"), "После входа не вернулись на главную страницу"

    # Закрытие браузера после теста
    browser.quit()

# вход через кнопку «Личный кабинет»
@pytest.mark.usefixture("browser_and_register")
def test_login_via_personal_account(browser_and_register):
    browser = browser_and_register

    # Открытие главной страницы
    browser.get("https://stellarburgers.education-services.ru")

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Переход на страницу входа не произошёл"

    # Заполнение полей email и пароль
    browser.find_element(*INPUT_EMAIL).send_keys(browser.email)
    browser.find_element(*INPUT_PASSWORD).send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка успешного входа
    assert browser.current_url == "https://stellarburgers.education-services.ru", "Вход не был успешным"

    # Закрытие браузера после теста
    browser.quit()

# вход через кнопку в форме регистрации
@pytest.mark.usefixture("browser_and_register")
def test_login_from_registration(browser_and_register):
    browser = browser_and_register

    # Открытие страницы регистрации
    browser.get("https://stellarburgers.education-services.ru/register")

    # Нажатие на кнопку "Войти" в форме регистрации
    browser.find_element(*BUTTON_SIGN_IN_FROM_REGISTRATION).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Переход на страницу входа не произошёл"

    # Заполнение полей email и пароль
    browser.find_element(*INPUT_EMAIL).send_keys(browser.email)
    browser.find_element(*INPUT_PASSWORD).send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка успешного входа
    assert browser.current_url == "https://stellarburgers.education-services.ru", "Вход не был успешным"

    # Закрытие браузера после теста
    browser.quit()

# вход через кнопку в форме восстановления пароля
@pytest.mark.usefixture("browser_and_register")
def login_via_recovery(browser_and_register):
    browser = browser_and_register

    # Открытие формы восстановления пароля
    browser.get("https://stellarburgers.education-services.ru/forgot-password")

    # Нажатие на кнопку "Войти" в форме восстановления пароля
    browser.find_element(*BUTTON_SIGN_IN_FROM_REGISTRATION).click()

    # Проверка перехода на страницу входа
    assert browser.current_url == "https://stellarburgers.education-services.ru/login", "Переход на страницу входа не произошёл"

    # Заполнение полей email и пароль
    browser.find_element(*INPUT_EMAIL).send_keys(browser.email)
    browser.find_element(*INPUT_PASSWORD).send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка успешного входа
    assert browser.current_url == "https://stellarburgers.education-services.ru", "Вход не был успешным"

    # Закрытие браузера после теста
    browser.quit()

