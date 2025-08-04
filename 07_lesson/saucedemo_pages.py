from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.item_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.item_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.driver.find_element(*self.item_backpack).click()

    def add_tshirt(self):
        self.driver.find_element(*self.item_tshirt).click()

    def add_onesie(self):
        self.driver.find_element(*self.item_onesie).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        return self.driver.find_element(*self.total_label).text
