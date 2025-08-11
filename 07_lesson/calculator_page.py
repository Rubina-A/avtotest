from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "=": (By.XPATH, "//span[text()='=']"),
        }

    def set_delay(self, seconds):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(seconds)

    def click_button(self, button):
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self):
        return self.driver.find_element(*self.result_field).text

    def wait_for_calculation(self, timeout):
        initial_text = self.get_result()
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_result() != initial_text
        )
