from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Определяем значения для заполнения формы
first_name = "Иван"
last_name = "Петров"
address = "Ленина, 55-3"
email = "test@skypro.com"
phone_number = "+7985899998787"
zip_code = ""  # Оставляем пустым
city = "Москва"
country = "Россия"
job_position = "QA"
company = "SkyPro"
url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"


# Тестовая функция
def test_fill_form():
    # Запускаем браузер
    driver = webdriver.Chrome()

    # Переходим на страницу
    driver.get(url)

    # Заполняем форму с использованием явных ожиданий (WebDriverWait)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.NAME, "first-name"))).send_keys(first_name)
    driver.find_element(By.NAME, "last-name").send_keys(last_name)
    driver.find_element(By.NAME, "address").send_keys(address)
    driver.find_element(By.NAME, "e-mail").send_keys(email)
    driver.find_element(By.NAME, "phone").send_keys(phone_number)
    driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
    driver.find_element(By.NAME, "city").send_keys(city)
    driver.find_element(By.NAME, "country").send_keys(country)
    driver.find_element(By.NAME, "job-position").send_keys(job_position)
    driver.find_element(By.NAME, "company").send_keys(company)

    # Нажимаем кнопку Submit
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )
    submit_button.click()

    # Проверяем, что поля подсвечены правильно
    assert "danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "company").get_attribute("class")

      # Закрываем браузер
    driver.quit()
