from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

URL_2 = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


def test_calculator_form():
    service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service)

    chrome_browser.get(URL_2)
    time.sleep(2)  # Ждем, пока страница загрузится

    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    time.sleep(1)  # Ждем ввода

    chrome_browser.find_element(By.XPATH, "//span[text()='7']").click()
    time.sleep(1)  # Ждем нажатия
    chrome_browser.find_element(By.XPATH, "//span[text()='+']").click()
    time.sleep(1)
    chrome_browser.find_element(By.XPATH, "//span[text()='8']").click()
    time.sleep(1)
    chrome_browser.find_element(By.XPATH, "//span[text()='=']").click()
    time.sleep(1)

    # Ожидание результата и проверка его
    WebDriverWait(chrome_browser, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15", f"Expected result to be '15', \
        but got '{result_text}'"

    print("Тест успешно выполнен!")

    chrome_browser.quit()


# Запускаем тест
test_calculator_form()
