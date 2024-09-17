from selenium.webdriver.common.by import By


class OrderListPageLocators:

    CLOSE_POP_UP_BUTTON = By.XPATH, '//*[contains(@class, "Modal_modal__close")]'
    ORDER_NUMBER_IN_LIST = By.XPATH, '(.//*[contains(@class, "text text_type_digits-default")])[1]'

    FIRST_ORDER = By.XPATH, '(.//*[contains(@class, "OrderHistory_link")])[1]'  #  первый заказ
    ELEMENT_FROM_POPUP = By.XPATH, './/*[text()="Cостав"]'

    FIRST_ORDER_HISTORY = By.XPATH, '(.//*[contains(@class, "text text_type_digits-default")])[1]'  # номер заказа в
    # Истории

    ORDER_IN_WORK_NUMBER = By.XPATH, '(//*[@class="text text_type_digits-default mb-2"])[1]'  # номер в работе, перед
    # номером ноль
    ORDERS_DONE_ALLTIME = By.XPATH, '(.//*[contains(@class, "OrderFeed_number")])[1]'  # Выполнено за всё время
    ORDERS_DONE_TODAY = By.XPATH, '(.//*[contains(@class, "OrderFeed_number")])[2]'  # Выполнено за сегодня
