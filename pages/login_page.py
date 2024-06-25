# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Wait for inventory page to load after login
        WebDriverWait(self.driver, 10).until(EC.url_contains("/inventory.html"))

    def logout(self):
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()

        # Wait for login page to load after logout
        WebDriverWait(self.driver, 10).until(EC.url_contains("/index.html"))

    def is_logged_in(self):
        return "/inventory.html" in self.driver.current_url

    def is_logged_out(self):
        return "/index.html" in self.driver.current_url
