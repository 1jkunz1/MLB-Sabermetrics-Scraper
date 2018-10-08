import unittest
from services.lambdas.getLineMovement.line_movement import get_line_movements


class UnitTest(unittest.TestCase):

    def test_data(self):

        my_test_data = get_line_movements()
        self.assertTrue(type(my_test_data[0]) == tuple, True)
        self.assertTrue(type(my_test_data[0][0]) == str, True)
        self.assertTrue(len(my_test_data) < 15, True)
        self.assertTrue(len(my_test_data) > 1, True)


if __name__ == "__main__":
    unittest.main()