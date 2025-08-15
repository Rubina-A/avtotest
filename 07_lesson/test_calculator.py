import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
import time


@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


@allure.feature("Тесты медленного калькулятора")
def test_calculator_with_delay(driver):
    with allure.step("Открытие страницы калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator = CalculatorPage(driver)

    with allure.step("Установка задержки вычислений"):
        calculator.set_delay("45")

    with allure.step("Ввод выражения для вычисления"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")

    start_time = time.time()

    with allure.step("Запуск вычисления"):
        calculator.click_button("=")

    with allure.step("Ожидание результата вычисления"):
        calculator.wait_for_calculation(50)

    with allure.step("Проверка результата вычисления"):
        assert calculator.get_result() == "15"
        elapsed_time = time.time() - start_time
        assert 45 <= elapsed_time <= 50, f"Вычисление заняло {elapsed_time} секунд вместо ожидаемых 45"