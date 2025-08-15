import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcMainPage:
    def __init__(self, driver):
        """
        Конструктор класса CalcMainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        :return: None
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step("Нажатие кнопки '{button}'")
    def click_button(self, button: str) -> None:
        """
        Нажимает на кнопку калькулятора.

        :param button: str — текст на кнопке, которую нужно нажать.
        :return: None
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Нажатие кнопок: {buttons}")
    def click_buttons(self, buttons: list[str]) -> None:
        """
        Нажимает на несколько кнопок калькулятора по очереди.

        :param buttons: list[str] — список кнопок.
        :return: None
        """
        for button in buttons:
            self.click_button(button)

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result: str, delay: int) -> None:
        """
        Ожидает появления ожидаемого результата.

        :param expected_result: str — ожидаемый результат.
        :param delay: int — задержка в секундах.
        :return: None
        """
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self) -> str:
        """
        Получает текущий результат с экрана калькулятора.

        :return: str — текст результата.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text
