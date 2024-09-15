
import allure
import data


class TestMainPage:

    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_leads_to_popup_with_details(self, main_page):
        main_page.click_on_bun_ingredient()
        result = main_page.find_details_text()
        assert result == data.DETAILS_POP_UP_TEXT

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_close_popup_button(self, main_page):
        main_page.click_on_bun_ingredient()
        main_page.click_on_close_popup_button()
        result = main_page.find_text_make_burger_after_popup_close()
        assert result == data.MAKE_BURGER_TEXT

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_add_ingredient_to_basket(self, main_page):
        main_page.drag_and_drop_ingredient()
        assert int(main_page.count_ingredients()) >= 1

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_user_with_login_make_order_success(self, account_page, switch_page, main_page):
        account_page.log_in()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        result = main_page.receive_order_in_work_text()
        assert result == data.ORDER_IN_WORK_TEXT

#  тесты пройдены успешно
