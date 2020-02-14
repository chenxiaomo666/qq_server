# -*- coding:utf-8 -*-

from flask import Blueprint, request
from ..repositorys.props import auth, success, error, panic
from ..types.user_schema import InfoSchema
from ..models import User
from .. import db

user_view = Blueprint("user_view", __name__)


@user_view.route("/info", methods=["GET"])
@panic(InfoSchema)
def fresh_info(args):
    user = User.query.filter_by(id=args.get("id")).first()
    if user:
        return success({
            "result": user.to_dict()
        })
    return error(reason="not found")
