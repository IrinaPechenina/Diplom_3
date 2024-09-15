import allure
import data


class TestPasswordRecoveryPage:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_switch_password_recovery(self, password_recovery_page):
        password_recovery_page.click_on_password_recovery_button()
        result = password_recovery_page.find_recover_button()
        assert result == data.RECOVER_TEXT

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_set_email_and_click_on_recover_button(self, password_recovery_page):
        password_recovery_page.go_to_reset_password()
        result = password_recovery_page.find_password_placeholder_text()
        assert result == data.PASSWORD_TEXT

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_button_show_hide_password(self, password_recovery_page):
        password_recovery_page.go_to_reset_password()
        password_recovery_page.click_on_action_icon_button()
        result = password_recovery_page.action_icon_button_on()
        assert result == data.PASSWORD_TEXT

    # тесты пройдены успешно
