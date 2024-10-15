from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

# Установка явного ожидания
wait = WebDriverWait(driver, 40, 0.1)

# Переход на страницу
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
    )

# Ожидание, пока текст "Done!" не появится на странице
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))

# Ожидание загрузки всех изображений
wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'img')))

# Получение значения атрибута src у 3-й картинки
image_src = driver.find_elements(By.TAG_NAME, 'img')[2].get_attribute('src')

print(image_src)

# Закрытие браузера
driver.quit()
