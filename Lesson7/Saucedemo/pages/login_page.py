from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(self.URL)

    def login(self, username, password):
        self.browser.find_element(By.ID, "user-name").send_keys(username)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()
