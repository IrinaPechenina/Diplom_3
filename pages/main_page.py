
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data

class MainPage(BasePage):

    @allure.step('Клик по ингредиенту Краторная булка N-200i')
    def click_on_bun_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_N200I)

    @allure.step('Во всплывающем окне находим текст "Детали ингредиента"')
    def find_details_text(self):
        self.find_element_with_wait(MainPageLocators.DETAILS_POP_UP)
        return self.get_text_from_element(MainPageLocators.DETAILS_POP_UP)

    @allure.step('Клик по крестику - закрыть всплывающее окно деталей ингредиента')
    def click_on_close_popup_button(self):
        self.click_on_element(MainPageLocators.CLOSE_POP_UP_BUTTON)

    @allure.step('После закрытия всплаывающего окна на главной странице найти текст Соберите бургер"')
    def find_text_make_burger_after_popup_close(self):
        self.find_element_with_wait(MainPageLocators.MAKE_BURGER)
        return self.get_text_from_element(MainPageLocators.MAKE_BURGER)

    @allure.step('Перетаскиваем элемент в корзину заказа')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop(MainPageLocators.BUN_N200I, MainPageLocators.BASKET)

    @allure.step('Проверяем счетчик')
    def count_ingredients(self):
        return self.get_text_from_elements(MainPageLocators.COUNTER_2)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_make_order_button(self):
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Создаем заказ, нажимаем на кнопку "Оформить заказ"')
    def make_order(self):
        self.drag_and_drop_ingredient()
        self.click_on_make_order_button()

    @allure.step('Проверяем текст во всплывающем окне - "Ваш заказ начали готовить"')
    def receive_order_in_work_text(self):
        return self.get_text_from_element(MainPageLocators.ORDER_IN_WORK)

    @allure.step('Закрыть окно с деталями заказа')
    def close_window_with_details(self):
        # self.wait_for_visibility(MainPageLocators.CLOSE_BUTTON_DETAILS)
        self.click_on_element_with_wait(MainPageLocators.CLOSE_BUTTON_DETAILS)

    @allure.step('Ожидание исчезновения модального окна')
    def wait_for_overlay_disappearance(self):
        try:
            (WebDriverWait(self.driver, data.TIMEOUT_2).until_not
             (expected_conditions.visibility_of_element_located(MainPageLocators.OVERLAY)))
        except TimeoutException:
            raise TimeoutException(f'Оверлей не исчезает, время ожидания:, {data.TIMEOUT_2}')
