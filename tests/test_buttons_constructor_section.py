from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import BUTTON_ROLLS, BUTTON_SAUCES, BUTTON_TOPPINGS, INGREDIENT_SAUCE_SPICY_X, INGREDIENT_MEAT_PROTOSTOMIA, INGREDIENT_BUN_R2_D3
from urls import MAIN_PAGE_URL

# Проверка перехода к разделу "Соусы" и наличия ингредиента "Соус Spicy-X"
@pytest.mark.usefixture("registration", "login")
def test_button_sauces(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Соусы"
    browser.find_element(*BUTTON_SAUCES).click()

    # Проверка наличия ингредиента "Соус Spicy-X" на экране
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(INGREDIENT_SAUCE_SPICY_X))

    # Получение класса элемента после клика
    element = browser.find_element(*BUTTON_SAUCES)
    class_attribute = element.get_attribute("class")
    assert "tab_tab_type_current" in class_attribute, "Класс активного элемента не найден"

# Проверка перехода к разделу "Начинки" и наличия ингредиента "Мясо бессмертных моллюсков Protostomia"
@pytest.mark.usefixture("registration", "login")
def test_button_toppings(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Начинки"
    browser.find_element(*BUTTON_TOPPINGS).click()

    # Проверка наличия ингредиента "Мясо бессмертных моллюсков Protostomia" на экране
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(INGREDIENT_MEAT_PROTOSTOMIA))

    # Получение класса элемента после клика
    element = browser.find_element(*BUTTON_TOPPINGS)
    class_attribute = element.get_attribute("class")
    assert "tab_tab_type_current" in class_attribute, "Класс активного элемента не найден"

# Проверка перехода к разделу "Булки" и наличия ингредиента "Флюоресцентная булка R2-D3"
@pytest.mark.usefixture("registration", "login")
def test_button_rolls(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Соусы"
    browser.find_element(*BUTTON_SAUCES).click()

    # Проверка наличия ингредиента "Соус Spicy-X" на экране
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(INGREDIENT_SAUCE_SPICY_X))

    # Нажатие на кнопку "Булки"
    browser.find_element(*BUTTON_ROLLS).click()

    # Проверка наличия ингредиента "Флюоресцентная булка R2-D3" на экране
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(INGREDIENT_BUN_R2_D3))

    # Получение класса элемента после клика
    element = browser.find_element(*BUTTON_ROLLS)
    class_attribute = element.get_attribute("class")
    assert "tab_tab_type_current" in class_attribute, "Класс активного элемента не найден"