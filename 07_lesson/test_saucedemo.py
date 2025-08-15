import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


@allure.feature("Процесс оформления заказа в SauceDemo")
def test_saucedemo_checkout(driver):
    with allure.step("Открытие страницы авторизации"):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)

    with allure.step("Авторизация стандартного пользователя"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение информации для оформления"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("John", "Doe", "12345")
        checkout_page.click_continue()

    with allure.step("Проверка итоговой суммы"):
        # Явное ожидание загрузки элемента с итоговой суммой
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(checkout_page.total_label)
        )
        assert checkout_page.get_total() == "Total: $58.29"