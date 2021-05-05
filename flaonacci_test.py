import unittest
from flatonacci import flatonacci

class TestFlatonacci(unittest.TestCase):

    def test_flatonacci(self):
        self.assertEqual(flatonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        self.assertEqual(flatonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
        self.assertEqual(flatonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
        self.assertEqual(flatonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
        self.assertEqual(flatonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(flatonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
        self.assertEqual(flatonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
        self.assertEqual(flatonacci([1, 1, 1], 1), [1])

if __name__ == '__main__':
    unittest.main()