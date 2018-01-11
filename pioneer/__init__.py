# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from flask_cors import *

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

CORS(app, supports_credentials=True)
db = SQLAlchemy(app)

auth = HTTPTokenAuth(scheme='Token')

import pioneer.models
import pioneer.views
