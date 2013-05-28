import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
import tornado.httpclient as httpclient
#import logging
#import csv
#import urllib
#import datetime
#from storm.locals import *
#from storm.expr import Sum
from tornado.options import define, options


class Index(tornado.web.RequestHandler):


	def get(self):
		self.render("index.html")



		
