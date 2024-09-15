import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
import allure


class AccountPage(BasePage):

    @allure.step('Клик по кнопке Личный кабинет') # Исправить сделать ссылку  на switch page
    def click_on_enter_account_button(self):
        self.click_on_element(AccountPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('На странице личного кабинета поиск кнопки "Войти"')
    def find_enter_button(self):
        self.find_element_with_wait(AccountPageLocators.ENTER_BUTTON)
        return self.get_text_from_element(AccountPageLocators.ENTER_BUTTON)

    @allure.step('Вход в личный кабинет по логину и паролю')
    def log_in(self):
        self.get_url(data.LOGIN_URL)
        self.set_text_to_element(AccountPageLocators.EMAIL_INPUT, data.EMAIL)
        self.set_text_to_element(AccountPageLocators.PASSWORD_INPUT, data.PASSWORD)
        self.click_on_element(AccountPageLocators.ENTER_BUTTON)
        self.click_on_enter_account_button()

    @allure.step('Клик по кнопке «История заказов»')
    def click_on_order_list_button(self):
        self.click_on_element(AccountPageLocators.ORDERS_LIST_BUTTON)

    @allure.step('В разделе "История заказов" найти заказ с текстом "Выполнен"')
    def find_order_history_element(self):
        self.find_element_with_wait(AccountPageLocators.ORDERS_HISTORY)
        return self.get_text_from_element(AccountPageLocators.ORDERS_HISTORY)

    @allure.step('выход из аккаунта»')
    def click_on_exit_from_account_button(self):
        self.click_on_element(AccountPageLocators.EXIT_ACCOUNT_BUTTON)
