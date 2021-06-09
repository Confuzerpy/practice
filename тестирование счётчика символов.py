import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert count_chars('') == {}


def test_many_letters():
    assert count_chars('ddddddddd') == {'d': 9}


def test_count_chars():
    assert count_chars('mnnp') == {'m': 1,
                                   'n': 2,
                                   'p': 1}


def test_wrong_type_list():
    with pytest.raises(TypeError):
        count_chars(['g', 'd', 's'])


def test_wrong_type_int():
    with pytest.raises(TypeError):
        count_chars(42)
