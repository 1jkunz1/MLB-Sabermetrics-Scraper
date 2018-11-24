from lxml import html
import requests


class Scraper(object):

    def __init__(self):
        self.all_games = []
        self.all_games_clean = []
        self.date = None
        self.time = None
        self.open1 = None
        self.open2 = None
        self.current1 = None
        self.current2 = None
        self.away_id = None
        self.home_id = None
        self.away_team = None
        self.home_team = None

class NCAAB(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.page = requests.get('http://www.vegasinsider.com/mlb/odds/las-vegas/')
        self.tree = html.fromstring(self.page.content)
        self.away_pitcher = None
        self.home_pitcher = None


# Go to 'thespread.com' and scrape data from the main NCAA page
class NCAAF(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.public_bets = []
        self.page = requests.get('http://www.vegasinsider.com/college-football/odds/las-vegas/')
        self.tree = html.fromstring(self.page.content)
        self.team = None
        self.percentage = None
        self.team_id = None


# Go to 'thespread.com' and scrape data from the main MLB page
class MLB(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.page = requests.get('http://www.vegasinsider.com/mlb/odds/las-vegas/')
        self.tree = html.fromstring(self.page.content)
        self.away_pitcher = None
        self.home_pitcher = None


# Go to 'thespread.com' and scrape data from the main NFL page
class NFL(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.page = requests.get('http://www.vegasinsider.com/nfl/odds/las-vegas/')
        self.tree = html.fromstring(self.page.content)

    def create_game_object(self):

        self.odds = self.tree.xpath('//a[contains(@href, "/nfl/odds/las-vegas/line-movement")]/text()')
        self.teams = self.tree.xpath('//a[contains(@href, "/nfl/teams/team-page.cfm/team")]/text()')

        return self.teams, self.odds
