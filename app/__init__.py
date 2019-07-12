__author__ = 'GitHub:Air-Zhuang'

from flask import Flask
from flask_login import LoginManager
from app.models.base import db

login_manager=LoginManager()

def create_app():
    app=Flask(__name__)
    app.config.from_object('app.local-setting')
    app.config.from_object('app.secure-setting')
    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    db.init_app(app)
    # db.create_all(app=app)        #根据model创建表，已有表则不覆盖创建

    '''flask-admin'''
    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    from app.models import cart, goods, order, user

    admin = Admin(app=app, name='magicshop后台管理系统', template_mode='bootstrap3')
    admin.add_view(ModelView(user.User, db.session, name='用户管理'))
    admin.add_view(ModelView(goods.Goods, db.session, name='商品管理'))
    admin.add_view(ModelView(cart.Cart, db.session, name='购物车管理'))
    admin.add_view(ModelView(order.Order, db.session, name='订单管理'))

    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)