from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//*[text()="Восстановить пароль"]'  # кнопка Восстановить пароль
    RECOVER_BUTTON = By.XPATH, '//*[text()="Восстановить"]'  # кнопка Восстановить
    EMAIL_INPUT = By.XPATH, './/input[@name="name"]'  # Поле ввода Email
    PASSWORD_PLACEHOLDER = By.XPATH, '//*[text()="Пароль"]'   # плейсхолдер ввода пароля
    ACTION_ICON_BUTTON = By.XPATH, './/div[@class="input__icon input__icon-action"]'  # кнопка показать/скрыть пароль
    ACTION_ICON_BUTTON_ON = By.XPATH, './/*[contains(@class, "placeholder-focused") and text()="Пароль"]'
