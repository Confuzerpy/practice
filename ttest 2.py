import pytest
from yandex_testing_lesson import reverse


def test_empty():
    assert reverse('') == ''


def test_one():
    assert reverse('f') == 'f'


def test_palindrome():
    assert reverse('аороа') == 'аороа'


def test_normal_text():
    assert reverse('klm') == 'mlk'


def test_wrong_type_int():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type_list():
    with pytest.raises(TypeError):
        reverse([1, 2, 3])
