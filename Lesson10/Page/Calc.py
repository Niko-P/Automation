import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр webdriver.Chrome
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Установка задержки перед выполнением следующего шага")
    def delay(self, delay_value: str):
        """
        Устанавливает задержку для калькулятора.

        :param delay_value: значение задержки
        """
        input_delay = self._driver.find_element(
            By.CSS_SELECTOR, 'input[id="delay"]'
            )
        input_delay.clear()
        input_delay.send_keys(delay_value)

    @allure.step("Ввод чисел и выполнение операции сложения")
    def sum_of_the_numbers(self):
        """
        Выполняет операцию сложения 7 + 8.
        """
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"7")]').click()
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"+")]').click()
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"8")]').click()
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"=")]').click()

    @allure.step("Получение результата сложения")
    def get_result(self) -> str:
        """
        Получает результат сложения.

        :return: строка с результатом
        """
        WebDriverWait(self._driver, 48).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
            )
        )
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text

    @allure.step("Закрытие драйвера веб-браузера")
    def close_driver(self):
        """
        Закрывает драйвер веб-браузера.
        """
        self._driver.quit()
