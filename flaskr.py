import sqlite3
from flask import Flask, g, abort, flash, g 
from contextlib import closing

# Config
DATABASE = 'tmp/flaskr.db'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'password'
SECRET_KEY = 'development key'

# Create app
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

if __name__ == '__main__':
	app.run()