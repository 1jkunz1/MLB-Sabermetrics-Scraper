from lxml import html
import requests


def get_public():

    public_bets = []

    page = requests.get('https://www.thespread.com/mlb-baseball-public-betting-chart')
    tree = html.fromstring(page.content)

    for i in range(1, 11):
        team_id = tree.xpath('//*[@id="Mod11135"]/div/div/div[1]/div[' + str(i) + ']/span[2]/b/text()')
        team_name = tree.xpath('//*[@id="Mod11135"]/div/div/div[1]/div[' + str(i) + ']/span[3]/a/text()')
        public_percentage = tree.xpath('//*[@id="Mod11135"]/div/div/div[1]/div[' + str(i) + ']/span[4]/b/text()')

        public_object = (
        ''.join(team_id).strip(), ''.join(team_name).encode('ascii', 'ignore'), ''.join(public_percentage).strip())

        public_bets.append(public_object)

        return public_bets

