import os.path

import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web

from tornado import web

from src.line_movement.line_movement import NFL, NCAAB, MLB
from src.reddit_scraper.reddit_scraper import *
from machine.machine_learning_sample import MachineLearningExamples


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/reddit", RedditHandler),
            (r"/sabermetrics", SaberHandler),
            (r"/machinelearning", MLHandler),
            (r"/mlb", MLBHandler),
            (r"/twitter", TwitterHandler),
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
        nfl_slate = NFL()
        linemovements = nfl_slate.create_game_object()
        self.render("templates/line_movement.html",
                    u='longcode', linemovements=linemovements)


class RedditHandler(tornado.web.RequestHandler):
    def get(self):
        reddit = RedditScraper()
        comments = reddit.make_comment_list(thread_id='a1dmz7')
        self.render("templates/reddit_data.html",
                    u='longcode', comments=comments)


class TwitterHandler(tornado.web.RequestHandler):
    def get(self):
        reddit = RedditScraper()
        comments = reddit.make_comment_list(thread_id='a1dmz7')
        self.render("templates/reddit_data.html",
                    u='longcode', comments=comments)


class SaberHandler(tornado.web.RequestHandler):
    def get(self):
        reddit = RedditScraper()
        comments = reddit.make_comment_list(thread_id='a1dmz7')
        self.render("templates/reddit_data.html",
                    u='longcode', comments=comments)


class MLHandler(tornado.web.RequestHandler):
    def get(self):
        machine = MachineLearningExamples()
        machine_data = machine.linear_regression()
        self.render("templates/machine_learning.html",
                    u='longcode', machine_data=machine_data)


class MLBHandler(tornado.web.RequestHandler):
    def get(self):
        machine = MachineLearningExamples()
        machine_data = machine.linear_regression()
        self.render("templates/mlb.html",
                    u='longcode', machine_data=machine_data)


def main():
    app = Application()
    print("Listening on %s" % 8888)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
