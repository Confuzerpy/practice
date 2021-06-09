import pytest
from yandex_testing_lesson import Rectangle


def test_normal_int_input():
    assert Rectangle(4, 10)


def test_normal_get_area():
    assert Rectangle(4, 10).get_area() == 40


def test_normal_get_perimeter():
    assert Rectangle(4, 10).get_perimeter() == 28


def test_error_type_input1():
    with pytest.raises(TypeError):
        Rectangle('a', 10)


def test_error_type_input2():
    with pytest.raises(TypeError):
        Rectangle(10, 'a')


def test_error_minus_int1():
    with pytest.raises(ValueError):
        Rectangle(-1, 20)


def test_error_minus_int2():
    with pytest.raises(ValueError):
        Rectangle(20, -1)
