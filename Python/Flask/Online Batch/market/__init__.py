from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # URI--> uniform resource identifier to identify the file as a database
db = SQLAlchemy(app)

from market import routes