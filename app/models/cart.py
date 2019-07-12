__author__ = 'GitHub:Air-Zhuang'

from sqlalchemy import Column, desc
from sqlalchemy import Integer,String,Numeric,distinct

from app.models.base import Base, db


class Cart(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    uid=Column(Integer)                         #用户id
    gid=Column(Integer)                         #商品id
    num=Column(Integer)                         #数量
    goods_name = Column(String(30))
    goods_img = Column(String(100))
    price = Column(Numeric(10, 2))
    cpu = Column(String(50))
    ram = Column(String(30))
    memory = Column(String(30))
    video_card = Column(String(50))
    size = Column(String(30))
    cate_company = Column(String(20))
    total_price = Column(Numeric(10, 2))        #总价

    @classmethod
    def getUserAllCartList(cls, uid):           #获取当前用户所有购物车信息
        userAllCartList = Cart.query.filter_by(uid=uid).all() \
            if Cart.query.filter_by(uid=uid).all() else []
        return userAllCartList

    @classmethod
    def deleteUserAllCartList(cls, uid):        #删除当前用户所有购物车信息
        Cart.query.filter_by(uid=uid).delete()

    @classmethod
    def getNum(cls,uid,gid):                    #一条记录的数量
        cart =Cart.query.filter_by(uid=uid,gid=gid).first()
        if not cart:
            return 0
        num=cart.num
        return num

    @classmethod
    def getTotalPrice(cls, uid, gid):       #得到一条记录的总价
        target_cart_info = Cart.query.filter_by(uid=uid, gid=gid).first()
        total_price = target_cart_info.total_price
        return total_price

    @classmethod
    def getUserCartTotalPrice(cls, uid):    #得到用户购物车所有总价
        userAllCartList = Cart.query.filter_by(uid=uid).all()
        total_price = sum([i.total_price for i in userAllCartList])
        return total_price                  #decimal

    @classmethod
    def getUserCartTotalImage(cls, uid):    #得到用户购物车所有封面图列表
        userAllCartList = Cart.query.filter_by(uid=uid).all()
        total_images = ",".join([i.goods_img for i in userAllCartList])
        return total_images                 #str

    def getUserCartTotalDetails(cls, uid):    #得到用户购物车所有商品信息详情
        userAllCartList = Cart.query.filter_by(uid=uid).all()
        total_details = ",".join([i.goods_name+"x"+str(i.num) for i in userAllCartList])
        return total_details                 #str

