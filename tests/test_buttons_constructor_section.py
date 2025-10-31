import pytest
from locators import BUTTON_ROLLS, BUTTON_SAUCES, BUTTON_TOPPINGS, INGREDIENT_SAUCE_SPICY_X, INGREDIENT_MEAT_PROTOSTOMIA, INGREDIENT_BUN_R2_D3
from urls import MAIN_PAGE_URL

# Проверка перехода к разделу "Соусы" и наличия ингредиента "Соус Spicy-X"
@pytest.mark.usefixture("registration", "login")
def test_button_sauces(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    if not browser.current_url.startswith(MAIN_PAGE_URL):
        print("После входа не вернулись на главную страницу")

    # Нажатие на кнопку "Соусы"
    browser.find_element(*BUTTON_SAUCES).click()

    # Проверка наличия ингредиента "Соус Spicy-X" на экране
    assert browser.find_element(*INGREDIENT_SAUCE_SPICY_X).is_displayed(), "Ингредиент 'Соус Spicy-X' не найден"

# Проверка перехода к разделу "Начинки" и наличия ингредиента "Мясо бессмертных моллюсков Protostomia"
@pytest.mark.usefixture("registration", "login")
def test_button_toppings(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    if not browser.current_url.startswith(MAIN_PAGE_URL):
        print("После входа не вернулись на главную страницу")

    # Нажатие на кнопку "Начинки"
    browser.find_element(*BUTTON_TOPPINGS).click()

    # Проверка наличия ингредиента "Мясо бессмертных моллюсков Protostomia" на экране
    assert browser.find_element(*INGREDIENT_MEAT_PROTOSTOMIA).is_displayed(), "Ингредиент 'Мясо бессмертных моллюсков Protostomia' не найден"

# Проверка перехода к разделу "Булки" и наличия ингредиента "Флюоресцентная булка R2-D3"
@pytest.mark.usefixture("registration", "login")
def test_button_rolls(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Проверка, что мы оказались на главной странице
    if not browser.current_url.startswith(MAIN_PAGE_URL):
        print("После входа не вернулись на главную страницу")

    # Нажатие на кнопку "Соусы"
    browser.find_element(*BUTTON_SAUCES).click()

    # Проверка наличия ингредиента "Соус Spicy-X" на экране
    if not browser.find_element(*INGREDIENT_SAUCE_SPICY_X).is_displayed():
        print("Ингредиент 'Соус Spicy-X' не найден")

    # Нажатие на кнопку "Булки"
    browser.find_element(*BUTTON_ROLLS).click()

    # Проверка наличия ингредиента "Флюоресцентная булка R2-D3" на экране
    assert browser.find_element(*INGREDIENT_BUN_R2_D3).is_displayed(), "Ингредиент 'Флюоресцентная булка R2-D3' не найден"