
"""Unit tests for simple_project.math_utils using unittest (stdlib)."""

import unittest

from simple_project.math_utils import add, multiply, mean


class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            mean([])


if __name__ == "__main__":
    unittest.main()
