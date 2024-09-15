from selenium.webdriver.common.by import By


class AccountPageLocators:

    ENTER_ACCOUNT_BUTTON = By.XPATH, '//*[text()="Личный Кабинет"]'  # кнопка входа в «Личный кабинет»
    EXIT_ACCOUNT_BUTTON = By.XPATH, '//*[text()="Выход"]'  # кнопка «Выход» из личного кабинета
    ORDERS_LIST_BUTTON = By.XPATH, '//*[text()="История заказов"]'  # кнопка «История заказов» в личном кабинете
    ORDERS_HISTORY = By.XPATH, '//*[text()="Выполнен"]'  # текст в разделе «История заказов»

    # Форма регистрации
    NAME_FIELD = By.XPATH, '(.//input[@type="text"])[1]'  # Поле ввода "Имя"
    EMAIL_FIELD = By.XPATH, '(.//input[@type="text"])[2]'  # Поле ввода "Email"
    PASSWORD_FIELD = By.XPATH, './/input[@type="password"]'  # Поле ввода "Пароль"
    CONFIRM_REGISTRATION = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка 'Зарегистрироваться'
    REGISTRATION_ERROR_MESSAGE = By.XPATH, './/p[text()="Некорректный пароль"]'  # ошибка некорретного пароля

    # Вход в личный кабинет
    EMAIL_INPUT = By.XPATH, './/input[@name="name"]'  # Поле ввода Email в личном кабинете
    PASSWORD_INPUT = By.XPATH, './/input[@type="password"]'  # Поле ввода пароля в личном кабинете
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка "Войти" после успешн регистрации
