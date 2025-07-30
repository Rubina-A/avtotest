from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def click_blue_button():
    driver = setup_driver()
    try:
        driver.get("http://uitestingplayground.com/classattr")
        print("Страница успешно загружена")

        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        print("Синяя кнопка найдена")

        blue_button.click()
        print("Успешный клик по синей кнопке")

        try:
            alert = driver.switch_to.alert
            print(f"Текст алерта: {alert.text}")
            alert.accept()
        except:
            pass

        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    print("=== Запуск теста кнопки ===")
    click_blue_button()
