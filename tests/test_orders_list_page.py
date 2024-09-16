
import allure
import data


class TestOrderListPage:

    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями заказа')
    def test_click_on_order_open_order_details(self, orders_list_page):
        orders_list_page.click_on_first_order()
        result = orders_list_page.receive_text_from_order_details_popup()
        assert result == data.ELEMENT_FROM_POPUP_TEXT

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» '
                  'отображаются на странице «Лента заказов»,')
    def test_order_number_in_order_history(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        order_number_order_list = orders_list_page.receive_orders_number_from_order_list()
        order_number_history = orders_list_page.receive_orders_number_history()
        assert order_number_order_list == order_number_history
        print(f'номер заказа в Листе заказа: {order_number_order_list}, '
              f'номер заказа в Истории заказа: {order_number_history}')

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_in_work(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        order_number_order_list = orders_list_page.receive_orders_number_from_order_list()
        order_number_history = orders_list_page.receive_orders_number_history()
        order_number_in_work = orders_list_page.receive_orders_number_in_work_list()
        assert order_number_in_work in order_number_order_list
        print(f'номер заказа в Листе заказа: {order_number_order_list},\n'
                f'номер заказа в Истории заказа: {order_number_history}, в работе: {order_number_in_work}')

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено ЗА ВСЁ ВРЕМЯ увеличивается')
    def test_orders_done_alltime(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()
        switch_page.click_on_orders_list_button()
        before_order = orders_list_page.receive_number_orders_done_alltime()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        after_order = orders_list_page.receive_number_orders_done_alltime()
        assert int(after_order) == int(before_order) + 1
        print(f'количество заказов ДО создания нового: {before_order},\n'
                f'количество заказов ПОСЛЕ создания нового: {after_order}')

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено ЗА СЕГОДНЯ увеличивается')
    def test_orders_done_today(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()
        switch_page.click_on_orders_list_button()
        before_order = orders_list_page.receive_number_orders_done_today()
        switch_page.click_on_constructor_button()
        main_page.make_order()
        main_page.close_window_with_details()
        switch_page.click_on_orders_list_button()
        after_order = orders_list_page.receive_number_orders_done_today()
        assert int(after_order) == int(before_order) + 1
        print(f'количество заказов ДО создания нового: {before_order},\n'
                f'количество заказов ПОСЛЕ создания нового: {after_order}')
