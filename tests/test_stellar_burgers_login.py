import pytest
from locators import BUTTON_LOGIN_ACCOUNT, BUTTON_PERSONAL_ACCOUNT, BUTTON_SIGN_IN_FROM_REGISTRATION, INPUT_EMAIL, INPUT_PASSWORD, BUTTON_SIGN_IN
from urls import MAIN_PAGE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL

# Вход по кнопке «Войти в аккаунт» на главной
@pytest.mark.usefixture("registration")
def test_login(registration):
    browser = registration  # Получаем объект браузера из фикстуры

    # Проверка URL после регистрации
    if browser.current_url != LOGIN_URL:
        print("Регистрация не прошла успешно, перенаправление на страницу входа не произошло")

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

# Вход через кнопку «Личный кабинет»
@pytest.mark.usefixture("registration")
def test_login_via_personal_account(registration):
    browser = registration

    # Проверка URL после регистрации
    if browser.current_url != LOGIN_URL:
        print("Регистрация не прошла успешно, перенаправление на страницу входа не произошло")

    # Открытие главной страницы
    browser.get(MAIN_PAGE_URL)

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода на страницу входа
    if browser.current_url != LOGIN_URL:
        print("Переход на страницу входа не произошёл")

    # Заполнение полей email и пароль
    browser.find_element(*INPUT_EMAIL).send_keys(browser.email)
    browser.find_element(*INPUT_PASSWORD).send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка успешного входа
    assert browser.current_url == MAIN_PAGE_URL, "Вход не был успешным"

# Вход через кнопку в форме регистрации
@pytest.mark.usefixture("registration")
def test_login_from_registration(registration):
    browser = registration

    # Проверка URL после регистрации
    if browser.current_url != LOGIN_URL:
        print("Регистрация не прошла успешно, перенаправление на страницу входа не произошло")

    # Открытие страницы регистрации
    browser.get(REGISTER_URL)

    # Нажатие на кнопку "Войти" в форме регистрации
    browser.find_element(*BUTTON_SIGN_IN_FROM_REGISTRATION).click()

    # Проверка перехода на страницу входа
    if browser.current_url != LOGIN_URL:
        print("Переход на страницу входа не произошёл")

    # Заполнение полей email и пароль
    browser.find_element(*INPUT_EMAIL).send_keys(browser.email)
    browser.find_element(*INPUT_PASSWORD).send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка успешного входа
    assert browser.current_url == MAIN_PAGE_URL, "Вход не был успешным"

# Вход через кнопку в форме восстановления пароля
@pytest.mark.usefixture("registration")
def login_via_recovery(registration):
    browser = registration

    # Проверка URL после регистрации
    if browser.current_url != LOGIN_URL:
        print("Регистрация не прошла успешно, перенаправление на страницу входа не произошло")

    # Открытие формы восстановления пароля
    browser.get(FORGOT_PASSWORD_URL)

    # Нажатие на кнопку "Войти" в форме восстановления пароля
    browser.find_element(*BUTTON_SIGN_IN_FROM_REGISTRATION).click()

    # Проверка перехода на страницу входа
    if browser.current_url != LOGIN_URL:
        print("Переход на страницу входа не произошёл")

    # Заполнение полей email и пароль
    browser.find_element(*INPUT_EMAIL).send_keys(browser.email)
    browser.find_element(*INPUT_PASSWORD).send_keys(browser.password)

    # Нажатие кнопки "Войти"
    browser.find_element(*BUTTON_SIGN_IN).click()

    # Проверка успешного входа
    assert browser.current_url == MAIN_PAGE_URL, "Вход не был успешным"