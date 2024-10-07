from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Указать путь к ChromeDriver
chrome = webdriver.Chrome()

# Шаг 1: Открыть страницу
chrome.get('http://uitestingplayground.com/dynamicid')

# Шаг 2: Найти синюю кнопку по её тексту и кликнуть по ней
blue_button = chrome.find_element(
    By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"
    )
blue_button.click()

# Ожидание 2 секунды для наблюдения
sleep(2)

# Подтверждение действия
print("Скрипт успешно кликнул на синюю кнопку.")

# Закрыть браузер
chrome.quit()

# Запустить скрипт три раза подряд. Убедиться, что он отработает одинаково
