# coding: utf-8
from . import auth
from .authority import *
from .forum import *
from .util import *
from .models import Users

from flask import g


@auth.verify_token
def verify_token(token):
    user = Users.verify_token(token)
    if not user:
        return False
    g.user = user
    return True
