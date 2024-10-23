from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

# Переход на страницу
driver.get('http://uitestingplayground.com/textinput')

# Ввод текста в поле ввода и клик по кнопке
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#newButtonName'))
).send_keys('SkyPro')

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#updatingButton'))
).click()

# Ожидание обновления текста кнопки и вывод нового текста
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, '#updatingButton'), 'SkyPro'))

button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(button_text)

# Закрытие браузера
driver.quit()
