import pytest
from locators import BUTTON_PERSONAL_ACCOUNT

# Переход в личный кабинет по клику на «Личный кабинет»
@pytest.mark.usefixture("registration_and_login")
def test_personal_account_click_transition(registration_and_login):
    browser = registration_and_login  # Получаем объект браузера из фикстуры

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    assert browser.current_url == "https://stellarburgers.education-services.ru/account/profile", "Переход в личный кабинет не произошёл"

    # Закрытие браузера после теста
    browser.quit()