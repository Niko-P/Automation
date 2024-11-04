import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page.Calc import CalculatorPage


@allure.title("Тест сложения чисел на калькуляторе")
@allure.description("Проверка функциональности сложения чисел на калькуляторе")
@allure.feature("Калькулятор")
@allure.severity("blocker")
def test_form_calculator():
    # Шаг 1: Открытие веб-страницы Chrome
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )

    # Шаг 2: Создание экземпляра класса CalculatorPage
    with allure.step("Создание экземпляра класса CalculatorPage"):
        calculator_page = CalculatorPage(driver)

    # Шаг 3: Установка задержки
    with allure.step("Установка задержки перед выполнением следующего шага"):
        calculator_page.delay('3')  # Устанавливаем задержку

    # Шаг 4: Выполнение операции сложения
    with allure.step("Ввод чисел и выполнение операции сложения"):
        calculator_page.sum_of_the_numbers()

    # Шаг 5: Получение результата сложения
    with allure.step("Получение результата сложения"):
        result = calculator_page.get_result()

    # Проверка результата
    with allure.step("Проверка, что результат равен '15'"):
        assert result == "15", (
            f"Expected result to be '15', but got '{result}'"
        )

    # Шаг 6: Закрытие драйвера веб-браузера
    calculator_page.close_driver()
