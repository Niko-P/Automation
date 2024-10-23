from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Установка явного ожидания
wait = WebDriverWait(driver, 40, 0.1)

# Переход на страницу
driver.get('http://uitestingplayground.com/ajax')

# Клик по синей кнопке
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

# Ожидание появления текста на зеленке
content = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
).text

# Текст в консоль
print(content)

# Закрытие браузера
driver.quit()
