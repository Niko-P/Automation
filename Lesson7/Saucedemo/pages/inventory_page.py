from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self, product_id):
        button = self.browser.find_element(By.ID, f"add-to-cart-{product_id}")
        button.click()

    def go_to_cart(self):
        self.browser.find_element(By.ID, "shopping_cart_container").click()
