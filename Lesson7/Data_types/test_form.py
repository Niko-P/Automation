from .main_page import MainPage


def test_fill_form(chrome_browser):
    page = MainPage(chrome_browser)
    page.fill_form()
    page.submit()

    # Проверяем, что поля подсвечены правильно
    assert "danger" in page.get_field_class("zip-code")
    assert "success" in page.get_field_class("first-name")
    assert "success" in page.get_field_class("last-name")
    assert "success" in page.get_field_class("address")
    assert "success" in page.get_field_class("e-mail")
    assert "success" in page.get_field_class("phone")
    assert "success" in page.get_field_class("city")
    assert "success" in page.get_field_class("country")
    assert "success" in page.get_field_class("job-position")
    assert "success" in page.get_field_class("company")
