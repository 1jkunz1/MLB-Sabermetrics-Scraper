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


class NCAA(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.page = requests.get('https://www.thespread.com/ncaa-football-public-betting-chart')
        self.tree = html.fromstring(self.page.content)

    def create_game_object(self):

        for i in range(1, 30):
            self.date = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[1]')
            self.time = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[2]')
            self.open1 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[1]')
            self.open2 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[2]')
            self.current1 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[1]')
            self.current2 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[2]')
            self.away_id = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[1]')
            self.home_id = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[2]')
            self.away_team = self.tree.xpath(
                '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmv"]/text()')
            self.home_team = self.tree.xpath(
                '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmh"]/text()')

            game_object = (''.join(self.date),
                           ''.join(self.time),
                           ''.join(self.open1).rstrip(),
                           ''.join(self.current1).rstrip(),
                           ''.join(self.away_id)[:3].rstrip(),
                           ''.join(self.away_team)[:3].rstrip(),
                           ''.join(self.open2).rstrip(),
                           ''.join(self.current2).rstrip(),
                           ''.join(self.home_id)[:3].rstrip(),
                           ''.join(self.home_team)[:3].rstrip())

            self.all_games.append(game_object)

            self.all_games_clean = [x for x in self.all_games if x != ('', '', '', '', '', '', '', '', '', '', '', '')]

        return self.all_games_clean


class MLB(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.page = requests.get('https://www.thespread.com/mlb-baseball-public-betting-chart')
        self.tree = html.fromstring(self.page.content)
        self.away_pitcher = None
        self.home_pitcher = None

    def create_game_object(self):

        for i in range(1, 30):
            self.date = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[1]')
            self.time = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[2]')
            self.open1 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[1]')
            self.open2 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[2]')
            self.current1 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[1]')
            self.current2 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[2]')
            self.away_id = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[1]')
            self.home_id = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[2]')
            self.away_pitcher = self.tree.xpath(
                '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span/span[@id="v_pitcher"]/text()')
            self.away_team = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmv"]/text()')
            self.home_pitcher = tree.xpath(
                '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span/span[@id="h_pitcher"]/text()')
            self.home_team = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmh"]/text()')

            game_object = (''.join(self.date),
                           ''.join(self.time),
                           ''.join(self.open1),
                           ''.join(self.current1),
                           ''.join(self.away_id)[:3].rstrip(),
                           ''.join(self.away_pitcher),
                           ''.join(self.away_team)[:3].rstrip(),
                           ''.join(self.open2), ''.join(current2),
                           ''.join(self.home_id)[:3].rstrip(),
                           ''.join(self.home_pitcher),
                           ''.join(self.home_team)[:3].rstrip())

            self.all_games.append(game_object)

            self.all_games_clean = [x for x in all_games if x != ('', '', '', '', '', '', '', '', '', '', '', '')]

        return self.all_games_clean


class NFL(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.page = requests.get('https://www.thespread.com/nfl-football-public-betting-chart')
        self.tree = html.fromstring(self.page.content)

    def create_game_object(self):

        for i in range(1, 30):
            self.date = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[1]')
            self.time = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[2]')
            self.open1 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[1]')
            self.open2 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[2]')
            self.current1 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[1]')
            self.current2 = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[2]')
            self.away_id = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[1]')
            self.home_id = self.tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[2]')
            self.away_team = self.tree.xpath(
                '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmv"]/text()')
            self.home_team = self.tree.xpath(
                '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmh"]/text()')

            game_object = (''.join(self.date),
                           ''.join(self.time),
                           ''.join(self.open1).rstrip(),
                           ''.join(self.current1).rstrip(),
                           ''.join(self.away_id)[:3].rstrip(),
                           ''.join(self.away_team)[:3].rstrip(),
                           ''.join(self.open2).rstrip(),
                           ''.join(self.current2).rstrip(),
                           ''.join(self.home_id)[:3].rstrip(),
                           ''.join(self.home_team)[:3].rstrip())

            self.all_games.append(game_object)

            self.all_games_clean = [x for x in self.all_games if x != ('', '', '', '', '', '', '', '', '', '', '', '')]

        return self.all_games_clean
