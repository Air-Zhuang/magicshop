__author__ = 'GitHub:Air-Zhuang'

from flask import Blueprint
from flask import render_template

web=Blueprint('web',__name__)

@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

from app.web import main
from app.web import auth
from app.web import detail
from app.web import cart
from app.web import order
from app.web import upload
