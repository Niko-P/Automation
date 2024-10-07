import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка драйвера
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))

# Открыть страницу
driver.get('http://the-internet.herokuapp.com/login')

# Найти поле для ввода имени пользователя и ввести значение
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Найти поле для ввода пароля и ввести значение
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Найти кнопку "Login" и нажать на нее
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Ожидание перед завершением работы
time.sleep(3)  # Задержка для визуального наблюдения

# Закрыть браузер
driver.quit()
