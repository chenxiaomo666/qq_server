# coding:utf-8

from .. import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    userName = db.Column("userName", db.String(64), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "userName": self.userName
        }
