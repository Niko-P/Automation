from .main_page import MainPage


def test_fill_form(chrome_browser):
    page = MainPage(chrome_browser)
    page.fill_form()
    page.submit()

    # Проверяем, что поле zip-code подсвечено красным
    assert "danger" in page.get_field_class("zip-code"), (
        "Поле zip-code должно быть подсвечено красным"
    )

    # Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field in fields_to_check:
        assert "success" in page.get_field_class(field), (
            f"Поле {field} должно быть подсвечено зеленым"
        )
