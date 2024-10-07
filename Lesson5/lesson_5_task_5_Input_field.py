import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка драйвера
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()
    ))

# Открыть страницу
driver.get('http://the-internet.herokuapp.com/inputs')

# Найти поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

# Ввести текст 1000
input_field.send_keys("1000")
time.sleep(1)  # Ожидание для визуального наблюдения

# Очистить поле ввода
input_field.clear()
time.sleep(1)  # Ожидание для визуального наблюдения

# Ввести текст 999
input_field.send_keys("999")
time.sleep(1)  # Ожидание для визуального наблюдения

# Ожидание перед завершением работы
time.sleep(2)

# Закрыть браузер
driver.quit()
