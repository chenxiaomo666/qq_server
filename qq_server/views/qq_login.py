# -*- coding:utf-8 -*-

from flask import Blueprint, request
from ..repositorys.props import auth, success, error, panic
from ..types.user_schema import InfoSchema
from ..models import User
from .. import db

login_view = Blueprint("login_view", __name__)


@login_view.route("/newlogin", methods=["GET"])
@panic()
def newLogin():

    result = None
    return success({
        "result": result
    })
    
