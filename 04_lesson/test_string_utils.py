import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# Тесты для capitalize
def test_capitalize_positive(utils):
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"


def test_capitalize_empty(utils):
    assert utils.capitalize("") == ""


# Тесты для trim
def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello  ") == "hello  "


def test_trim_no_spaces(utils):
    assert utils.trim("skypro") == "skypro"


# Тесты для contains
def test_contains_positive(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "y") is True


def test_contains_negative(utils):
    assert utils.contains("SkyPro", "U") is False


# Тесты для delete_symbol
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found(utils):
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
