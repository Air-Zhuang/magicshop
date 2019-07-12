__author__ = 'GitHub:Air-Zhuang'

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy,BaseQuery
from sqlalchemy import Column,Integer,SmallInteger,distinct
from contextlib import contextmanager

from datetime import datetime

class SQLAlchemy(_SQLAlchemy):
    @contextmanager         #事务
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Query(BaseQuery):     #软删除
    def filter_by(self, **kwargs):          #Cart.query.filter_by(uid=uid)  =>  Cart.query.filter_by(uid=uid,status=1)
        if 'status' not in kwargs.keys():
            kwargs['status']=1
        return super(Query,self).filter_by(**kwargs)
db=SQLAlchemy(query_class=Query)



class Base(db.Model):
    __abstract__=True                                       #不这么写SQLAlchemy会报找不到主键错误
    create_time=Column('create_time',Integer)
    status=Column(SmallInteger,default=1)

    def __init__(self):
        self.create_time=int(datetime.now().timestamp())

    # def set_attrs(self,attrs_dict):                     #web.register
    #     for key,value in attrs_dict.items():
    #         if hasattr(self,key) and key!='id':
    #             setattr(self,key,value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):       #删除方法
        self.status=0