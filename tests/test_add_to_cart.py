import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.product_page import ProductPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    product_page = ProductPage(driver)
    product_page.login("standard_user", "secret_sauce")
    product_page.go_to_product("Sauce Labs Backpack")
    product_page.add_to_cart()

    # Verify that the product has been added to the cart
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.is_displayed()
