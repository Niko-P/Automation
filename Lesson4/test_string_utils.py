from typing import Literal
import pytest
from string_utils import StringUtils
util = StringUtils()

"""capitalize"""


def test_capitilize():
    """POSITIVE"""
    assert util.capitilize("николай") == "Николай"
    assert util.capitilize("займись учёбой!") == "Займись учёбой!"
    assert util.capitilize("big") == "Big"
    """NEGATIVE"""
    assert util.capitilize("") == ""
    assert util.capitilize(" ") == " "
    assert util.capitilize("123456qwerty") == "123456qwerty"


"""trim"""


def test_trim():
    """POSITIVE"""
    assert util.trim(" где иои 17 лет?") == "где иои 17 лет?"
    assert util.trim("   город дорог   ") == "город дорог   "
    assert util.trim(" 123") == "123"
    """NEGATIVE"""
    assert util.trim("") == ""


@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert util.trim(123) == "123"


"""to_list"""


@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE:
    ("one,two,three", ",", ["one", "two", "three"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@/%/&/!/*", "/", ["@", "%", "&", "!", "*"]),
    # NEGATIVE:
    ("", None, []),
    ("1 2,3,4 5", None, ["1 2", "3", "4 5"]),
    ])
def test_to_list(string:
                 Literal['one,two,three'] |
                 Literal['1,2,3,4,5'] | Literal['@/%/&/!/*'] |
                 Literal[''] | Literal['1 2,3,4 5'], delimeter: None |
                 Literal[','] |
                 Literal['/'],
                 result: list[str]):
    if delimeter is None:
        res = util.to_list(string)
    else:
        res = util.to_list(string, delimeter)
    assert res == result


"""contains"""


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE:
    ("SkyPro", "y", True),
    ("test", "t", True),
    ("Ночь", "ь", True),
    ("Жили-были ", " ", True),
    ("123", "2", True),
    ("", "", True),
    # NEGATIVE:
    ("Стол", "c", False),
    ("Ракета", "P", False),
    ("X-mas!", "r", False),
    ("12345", "7", False),
    ("", "x", False),
])
def test_contains(string, symbol, result):
    res = util.contains(string, symbol)
    assert res == result


"""delete_symbol"""


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE:
    ("Кавардак", "а", "Кврдк"),
    ("Коля", "я", "Кол"),
    ("12345", "3", "1245"),
    ("New-York", "-", "NewYork"),
    ("Бесперспективный", "перспективный", "Бес"),
    # NEGATIVE:
    ("Йогурт", "ё", "Йогурт"),
    ("", "", ""),
    ("", "6", ""),
    ("yesterday", "", "yesterday"),
    ("Rock", "r", "Rock"),
    ("Malina", "а", "Malina")
])
def test_delete_symbol(string, symbol, result):
    res = util.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE:
    ("test", "t", True),
    ("", "", True),
    (" SkyPro", "", True),
    ("Лебедь  ", "Л", True),
    ("123", "1", True),
    # NEGATIVE:
    ("Ива", "и", False),
    ("frost", "F", False),
    ("", "g", False),
    ("winter", "в", False),
    ("Счастье", "Щ", False)
])
def test_starts_with(string, symbol, result):
    res = util.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE:
    ("Мысль", "ь", True),
    ("МММ", "М", True),
    ("", "", True),
    ("Пробел ", "", True),
    ("123", "3", True),
    ("Yes!", "!", True),
    ("Молодёжь", "ь", True),
    # NEGATIVE:
    ("one", "н", False),
    ("two", "u", False),
    ("Three", "I", False),
    ("", "%", False),
    ("Молодёжь", "ж", False)
])
def test_end_with(string, symbol, result):
    res = util.end_with(string, symbol)
    assert res == result


"""is_empty"""


@pytest.mark.parametrize('string, result', [
    # POSITIVE:
    ("", True),
    (" ", True),
    ("  ", True),
    # NEGATIVE:
    (".", False),
    (" space", False),
    ("empty", False),
    (" строка пустая ", False)
])
def test_is_empty(string, result):
    res = util.is_empty(string)
    assert res == result


"""list_to_string"""


@pytest.mark.parametrize('lst, joiner, result', [
    # POSITIVE:
    (["1", "2", "3"], ",", "1,2,3"),
    (["q", "w", "e", "r", "t", "y"], None, "q, w, e, r, t, y"),
    (["a", "b", "c"], "-", "a-b-c"),
    (["Бес", "перспективный"], "", "Бесперспективный"),
    (["P", "P"], "2", "P2P"),
    # NEGATIVE:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = util.list_to_string(lst)
    else:
        res = util.list_to_string(lst, joiner)
    assert res == result
