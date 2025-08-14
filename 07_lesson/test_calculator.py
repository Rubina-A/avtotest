import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalcMainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест калькулятора: {num1} {operation} {num2} = {expected_result}")
@allure.description("Проверка работы калькулятора с разными операциями и задержкой.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 5),
    ],
)
def test_calculator_flow(driver, num1, operation, num2, expected_result, delay):
    page = CalcMainPage(driver)

    page.open()
    page.set_delay(delay)
    page.click_buttons([num1, operation, num2, "="])
    page.wait_for_result(expected_result, delay)

    assert page.get_result() == expected_result
