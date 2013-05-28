import tornado.ioloop
import tornado.web
import tornado.httpserver
import routes.index
import os


class Application(tornado.web.Application):


	def __init__(self):
		handlers = [
		(r"/", routes.index.Index),
		(r"/favicon.ico", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'favicon.ico'}), 	
		#Statics
		(r"/statics/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'statics/')}),
		(r"/css/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'statics/css/')}),
		(r"/js/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'statics/js/')}),
		(r"/img/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'statics/img/')}),
        (r"/font/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'statics/font/')}),
        #Files
        (r"/files/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'files/')}),
        (r"/uploads/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'files/')}),


		]
	
		settings = dict(
			site_title="paulvalenzano.com", 
			debug=True,
			template_path=os.path.join(os.path.dirname(__file__), 'templates')
			)

		tornado.web.Application.__init__(self, handlers, **settings)



def main():
	report_app = Application()
	http_server = tornado.httpserver.HTTPServer(report_app)
	http_server.listen(80)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()

