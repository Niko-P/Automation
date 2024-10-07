from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Указать путь к ChromeDriver
chrome = webdriver.Chrome()

# Шаг 1: Открыть страницу
chrome.get('http://the-internet.herokuapp.com/add_remove_elements/')
# Шаг 2: Найти кнопку "Add Element" и кликнуть по ней 5 раз
for i in range(5):
    add_Button = chrome.find_element(
        By.XPATH, ("//button[text()='Add Element']")
        )
    add_Button.click()
sleep(3)
# Шаг 3: Собрать список всех кнопок "Delete"
chrome_delete_buttons = chrome.find_elements(
    By.XPATH, '//button[text()="Delete"]'
    )
# Шаг 4: Вывести количество кнопок "Delete"
print(f"Размер списка кнопок Delete: {len(chrome_delete_buttons)}")

# Закрыть браузер
chrome.quit()
