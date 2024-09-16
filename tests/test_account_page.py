import allure
import data


class TestAccountPage:

    @allure.title('Проверяем переход по клику "История заказов"')
    def test_switch_order_list(self, account_page):
        account_page.log_in()
        account_page.click_on_order_list_button()
        result = account_page.find_order_history_element()
        assert result == data.IS_DONE_TEXT

    @allure.title('Проверяем выход из аккаунта')
    def test_exit_account(self, account_page):
        account_page.log_in()
        account_page.click_on_exit_from_account_button()
        result = account_page.find_enter_button()
        assert result == data.ENTER_TEXT
