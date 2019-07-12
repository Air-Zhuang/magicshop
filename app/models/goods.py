__author__ = 'GitHub:Air-Zhuang'

from sqlalchemy import Column, desc
from sqlalchemy import Integer,String,Numeric,distinct

# from app import create_app
from flask import current_app

from app.models.base import Base, db


class Goods(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    goods_name=Column(String(30))                   #商品名
    goods_img=Column(String(100))                   #封面图
    stock=Column(Integer)                           #存货量
    price =Column(Numeric(10, 2))                   #售价
    goods_detail=Column(String(10000))              #商品详情
    cpu=Column(String(50))                          #cpu
    ram=Column(String(30))                          #内存
    memory=Column(String(30))                       #硬盘内存
    video_card=Column(String(50))                   #显卡
    size=Column(String(30))                         #尺寸
    cate_company=Column(String(20))                 #厂家
    cate_outlook = Column(String(20))               #外观(笔记本/平板/台式/...)

    # per_page=6
    # per_page=create_app().config['PER_PAGE']
    # per_page=current_app.config['PER_PAGE']


    @classmethod
    def getAllGoods(cls,index):       #首页全部商品    index占位，没作用
        goods=Goods.query.filter_by().order_by(desc(Goods.create_time)).all() \
            if Goods.query.filter_by().order_by(desc(Goods.create_time)).all() else []
        return goods

    @classmethod
    def getAllGoodsLimitPerPage(cls):  # 首页全部商品 显示per_page
        goods = Goods.query.filter_by().order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter_by().order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getAllGoodsPaging(cls,index,page):  # 首页全部商品 分页查询   index占位，没作用
        goods = Goods.query.filter_by().order_by(desc(Goods.create_time)).offset((int(page)-1)*current_app.config['PER_PAGE']).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter_by().order_by(desc(Goods.create_time)).offset((int(page)-1)*current_app.config['PER_PAGE']).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getAllGoodsLimit3(cls): #首页三张轮播图
        goods = Goods.query.filter_by().all()[:3] \
            if Goods.query.filter_by().all()[:3] else []
        return goods

    @classmethod
    def getGoodListByOutlook(cls,search):   #按种类分类所有商品
        goods=Goods.query.filter_by(cate_outlook=search).order_by(desc(Goods.create_time)).all() \
            if Goods.query.filter_by(cate_outlook=search).order_by(desc(Goods.create_time)).all() else []
        return goods

    @classmethod
    def getGoodListByOutlookLimitPerPage(cls, search):  # 按种类分类所有商品 显示per_page
        goods = Goods.query.filter_by(cate_outlook=search).order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter_by(cate_outlook=search).order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getGoodListByOutlookPaging(cls, search, page):  # 按种类分类所有商品 分页查询
        goods = Goods.query.filter_by(cate_outlook=search).order_by(desc(Goods.create_time)).offset((int(page)-1)*current_app.config['PER_PAGE']).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter_by(cate_outlook=search).order_by(desc(Goods.create_time)).offset((int(page)-1)*current_app.config['PER_PAGE']).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getGoodListByCompany(cls, search):  #按品牌分类所有商品
        goods = Goods.query.filter_by(cate_company=search).order_by(desc(Goods.create_time)).all() \
            if Goods.query.filter_by(cate_company=search).order_by(desc(Goods.create_time)).all() else []
        return goods

    @classmethod
    def getGoodListByCompanyLimitPerPage(cls, search):  # 按品牌分类所有商品 显示per_page
        goods = Goods.query.filter_by(cate_company=search).order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter_by(cate_company=search).order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getGoodListByCompanyPaging(cls, search,page):  # 按品牌分类所有商品
        goods = Goods.query.filter_by(cate_company=search).order_by(desc(Goods.create_time)).offset((int(page)-1)*current_app.config['PER_PAGE']).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter_by(cate_company=search).order_by(desc(Goods.create_time)).offset((int(page)-1)*current_app.config['PER_PAGE']).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getGoodListByName(cls, search):     #首页搜索框
        goods=Goods.query.filter(Goods.goods_name.ilike('%'+search+'%')).order_by(desc(Goods.create_time)).all() \
            if Goods.query.filter(Goods.goods_name.ilike('%'+search+'%')).order_by(desc(Goods.create_time)).all() else []
        return goods

    @classmethod
    def getGoodListByNameLimitPerPage(cls, search):     #首页搜索框  显示per_page
        goods = Goods.query.filter(Goods.goods_name.ilike('%' + search + '%')).order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() \
            if Goods.query.filter(Goods.goods_name.ilike('%' + search + '%')).order_by(desc(Goods.create_time)).limit(current_app.config['PER_PAGE']).all() else []
        return goods

    @classmethod
    def getGoodListById(cls, search):       #detail页商品信息
        good = Goods.query.filter_by(id=search).first() \
            if Goods.query.filter_by(id=search).first() else []
        return good

    @classmethod
    def getCartWantDict(cls, id):       #给cart用，创建购物车记录时需要的商品信息
        d={}
        good = Goods.query.filter_by(id=id).first() if Goods.query.filter_by(id=id).first() else None
        if good:
            d['id']=good.id
            d['goods_name']=good.goods_name
            d['goods_img']=good.goods_img
            d['price']=good.price
            d['cpu']=good.cpu
            d['ram']=good.ram
            d['memory']=good.memory
            d['video_card']=good.video_card
            d['size']=good.size
            d['cate_company']=good.cate_company
        return d

    @classmethod
    def getDistinctCompany(cls):       #首页品牌下拉框
        companys=db.session.query(Goods.cate_company).filter(Goods.status == 1).distinct().all() \
            if db.session.query(Goods.cate_company).filter(Goods.status == 1).distinct().all() else []
        if companys==[]:
            return []
        d = []
        for i in companys:
            d.append(i.cate_company)
        return d

    @classmethod
    def getName(cls,gid):  # 商品详情
        good = Goods.query.filter_by(id=gid).first()
        return good.goods_name

    @classmethod
    def getImage(cls, gid):  # 商品封面图
        good = Goods.query.filter_by(id=gid).first()
        return good.goods_img

    @classmethod
    def getPrice(cls, gid):  # 商品价格
        good = Goods.query.filter_by(id=gid).first()
        return good.price
