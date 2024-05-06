from django.test import TestCase

from .commons import fibonacci


class FibonacciTestCase(TestCase):
    def test_fibonacci_positive_numbers(self):
        produced_numbers = 5
        result = fibonacci(produced_numbers)
        expected_result = [0, 1, 1, 2, 3, 5, 8]
        self.assertEqual(result, expected_result)

    def test_fibonacci_negative_numbers(self):
        produced_numbers = -5
        result = fibonacci(produced_numbers)
        expected_result = [0]
        self.assertEqual(result, expected_result)
