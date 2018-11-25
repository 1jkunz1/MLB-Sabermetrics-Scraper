import unittest
from src.line_movement.line_movement import NCAAB, NCAAF, NFL, MLB, NBA


# Tests for Sample YouTube Series
class UnitTest(unittest.TestCase):
    def setUp(self):
        self.nfl = NFL()
        self.mlb = MLB()
        self.ncaab = NCAAB()
        self.ncaaf = NCAAF()
        self.nba = NBA()

    def test_nfl(self):

        game_object = self.nfl.create_game_object()
        self.assertIsInstance(self.nfl, NFL)
        self.assertTrue(True, type(game_object[0]) == tuple)
        self.assertTrue(True, type(game_object[0][0]) == str)
        self.assertTrue(True, len(game_object) <= 30)
        self.assertTrue(True, len(game_object) >= 1)

    def test_mlb(self):
        pass

    def test_ncaab(self):
        game_object = self.ncaab.create_game_object()
        self.assertIsInstance(self.ncaab, NCAAB)
        self.assertTrue(True, type(game_object[0]) == tuple)
        self.assertTrue(True, type(game_object[0][0]) == str)
        self.assertTrue(True, len(game_object) <= 200)
        self.assertTrue(True, len(game_object) >= 1)

    def test_ncaaf(self):
        pass

    def test_nba(self):
        pass


if __name__ == "__main__":
    unittest.main()