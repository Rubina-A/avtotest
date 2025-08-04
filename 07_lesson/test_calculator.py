import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator_with_delay(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = CalculatorPage(driver)

    calculator.set_delay("45")

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")

    start_time = time.time()

    calculator.click_button("=")

    calculator.wait_for_calculation(50)

    assert calculator.get_result() == "15"

    elapsed_time = time.time() - start_time
    assert 45 <= elapsed_time <= 50, f"Вычисление заняло {elapsed_time} секунд вместо ожидаемых 45"
