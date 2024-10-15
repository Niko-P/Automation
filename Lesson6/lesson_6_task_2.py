from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install())
    )

# Переход на страницу
driver.get('http://uitestingplayground.com/textinput')

# Ожидание появления поля ввода
wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#newButtonName'))
)

# Ввод текста в поле ввода
input_field.send_keys('SkyPro')

# Ожидание появления кнопки и клик по ней
button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '#updatingButton'))
)
button.click()

# Ожидание обновления текста кнопки и получение нового текста
updated_button = wait.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, '#updatingButton'), 'SkyPro')
)

# Получение и вывод текста кнопки
button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(button_text)

# Закрытие браузера
driver.quit()
