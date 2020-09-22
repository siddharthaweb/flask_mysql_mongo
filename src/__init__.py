# -*- coding: utf-8 -*-
__version__ = '1.0'
from flask import Flask
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask('src')

# Get config
app.config.from_object('config')

#app.config['SECRET_KEY'] = 'random'
app.debug = True
#toolbar = DebugToolbarExtension(app)
from src.controllers import *
