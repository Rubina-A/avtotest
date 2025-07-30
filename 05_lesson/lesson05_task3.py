from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time


def setup_driver():
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    return driver


def test_input_field():
    driver = setup_driver()
    try:
        driver.get("http://the-internet.herokuapp.com/inputs")
        print("Страница успешно загружена")
        time.sleep(2)

        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        print("Поле ввода найдено")

        input_field.send_keys("Sky")
        print("Введен текст 'Sky'")
        time.sleep(2)

        input_field.clear()
        print("Поле очищено")
        time.sleep(2)

        input_field.send_keys("Pro")
        print("Введен текст 'Pro'")
        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    print("=== Тестирование поля ввода ===")
    test_input_field()
