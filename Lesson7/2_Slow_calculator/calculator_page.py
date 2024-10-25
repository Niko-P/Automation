# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(self.URL)

    def set_delay(self, delay_value):
        delay_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']"))
        )
        button.click()

    def get_result(self):
        expected_result = "15"  # Пример значения для проверки
        WebDriverWait(self.browser, 50).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result)
        )
        return self.browser.find_element(By.CLASS_NAME, "screen").text
