
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
        account_page.log_in()  # вход в личный кабинет
        switch_page.click_on_constructor_button()  # переход на страницу Конструктор
        main_page.make_order()  # собираем заказ: ингредиенты в корзину, клик "Оформить заказ", закрыть окно
        main_page.close_window_with_details()  # закрываем окно Детали заказа
        switch_page.click_on_orders_list_button()  # переход на страницу Лента заказов
        order_number_order_list = orders_list_page.receive_orders_number_from_order_list()  # получаем номер заказа
        # из списка заказов
        order_number_history = orders_list_page.receive_orders_number_history()  # получаем номер заказа из ИСТОРИИ
        assert order_number_order_list == order_number_history
        print(f'номер заказа в Листе заказа: {order_number_order_list}, '
              f'номер заказа в Истории заказа: {order_number_history}')

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_in_work(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()  # вход в личный кабинет
        switch_page.click_on_constructor_button()  # переход на страницу Конструктор
        main_page.make_order()  # собираем заказ: ингредиенты в корзину, клик "Оформить заказ", закрыть окно
        main_page.close_window_with_details()  # закрываем окно Детали заказа
        switch_page.click_on_orders_list_button()  # переход на страницу Лента заказов
        order_number_order_list = orders_list_page.receive_orders_number_from_order_list()  # получаем номер заказа
        # из списка заказов
        order_number_history = orders_list_page.receive_orders_number_history()  # получаем номер заказа из ИСТОРИИ
        order_number_in_work = orders_list_page.receive_orders_number_in_work_list()
        assert order_number_in_work in order_number_order_list
        print(f'номер заказа в Листе заказа: {order_number_order_list},\n'
                f'номер заказа в Истории заказа: {order_number_history}, в работе: {order_number_in_work}')

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено ЗА ВСЁ ВРЕМЯ увеличивается')
    def test_orders_done_alltime(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()  # вход в личный кабинет
        switch_page.click_on_orders_list_button()  # переход на страницу Лента заказов
        before_order = orders_list_page.receive_number_orders_done_alltime() # количество заказов ДО создания нового
        switch_page.click_on_constructor_button()  # переход на страницу Конструктор
        main_page.make_order()  # собираем заказ - перетаскиваем ингредиенты в корзину, клик "Оформить заказ"
        main_page.close_window_with_details()  # закрываем окно Детали заказа
        switch_page.click_on_orders_list_button()  # переход на страницу Лента заказов
        after_order = orders_list_page.receive_number_orders_done_alltime()  # количество заказов ПОСЛЕ создания нового
        assert int(after_order) == int(before_order) + 1
        print(f'количество заказов ДО создания нового: {before_order},\n'
                f'количество заказов ПОСЛЕ создания нового: {after_order}')

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено ЗА СЕГОДНЯ увеличивается')
    def test_orders_done_today(self, orders_list_page, account_page, main_page, switch_page):
        account_page.log_in()  # вход в личный кабинет
        switch_page.click_on_orders_list_button()  # переход на страницу Лента заказов
        before_order = orders_list_page.receive_number_orders_done_today() # количество заказов ДО создания нового
        switch_page.click_on_constructor_button()  # переход на страницу Конструктор
        main_page.make_order()  # собираем заказ - перетаскиваем ингредиенты в корзину, клик "Оформить заказ"
        main_page.close_window_with_details()  # закрываем окно Детали заказа
        switch_page.click_on_orders_list_button()  # переход на страницу Лента заказов
        after_order = orders_list_page.receive_number_orders_done_today()  # количество заказов ПОСЛЕ создания нового
        assert int(after_order) == int(before_order) + 1
        print(f'количество заказов ДО создания нового: {before_order},\n'
                f'количество заказов ПОСЛЕ создания нового: {after_order}')

        #  тесты пройдены успешно
