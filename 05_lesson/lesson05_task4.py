from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time


def setup_driver():
    firefox_options = Options()
    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    firefox_options.add_argument("--start-maximized")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    return driver


def test_login():
    driver = setup_driver()
    try:
        driver.get("http://the-internet.herokuapp.com/login")
        print("Страница логина загружена")
        time.sleep(2)

        username = driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        print("Логин введен")

        password = driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")
        print("Пароль введен")

        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()
        print("Кнопка Login нажата")
        time.sleep(2)

        flash_message = driver.find_element(By.ID, "flash")
        message_text = flash_message.text.split("\n")[0]
        print(f"Сообщение об успехе: {message_text}")

        time.sleep(3)

    except Exception as e:
        print(f"Ошибка при выполнении теста: {str(e)}")
    finally:
        driver.quit()
        print("Тест завершен. Браузер закрыт.")


if __name__ == "__main__":
    print("=== Тестирование логина ===")
    test_login()
