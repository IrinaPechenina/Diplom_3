from selenium.webdriver.common.by import By


class SwitchPageLocators:
    ENTER_ACCOUNT_BUTTON = By.XPATH, '//*[text()="Личный Кабинет"]'  # кнопка входа в «Личный кабинет» -switch
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'   # кнопка "Войти" после успешн регистрации -switch
    ORDERS_ARE_READY_TEXT = By.XPATH, './/*[text()="Все текущие заказы готовы!"]'  # текст в разделе
    ORDERS_LIST_BUTTON = By.XPATH, './/*[contains(@href, "feed")]'  # кнопка "Лента заказов" -switch

    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text()="Конструктор"]'  # по клику на «Конструктор»
    MAKE_BURGER = By.XPATH, './/*[text()="Соберите бургер"]'  # заголовок раздела Конструктор