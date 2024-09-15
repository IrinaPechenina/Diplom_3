
import pytest
from selenium import webdriver
import data
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.orders_list_page import OrderListPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.switch_page import SwitchPage


@pytest.fixture()
def driver():
    service = webdriver.chrome.service.Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()


@pytest.fixture
def account_page(driver):
    page = AccountPage(driver)
    page.get_url(data.HOME_PAGE_URL)
    return page


@pytest.fixture
def password_recovery_page(driver):
    page = PasswordRecoveryPage(driver)
    page.get_url(data.LOGIN_URL)
    return page


@pytest.fixture
def switch_page(driver):
    page = SwitchPage(driver)
    page.get_url(data.HOME_PAGE_URL)
    return page


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.get_url(data.HOME_PAGE_URL)
    return page


@pytest.fixture
def orders_list_page(driver):
    page = OrderListPage(driver)
    page.get_url(data.ORDER_LIST_URL)
    return page
