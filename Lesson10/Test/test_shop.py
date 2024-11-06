import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page.Shop import InternetMagPage


@allure.title("Тест выбора товара и оплаты в интернет-магазине")
@allure.description(
    "Проверка процесса выбора товара, добавления в корзину и оплаты"
    )
@allure.feature("Интернет-магазин")
@allure.severity("blocker")
def test_form_internet_mag():
    # Шаг 1: Открытие веб-страницы Chrome
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )

    # Шаг 2: Создание экземпляра класса InternetMagPage
    with allure.step("Создание экземпляра класса InternetMagPage"):
        internet_mag_page = InternetMagPage(driver)

    # Шаг 3: Авторизация
    with allure.step("Авторизация пользователя"):
        internet_mag_page.authorization("standard_user", "secret_sauce")

    # Шаг 4: Добавление продуктов в корзину
    with allure.step("Добавление товаров в корзину"):
        to_be = internet_mag_page.add_products()

    # Шаг 5: Переход в корзину
    with allure.step("Переход в корзину интернет-магазина"):
        internet_mag_page.go_to_cart()

    # Шаг 6: Ввод персональных данных
    with allure.step("Ввод персональных данных пользователя"):
        internet_mag_page.personal_data("Nikolai", "P.", "644033")

    # Шаг 7: Получение итоговой стоимости
    with allure.step("Получение итоговой стоимости"):
        as_is = internet_mag_page.total_cost()

    # Проверка итоговой стоимости
    with allure.step("Проверка, что ожидаемая и фактическая стоимость равны"):
        assert as_is == to_be, (
            f"Expected total cost to be '{to_be}', but got '{as_is}'"
        )

    # Шаг 8: Закрытие интернет-магазина
    internet_mag_page.close()
