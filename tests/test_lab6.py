"""
Тести для перевірки математичних модулів.
"""
import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.basic_operations import add, divide
from src.advanced_operations import power, root, percentage

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_root(self):
        self.assertEqual(root(16, 2), 4.0)
        self.assertEqual(root(27, 3), 3.0)

    def test_percentage(self):
        self.assertEqual(percentage(200, 10), 20.0)

if __name__ == '__main__':
    unittest.main()