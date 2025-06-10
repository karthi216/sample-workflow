import unittest
from main import add

class TestMain(unittest.TestCase):  # Fixed class name capitalization
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Used unittest methods for better debugging
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()