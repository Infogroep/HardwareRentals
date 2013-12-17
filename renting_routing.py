#import bottle
from bottle import TEMPLATE_PATH, Bottle, hook, route, run, app, request, redirect, static_file
from bottle import jinja2_view as view, jinja2_template as template
from bottle import Jinja2Template
from bottle_flash import FlashPlugin

from beaker.middleware import SessionMiddleware

from cgi import escape
from os.path import join


from config import DevelopmentConfig

config = DevelopmentConfig()
TEMPLATE_PATH.append(config.TEMPLATE)
app = SessionMiddleware(app(), config.SESSIONS)
message_flash = FlashPlugin(key='messages', secret=config.SECRET_KEY)
Jinja2Template.defaults["get_flashed_messages"] = message_flash.get_flashed_messages
Jinja2Template.settings["extensions"] =  ["jinja2.ext.with_"]

@route("/")
def main_route():
	return "Hello world!"