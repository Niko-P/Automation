# Lesson7/Data_types/main_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .data import (
    first_name,
    last_name,
    address,
    email,
    phone_number,
    zip_code,
    city,
    country,
    job_position,
    company,
    url
)


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(url)

    def fill_form(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        ).send_keys(first_name)

        self.browser.find_element(By.NAME, "last-name").send_keys(last_name)
        self.browser.find_element(By.NAME, "address").send_keys(address)
        self.browser.find_element(By.NAME, "e-mail").send_keys(email)
        self.browser.find_element(By.NAME, "phone").send_keys(phone_number)
        self.browser.find_element(By.NAME, "zip-code").send_keys(zip_code)
        self.browser.find_element(By.NAME, "city").send_keys(city)
        self.browser.find_element(By.NAME, "country").send_keys(country)
        self.browser.find_element(
            By.NAME, "job-position").send_keys(job_position)
        self.browser.find_element(By.NAME, "company").send_keys(company)

    def submit(self):
        submit_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )
        submit_button.click()

    def get_field_class(self, field_name):
        return self.browser.find_element(
            By.ID, field_name).get_attribute("class")
