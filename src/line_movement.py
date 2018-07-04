from lxml import html
import requests
from tabulate import tabulate


def get_line_movements():

    all_games = []
    
    page = requests.get('https://www.thespread.com/mlb-baseball-public-betting-chart')
    tree = html.fromstring(page.content)

    for i in range(1,10):

        date = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[1]/text()[1]')
        time = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[1]/text()[2]')
        open1 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[1]/text()[1]')
        current1 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[1]/text()[2]')
        open2 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[2]/text()[1]')
        current2 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[2]/text()[2]')
        away_pitcher = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span/span[@id="v_pitcher"]/text()')
        away_team = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span[@id="tmv"]/text()')
        home_pitcher = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span/span[@id="h_pitcher"]/text()')
        home_team = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span[@id="tmh"]/text()')

        game_object = (date, time, open1, current1, open2, current2, away_pitcher, away_team, home_pitcher, home_team)

        all_games.append(game_object)

    return all_games
