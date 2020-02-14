# -*- coding:utf-8 -*-

from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

# config
app.config.from_object(Config)

# init ext
db.init_app(app)
from .models import init_model
init_model()

# app router
with app.app_context():
    from .views import user_view
    app.register_blueprint(user_view, url_prefix="/user")
