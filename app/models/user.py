__author__ = 'GitHub:Air-Zhuang'

from sqlalchemy import Column
from sqlalchemy import Integer,String

from app.models.base import Base

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager


class User(UserMixin,Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24))                                   #昵称
    phone_number = Column(String(18))                               #电话号码
    _password=Column('password',String(128),nullable=False)         #密码
    email = Column(String(50), unique=True, nullable=False)         #邮箱
    address=Column(String(200))                                     #收货地址
    user_img=Column(String(100))                                    #头像

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)

    def check_password(self,raw):
        return check_password_hash(self._password,raw)

    @classmethod
    def getUserInfoById(cls, id):
        user = User.query.filter_by(id=id).first() \
            if User.query.filter_by(id=id).first() else []
        return user


    def get_id(self):   #flask_login需要在model层返回一个标志id的函数，函数名固定
        return self.id
@login_manager.user_loader   #使之后每次调用时候的current_user变成一个用户模型
def get_user(uid):
    return User.query.get(int(uid))    #主键查找不需要用filter_by