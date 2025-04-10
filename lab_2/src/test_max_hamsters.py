import unittest
from main import max_hamsters

class TestMaxHamsters(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_hamsters(7, 3, [[1, 2], [2, 2], [3, 1]]), 2)
        self.assertEqual(max_hamsters(19, 5, [[5, 0], [2, 2], [1, 4], [5, 1], [4, 2]]), 3)
        self.assertEqual(max_hamsters(2, 2, [[1, 50000], [1, 60000]]), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
