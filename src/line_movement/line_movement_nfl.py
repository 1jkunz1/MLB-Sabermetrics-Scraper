from lxml import html
import requests


def get_line_movements_nfl():
    all_games = []

    page = requests.get('https://www.thespread.com/nfl-football-public-betting-chart')
    tree = html.fromstring(page.content)

    for i in range(1, 30):
        date = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[1]')
        time = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[2]')
        open1 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[1]')
        open2 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[2]')
        current1 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[1]')
        current2 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[2]')
        away_id = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[1]')
        home_id = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[2]')
        away_team = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmv"]/text()')
        home_team = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmh"]/text()')

        game_object = (''.join(date), ''.join(time), ''.join(open1).rstrip(), ''.join(current1).rstrip(), ''.join(away_id)[:3].rstrip(),
                       ''.join(away_team)[:3].rstrip(), ''.join(open2).rstrip(), ''.join(current2).rstrip(),
                       ''.join(home_id)[:3].rstrip(), ''.join(home_team)[:3].rstrip())

        all_games.append(game_object)

        all_games_clean = [x for x in all_games if x != ('', '', '', '', '', '', '', '', '', '', '', '')]

    return all_games_clean
