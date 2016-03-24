import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        self.write("Welcome to the roundtable, %s!" % self.get_argument("person"))


app = tornado.web.Application([
    (r"/", MainHandler),
])


app.listen(8000)
tornado.ioloop.IOLoop.current().start()
