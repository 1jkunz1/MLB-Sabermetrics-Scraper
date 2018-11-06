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

from src.line_movement import get_line_movements


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
