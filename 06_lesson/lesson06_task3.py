from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4
        )

        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        print(f"Найдено изображений: {len(images)}")

        if len(images) >= 3:
            third_image = images[2]
            src_value = third_image.get_attribute("src")
            print(f"Атрибут src 3-й картинки: {src_value}")

        else:
            raise Exception(f"Ошибка: найдено только {len(images)} изображений (нужно минимум 3)")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    main()
