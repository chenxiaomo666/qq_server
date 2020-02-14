# coding:utf-8

from .user import User
from .. import db, app


def init_model():
    db.create_all(app=app)
