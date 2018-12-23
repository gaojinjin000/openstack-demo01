# coding: utf-8

from paste.deploy import loadapp
from  wsgiref.simple_server import make_server
import os

config = "python_paste.ini"
appname = "common"
wsgi_app = loadapp("config:%s" % os.path.abspath(config), appname)
server = make_server('localhost',80,wsgi_app)
server.serve_forever()