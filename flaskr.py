import sqlite 3
from flaskr import Flask, g, abort, flash, g

# Config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'password'
SECRET_KEY = 'development key'

# Create app
app = Flask(__name__)
app.config.from_object(__name__)