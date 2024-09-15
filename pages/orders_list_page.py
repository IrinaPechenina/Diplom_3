
from locators.orders_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage
import allure


class OrderListPage(BasePage):
    @allure.step('Получить номер заказа ')
    def receive_orders_number_from_order_list(self):
        return self.get_text_from_element(OrderListPageLocators.ORDER_NUMBER_IN_LIST)

    @allure.step('Клик на первый заказ в списке')
    def click_on_first_order(self):
        self.click_on_element(OrderListPageLocators.FIRST_ORDER)

    @allure.step('Получить номер заказа ')
    def receive_text_from_order_details_popup(self):
        return self.get_text_from_element(OrderListPageLocators.ELEMENT_FROM_POPUP)

    @allure.step('Получить номер заказа из Истории заказов')
    def receive_orders_number_history(self):
        return self.get_text_from_element(OrderListPageLocators.FIRST_ORDER_HISTORY)

    @allure.step('Получить номер заказа из раздела "В работе"')
    def receive_orders_number_in_work_list(self):
        return self.get_text_from_element(OrderListPageLocators.ORDER_IN_WORK_NUMBER)

    @allure.step('Получить количество выполненых заказов за все время:')
    def receive_number_orders_done_alltime(self):
        return self.get_text_from_element(OrderListPageLocators.ORDERS_DONE_ALLTIME)

    @allure.step('Получить количество выполненых заказов за сегодня:')
    def receive_number_orders_done_today(self):
        return self.get_text_from_element(OrderListPageLocators.ORDERS_DONE_TODAY)
