from unittest import TestCase

from main2 import Caesar


class TestCaesar(TestCase):
    def test_basic_data(self):
        self.assertEqual("def", Caesar.cipher("abc", 3))

    def test_wrapping(self):
        self.assertEqual("abc", Caesar.cipher("xyz", 3))

    def test_decrypting(self):
        self.assertEqual("abc", Caesar.cipher("def", -3))

    def test_key_greater_than_alphabet(self):
        self.assertEqual("def", Caesar.cipher("abc", 29))

    def test_space_in_text(self):
        self.assertEqual("cd ef", Caesar.cipher("ab cd", 2))
