
import helpers
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
import allure


class PasswordRecoveryPage(BasePage):

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_password_recovery_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('На странице восстановления пароля найти кнопку с текстом "Восстановить"')
    def find_recover_button(self):
        self.find_element_with_wait(PasswordRecoveryPageLocators.RECOVER_BUTTON)
        return self.get_text_from_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    @allure.step('В поле ввода Email вводим данные электронной почты"')
    def set_email(self):
        email = helpers.generate_email()
        self.set_text_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_recover_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    @allure.step('На странице восстановления пароля найти кнопку с текстом "Восстановить"')
    def find_password_placeholder_text(self):
        self.find_element_with_wait(PasswordRecoveryPageLocators.PASSWORD_PLACEHOLDER)
        return self.get_text_from_element(PasswordRecoveryPageLocators.PASSWORD_PLACEHOLDER)

    @allure.step('Переход на страницу введения нового пароля')
    def go_to_reset_password(self):
        self.click_on_password_recovery_button()
        self.set_email()
        self.click_on_recover_button()

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_on_action_icon_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.ACTION_ICON_BUTTON)

    @allure.step('кнопка пароля активна')
    def action_icon_button_on(self):
        self.find_element_with_wait(PasswordRecoveryPageLocators.ACTION_ICON_BUTTON_ON)
        return self.get_text_from_element(PasswordRecoveryPageLocators.ACTION_ICON_BUTTON_ON)
