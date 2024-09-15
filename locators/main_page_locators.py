from selenium.webdriver.common.by import By


class MainPageLocators:
    OVERLAY = By.XPATH, '//*[contains(@class, "Modal_modal__loading")]/following::*[@class="Modal_modal_overlay__x2ZCr"]'
    BUN_N200I = By.XPATH, './/*[contains(@href, "61c0c5a71d1f82001bdaaa6c")]'  # Краторная булка
    DETAILS_POP_UP = By.XPATH, '//*[text()="Детали ингредиента"]'  #  Детали ингредиента
    POP_UP_OPENED = By.XPATH, './*[contains(@class,"Modal_modal_opened")]'  # всплывающее окно открыто
    CLOSE_POP_UP_BUTTON = By.XPATH, (
        '//*[contains(@class, "Modal_modal__contentBox")]/following::*[contains(@class, "Modal_modal__close")][1]')
    MAKE_BURGER = By.XPATH, './/*[text()="Соберите бургер"]'  # заголовок раздела Конструктор
    BASKET = By.XPATH, '//*[contains(@class, "BurgerConstructor_basket__list__l9dp_")]'
    COUNTER_2 = By.XPATH, '(.//*[contains(@class, "counter_counter__num__3nue1")])[2]'

    MAKE_ORDER_BUTTON = By.XPATH, './/*[text()="Оформить заказ"]'
    ORDER_IN_WORK = By.XPATH, './/*[text()="Ваш заказ начали готовить"]'

    CLOSE_BUTTON_DETAILS = By.XPATH, (
        '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//button')
