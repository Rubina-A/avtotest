import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор страницы логина.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ввод имени пользователя: {username}")
    def enter_username(self, username: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def click_login(self) -> None:
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver):
        """
        Конструктор страницы товаров.
        """
        self.driver = driver

    @allure.step("Добавление в корзину: Sauce Labs Backpack")
    def add_backpack(self) -> None:
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    @allure.step("Добавление в корзину: Sauce Labs Bolt T-Shirt")
    def add_tshirt(self) -> None:
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("Добавление в корзину: Sauce Labs Onesie")
    def add_onesie(self) -> None:
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение данных покупателя: {first_name} {last_name}")
    def fill_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    @allure.step("Нажатие кнопки Continue")
    def click_continue(self) -> None:
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение суммы заказа")
    def get_total(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
