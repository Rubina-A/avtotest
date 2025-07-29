from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Максимизировать окно

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def test_dynamic_button():
    driver = setup_driver()
    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        print("Страница успешно загружена")

        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        print("Синяя кнопка найдена")

        blue_button.click()
        print("Успешный клик по кнопке с динамическим ID")

        time.sleep(2)

    except Exception as e:
        print(f"Ошибка при выполнении теста: {str(e)}")
    finally:
        driver.quit()
        print("Тест завершен. Браузер закрыт.")


if __name__ == "__main__":
    print("=== Тестирование кнопки с динамическим ID ===")
    test_dynamic_button()
