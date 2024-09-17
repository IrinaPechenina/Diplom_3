
import allure
import data


class TestSwitchPage:

    @allure.title('Проверяем переход по клику "Личный кабинет"')
    def test_switch_personal_account(self, switch_page):
        switch_page.click_on_enter_account_button()
        result = switch_page.find_enter_button()
        assert result == data.ENTER_TEXT

    @allure.title('Проверяем переход по клику "Лента заказов"')
    def test_switch_orders_list(self, switch_page):
        switch_page.click_on_orders_list_button()
        result = switch_page.find_text_orders_are_ready()
        assert result == data.ORDERS_ARE_READY

    @allure.title('Проверяем переход по клику на "Конструктор"')
    def test_switch_to_constructor(self, switch_page):
        switch_page.click_on_constructor_button()
        result = switch_page.find_text_make_burger()
        assert result == data.MAKE_BURGER_TEXT
