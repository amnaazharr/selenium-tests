# tests/test_login_and_logout.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # You can replace with your preferred WebDriver
    yield driver
    driver.quit()

def test_login_and_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()

    # Perform login
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()

    # Perform logout
    login_page.logout()
    assert login_page.is_logged_out()
