from src.main import divide, calculate_logorifm, reverse_string
import pytest

def test_divide():

    assert divide(2, 1) == 2

    assert divide(2, 0) == 0

def test_calc_lig():
    assert calculate_logorifm(8, 2) == 3.0

    assert calculate_logorifm(8, 4) == 1.5

    with pytest.raises(ValueError):
         calculate_logorifm(0, 2)
    with pytest.raises(ValueError):
        calculate_logorifm(8, 0)


def test_reverse_string_numbers(numbers):
    assert reverse_string("123") == numbers


def test_reverse_string_letters(letters):
    assert reverse_string("hello") == letters