import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page.Dtypes import PersonalDataPage


@allure.title("Тест заполнения персональных данных")
@allure.description(
    "Проверка функциональности заполнения формы персональных данных"
    )
@allure.feature("Форма")
@allure.severity("blocker")
def test_form_elements():
    # Шаг 1: Открытие веб-страницы Chrome
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )

    # Шаг 2: Создание экземпляра класса PersonalDataPage
    with allure.step("Создание экземпляра класса PersonalDataPage"):
        personal_data_page = PersonalDataPage(driver)

    # Шаг 3: Заполнение формы с персональными данными
    with allure.step("Заполнение формы с персональными данными"):
        personal_data_page.personal_data(
            "Иван",
            "Петров",
            "Ленина, 55-3",
            "test@skypro.com",
            "+7985899998787",
            "Москва",
            "Россия",
            "QA",
            "SkyPro",
        )

    # Шаг 4: Проверка цвета поля ZIP-кода
    with allure.step("Проверка, что поле ZIP-кода имеет красный цвет"):
        zip_code_is_red = personal_data_page.zip_code_red()
        assert zip_code_is_red, "Поле ZIP-кода не имеет красный цвет"

    # Шаг 5: Проверка цвета остальных полей
    with allure.step("Проверка, что остальные поля имеют зеленый цвет"):
        fields_are_green = personal_data_page.other_fields_green()
        assert fields_are_green, "Не все поля имеют зеленый цвет"

    # Шаг 6: Закрытие драйвера веб-браузера
    personal_data_page.close_driver()
