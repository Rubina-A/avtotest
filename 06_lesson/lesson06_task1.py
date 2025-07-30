from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.set_window_size(1200, 800)

    driver.get("http://uitestingplayground.com/ajax")

    print(f"Title страницы: {driver.title}")
    print(f"Текущий URL: {driver.current_url}")

    button = driver.find_element(By.ID, "ajaxButton")
    print(f"Кнопка отображается: {button.is_displayed()}")
    print(f"Кнопка активна: {button.is_enabled()}")
    print(f"Атрибуты кнопки: class={button.get_attribute('class')}, id={button.get_attribute('id')}")

    button.click()

    success_message = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    message_text = success_message.text
    print(f"Текст плашки: {message_text}")

    assert message_text == "Data loaded with AJAX get request.", "Текст не совпадает"


finally:
    driver.quit()
    print("Браузер закрыт")
