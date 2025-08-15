from selenium.webdriver.common.by import By


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