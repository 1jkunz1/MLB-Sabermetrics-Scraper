import unittest
from src.line_movement import get_line_movements

# Tests for Sample YouTube Series
class UnitTest(unittest.TestCase):

    def test_data(self):

        my_test_data = get_line_movements()
        self.assertTrue(True, type(my_test_data[0]) == tuple)
        self.assertTrue(True, type(my_test_data[0][0]) == str)
        self.assertTrue(False, len(my_test_data) <= 15)
        self.assertTrue(True, len(my_test_data) >= 1)


if __name__ == "__main__":
    unittest.main()
