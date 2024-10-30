from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_information(self, first_name, last_name, postal_code):
        self.browser.find_element(By.ID, "first-name").send_keys(first_name)
        self.browser.find_element(By.ID, "last-name").send_keys(last_name)
        self.browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.browser.find_element(By.ID, "continue").click()

    def get_total_price(self):
        total_label = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
                ))
        return total_label.text.strip().replace("Total: $", "")
