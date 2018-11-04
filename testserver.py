import os.path
import logging

import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import requests

from lxml import html
from tornado import web


def get_line_movements():
    all_games = []

    page = requests.get('https://www.thespread.com/mlb-baseball-public-betting-chart')
    tree = html.fromstring(page.content)

    logging.info(tree)

    for i in range(1, 30):
        date = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[1]')
        time = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[1]/text()[2]')
        open1 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[1]')
        open2 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[1]/text()[2]')
        current1 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[1]')
        current2 = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[4]/div[2]/text()[2]')
        away_id = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[1]')
        home_id = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/text()[2]')
        away_pitcher = tree.xpath(
            '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span/span[@id="v_pitcher"]/text()')
        away_team = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmv"]/text()')
        home_pitcher = tree.xpath(
            '//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span/span[@id="h_pitcher"]/text()')
        home_team = tree.xpath('//*[@id="pb"]/div/div[' + str(i) + ']/div[2]/div[2]/span[@id="tmh"]/text()')

        game_object = (''.join(date), ''.join(time), ''.join(open1), ''.join(current1), ''.join(away_id)[:3].rstrip(),
                       ''.join(away_pitcher), ''.join(away_team)[:3].rstrip(), ''.join(open2), ''.join(current2),
                       ''.join(home_id)[:3].rstrip(), ''.join(home_pitcher), ''.join(home_team)[:3].rstrip())

        logging.info(game_object)

        all_games.append(game_object)

    return all_games


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

    logging.info(public_bets)
    return public_bets


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/data/(?P<u>.*)$", RestHandler),
            (r'/js/(.*)', web.StaticFileHandler, {'path': './js'}),
            (r'/css/(.*)', web.StaticFileHandler, {'path': './css'}),
            (r'/images/(.*)', web.StaticFileHandler, {'path': './images'}),
            (r'/jquery/(.*)', web.StaticFileHandler, {'path': './min.css'}),
            (r'/bootstrap/(.*)', web.StaticFileHandler, {'path': './min.css'})
        ]

        #static_path = os.path.join(os.path.dirname(__file__), "..", "..", "static")
        static_path = os.path.join(os.path.dirname(__file__), "static")
        settings = dict(
            debug=True,
            static_path=static_path
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class RestHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def post(self, u):
        if self.request.method == 'POST':
        #similar print statement here
            print("Requested %s" % u)

    @tornado.gen.coroutine
    def get(self, u):
        if self.request.headers.get('Content-Type') != 'application/json':
            self.write("send requests here")
            return

        self.finish()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        linemovements = get_line_movements()
        self.render("templates/line_movement.html",
                    u='longcode', linemovements=linemovements)


def main():
    app = Application()
    print ("Listening on %s" % 8888)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
