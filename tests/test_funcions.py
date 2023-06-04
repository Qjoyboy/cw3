import pytest

from main import change_data
from main import hide_ciferki

def test_change_date():
    assert change_data("2019-08-26T10:50:58.294041") == "26.08.2019"

def test_hide_ciferki():
    assert hide_ciferki("Maestro 1596837868705199") == "Maestro 159683**5199"
    assert hide_ciferki("Счет 64686473678894779589") == "Счет **9589"
