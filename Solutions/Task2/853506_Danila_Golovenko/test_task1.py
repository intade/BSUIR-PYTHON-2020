import unittest
import task1

class TestSorting(unittest.TestCase):
    def __init__(self):
        task1.sorting('numbers.txt')

    def test_order(self):
        with open('sorted.txt') as f:
            a = int(f.readline())
            for num in f:
                b = int(num)
                self.assertTrue(a <= b)
                a = b

    def test_number(self):
        first_counter = 0
        second_counter = 0
        with open('numbers.txt') as f:
            for _ in f:
                first_counter += 1
        with open('sorted.txt') as f:
            for _ in f:
                second_counter += 1
        self.assertEqual(first_counter, second_counter)
 