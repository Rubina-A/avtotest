from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы авторизации"""
    
    def __init__(self, driver):
        self.driver = driver
        # Локаторы элементов
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        """Ввод имени пользователя"""
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        """Ввод пароля"""
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        """Клик по кнопке входа"""
        self.driver.find_element(*self.login_button).click()
