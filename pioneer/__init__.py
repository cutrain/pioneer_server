from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = 'Your session timeout, please login again'
login_manager.login_view = 'login'
login_manager.init_app(app)

import pioneer.views
