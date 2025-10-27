from selenium.webdriver.common.by import By

# Локаторы для файла test_registration_stellar_burgers.py
NAME_INPUT = (By.CSS_SELECTOR, ".input_type_text input[name='name']")  # Поле ввода имени
EMAIL_INPUT = (By.CSS_SELECTOR, ".input_type_text input[name='email']")  # Поле ввода email
PASSWORD_INPUT = (By.CSS_SELECTOR, ".input_type_password input[name='password']")  # Поле ввода пароля
REGISTER_BUTTON = (By.CSS_SELECTOR, ".button_button_type_primary__1O7Bx")  # Кнопка регистрации
ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")  # Сообщение об ошибке для пароля

# Локаторы для файла test_stellar_burgers_login.py
BUTTON_LOGIN_ACCOUNT = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg") # кнопка «Войти в аккаунт» на главной
INPUT_EMAIL = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[name='name']") # Поле ввода email
INPUT_PASSWORD = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[type='password']") # Поле ввода пароля
BUTTON_SIGN_IN = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa") # кнопка "Войти" на странице входа
BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # кнопка "Личный кабинет"
BUTTON_SIGN_IN_FROM_REGISTRATION = (By.CSS_SELECTOR, ".Auth_link__1fOlj")  # кнопка "Войти" в форме регистрации и в форме восстановления пароля

# Локаторы для файла test_from_profile_to_constructor.py
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # кнопка "Конструктор"
LOGO_STELLAR_BURGERS = (By.CSS_SELECTOR, "svg[width='290'][height='50']") # логотип Stellar Burgers

# Локаторы для файла test_logout_of_account.py
BUTTON_EXIT = (By.CSS_SELECTOR, ".Account_button__14Yp3.text_type_main-medium") # кнопка "Выход"

# Локаторы для файла test_buttons_constructor_section.py
BUTTON_SAUCES = (By.XPATH, "//span[text()='Соусы']") # кнопка "Соусы"
BUTTON_ROLLS = (By.XPATH, "//span[text()='Булки']") # кнопка "Булки"
BUTTON_TOPPINGS = (By.XPATH, "//span[text()='Начинки']") # кнопка "Начинки"

INGREDIENT_SAUCE_SPICY_X = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__text__yp3dH:contains('Соус Spicy-X')") # ингредиент "Соус Spicy-X"
INGREDIENT_MEAT_PROTOSTOMIA = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__text__yp3dH:contains('Мясо бессмертных моллюсков Protostomia')") # ингредиент "Мясо бессмертных моллюсков Protostomia"
INGREDIENT_BUN_R2_D3 = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__text__yp3dH:contains('Флюоресцентная булка R2-D3')") # ингредиент "Флюоресцентная булка R2-D3"