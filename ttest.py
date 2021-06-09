import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_one(self):
        self.assertEqual(reverse('f'), 'f')

    def test_palindrome(self):
        self.assertEqual(reverse('аороа'), 'аороа')

    def test_normal_text(self):
        self.assertEqual(reverse('klm'), 'mlk')

    def test_wrong_type_int(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_list(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
