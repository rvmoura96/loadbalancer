from unittest import TestCase

from sum import my_sum


class TestMySum(TestCase):
    def test_my_sum_should_return_20_when_x_and_y_are_equal_10(self):
        expected = 20
        result = my_sum(10, 10)
        self.assertEqual(expected, result)

    def test_my_sum_should_return_30_when_x_and_y_are_equal_15(self):
        expected = 30
        result = my_sum(15, 15)
        self.assertEqual(expected, result)
