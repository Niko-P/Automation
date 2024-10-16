from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# URL для теста
URL_3 = "https://www.saucedemo.com/"


def test_shop_form():
    # Инициализация драйвера
    chrome_service = ChromeService(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=chrome_service)

    # Открытие сайта
    chrome_browser.get(URL_3)

    # Логин
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    add_to_cart_buttons = [
        (By.ID, "add-to-cart-sauce-labs-backpack"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID, "add-to-cart-sauce-labs-onesie")
    ]

    for button in add_to_cart_buttons:
        chrome_browser.find_element(*button).click()

    # Переход в корзину и Checkout
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()

    # Заполнение формы
    chrome_browser.find_element(By.ID, "first-name").send_keys("Nikolai")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Poliakov")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("644033")
    chrome_browser.find_element(By.ID, "continue").click()

    # Проверка итоговой суммы
    total_price = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total_price == expected_total
    print(f"Итоговая сумма равна ${total_price}")

    # Закрытие браузера
    chrome_browser.quit()
