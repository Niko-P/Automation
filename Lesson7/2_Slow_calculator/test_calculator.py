# test_calculator.py
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_addition(browser):
    calculator_page = CalculatorPage(browser)

    # Установить задержку на 45 секунд
    calculator_page.set_delay(45)

    # Выполнить операцию 7 + 8 =
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    # Проверка результата
    result = calculator_page.get_result()
    assert result == "15", f"Expected result to be '15', but got '{result}'"
