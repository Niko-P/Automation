import pytest
from selenium import webdriver
from Lesson7.Saucedemo.pages.login_page import LoginPage
from Lesson7.Saucedemo.pages.inventory_page import InventoryPage
from Lesson7.Saucedemo.pages.cart_page import CartPage
from Lesson7.Saucedemo.pages.checkout_page import CheckoutPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total_price(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # Логин
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("sauce-labs-onesie")

    # Переход в корзину и к оформлению заказа
    inventory_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # Заполнение данных и проверка стоимости
    checkout_page.fill_information("Nikolai", "Poliakov", "644033")
    total_price = checkout_page.get_total_price()

    # Проверка итоговой стоимости
    expected_total = "58.29"
    assert total_price == expected_total, (
        f"Expected total to be '{expected_total}', "
        f"but got '{total_price}'"
        )
