import unittest
from src.fangraphs_scraper.mlb_scraper import FangraphsScraper


# Tests for Sample YouTube Series
class UnitTest(unittest.TestCase):
    def setUp(self):
        self.fangraphs = FangraphsScraper()

    def test_scraper(self):
        self.assertIsInstance(self.fangraphs, FangraphsScraper)

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
