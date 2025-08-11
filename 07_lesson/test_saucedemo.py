import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from saucedemo_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_saucedemo_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.click_continue()

    assert checkout_page.get_total() == "Total: $58.29"
