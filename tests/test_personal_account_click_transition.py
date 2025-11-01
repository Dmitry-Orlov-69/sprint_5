from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import BUTTON_PERSONAL_ACCOUNT
from urls import MAIN_PAGE_URL, PERSONAL_ACCOUNT_URL

# Переход в личный кабинет по клику на «Личный кабинет»
@pytest.mark.usefixture("registration", "login")
def test_personal_account_click_transition(login):
    browser = login  # Получаем объект браузера из фикстуры

    # Ожидание перехода на главную страницу
    WebDriverWait(browser, 10).until(EC.url_contains(MAIN_PAGE_URL))

    # Нажатие на кнопку "Личный кабинет"
    browser.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Проверка перехода в личный кабинет
    assert browser.current_url == PERSONAL_ACCOUNT_URL, "Переход в личный кабинет не произошёл"