from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)


try:
    driver.set_window_size(1024, 768)

    driver.get("http://uitestingplayground.com/textinput")
    print(f"Title страницы: {driver.title}")
    print(f"Текущий URL: {driver.current_url}")

    input_field = driver.find_element(By.ID, "newButtonName")
    print(f"Поле ввода доступно: {input_field.is_enabled()}")
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    print(f"Кнопка отображается: {button.is_displayed()}")
    print(f"Исходный текст кнопки: {button.text}")

    button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    updated_button = driver.find_element(By.ID, "updatingButton")
    print(f"Новый текст кнопки: {updated_button.text}")
    assert updated_button.text == "SkyPro", "Текст кнопки не изменился"


finally:
    driver.quit()
    print("Браузер закрыт")
