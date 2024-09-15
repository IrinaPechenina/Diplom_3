import data
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage
import allure


class SwitchPage(BasePage):
    @allure.step('Клик по кнопке Личный кабинет')
    def click_on_enter_account_button(self):
        self.click_on_element(SwitchPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('На странице личного кабинета поиск кнопки "Войти"')
    def find_enter_button(self):
        self.find_element_with_wait(SwitchPageLocators.ENTER_BUTTON)
        return self.get_text_from_element(SwitchPageLocators.ENTER_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_orders_list_button(self):
        self.click_on_element(SwitchPageLocators.ORDERS_LIST_BUTTON)

    @allure.step('На странице Ленты заказов поиск теста, потверждающего готовность заказов"')
    def find_text_orders_are_ready(self):
        self.find_element_with_wait(SwitchPageLocators.ORDERS_ARE_READY_TEXT)
        return self.get_text_from_element(SwitchPageLocators.ORDERS_ARE_READY_TEXT)

    @allure.step('Переход по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.get_url(data.LOGIN_URL)
        self.click_on_element(SwitchPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('На странице Конструктор найти текст Соберите бургер"')
    def find_text_make_burger(self):
        self.find_element_with_wait(SwitchPageLocators.MAKE_BURGER)
        return self.get_text_from_element(SwitchPageLocators.MAKE_BURGER)
