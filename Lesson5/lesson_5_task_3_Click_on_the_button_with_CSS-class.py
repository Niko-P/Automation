from selenium import webdriver
from time import sleep

# Открытие браузера
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# Найти синюю кнопку и кликнуть на неё
blue_button = driver.find_element(
    "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), \
        ' btn-primary ')]"
)
blue_button.click()

# Обработка всплывающего окна
sleep(2)
driver.switch_to.alert.accept()

# Подтверждение действия
print("Скрипт успешно кликнул на синюю кнопку и обработал всплывающее окно.")

# Закрыть браузер
sleep(1)
driver.quit()

# Запустить скрипт три раза подряд. Убедиться, что он отработает одинаково
