__author__ = 'GitHub:Air-Zhuang'

from sqlalchemy import Column, desc
from sqlalchemy import Integer,String,Numeric,distinct

from app.models.base import Base, db


class Order(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    uid=Column(Integer)                         #用户id
    order_no=Column(String(30))                 #订单号
    order_status=Column(Integer)                #订单状态 600待支付 601待发货 602待收货 603订单关闭
    order_address=Column(String(200))           #收货地址
    order_detail=Column(String(200))            #订单详情信息
    goods_imgs = Column(String(1000))            #商品封面图集合
    total_price = Column(Numeric(10, 2))        #总价

    @classmethod
    def getUserAllOrderList(cls, uid):      #获取当前用户所有订单信息
        userAllOrderList = Order.query.filter_by(uid=uid).all() \
            if Order.query.filter_by(uid=uid).all() else []
        return userAllOrderList

    @classmethod
    def deleteOrderById(cls, oid):          #删除选中的订单信息
        Order.query.filter_by(id=oid).delete()


