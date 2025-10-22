import pytest
from locators import BUTTON_ROLLS, BUTTON_SAUCES, BUTTON_TOPPINGS

# Проверка перехода к разделам Конструктора
@pytest.mark.usefixture("registration_and_login")
def test_buttons_constructor_section(registration_and_login):
    browser = registration_and_login  # Получаем объект браузера из фикстуры

    # Нажатие на кнопку "Соусы"
    browser.find_element(*BUTTON_SAUCES).click()

    # Нажатие на кнопку "Начинки"
    browser.find_element(*BUTTON_TOPPINGS).click()

    # Нажатие на кнопку "Булки"
    browser.find_element(*BUTTON_ROLLS).click()

    # Закрытие браузера после теста
    browser.quit()