import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Установка драйвера
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))

# Открыть страницу
driver.get('http://the-internet.herokuapp.com/entry_ad')

# Ожидание появления модального окна
wait = WebDriverWait(driver, 10)
modal_window = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal"))
    )

# Ожидание элемента "Close" и клик по нему
close_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//div[@class='modal-footer']/p[text()='Close']"
    )))
time.sleep(3)  # Ожидание для визуального наблюдения
close_button.click()

# Ожидание, чтобы модальное окно закрылось
wait.until(EC.invisibility_of_element(modal_window))

# Ожидание перед завершением работы
time.sleep(2)
print("Скрипт успешно кликнул на кнопку 'Close'.")

# Закрыть браузер
driver.quit()
