from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):  #
        WebDriverWait(self.driver, data.TIMEOUT).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, data.TIMEOUT_2).until(expected_conditions.visibility_of_element_located(locator))

    def click_on_element(self, locator):  #
        element = self.find_element_with_wait(locator)
        element.click()

    def find_element_with_wait_to_click(self, locator):  #
        WebDriverWait(self.driver, data.TIMEOUT).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def click_on_element_with_wait(self, locator):  #
        element = self.find_element_with_wait_to_click(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def get_text_from_elements(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def drag_and_drop(self, element_from, element_to):
        action = ActionChains(self.driver)
        from_element = self.find_element_with_wait(element_from)
        to_element = self.find_element_with_wait(element_to)
        action.drag_and_drop(from_element, to_element).perform()
