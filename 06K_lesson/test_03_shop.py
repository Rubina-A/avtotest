import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shopping_cart_total(browser):
    browser.get("https://www.saucedemo.com/")

    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    login_btn = browser.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_to_cart_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, item_xpath)))
        add_to_cart_btn.click()

    cart_icon = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    checkout_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    first_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "first-name")))
    last_name = browser.find_element(By.ID, "last-name")
    postal_code = browser.find_element(By.ID, "postal-code")

    first_name.send_keys("Иван")
    last_name.send_keys("Петров")
    postal_code.send_keys("123456")

    continue_btn = browser.find_element(By.ID, "continue")
    continue_btn.click()

    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text
    assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, но получено {total_text}"
