from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def proceed_to_checkout(self):
        self.browser.find_element(By.ID, "checkout").click()
