from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL_2 = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


def test_calculator_form():
    service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service)

    chrome_browser.get(URL_2)

    # Ожидание и ввод значения в поле delay
    delay_input = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.ID, "delay"))
    )
    delay_input.clear()
    delay_input.send_keys(45)

    # Ожидание и нажатие на кнопки
    chrome_browser.find_element(By.XPATH, "//span[text()='7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text()='+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text()='8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата и проверка его
    WebDriverWait(chrome_browser, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15", f"Expected result to be '15', \
        but got '{result_text}'"

    # Закрытие браузера
    chrome_browser.quit()
