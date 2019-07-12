__author__ = 'GitHub:Air-Zhuang'

from flask import render_template,jsonify,request
from flask_login import login_required,current_user

from app.view_models.goods_view_model import GoodsCollection
from app.view_models.user_view_model import UserViewModel
from . import web
from app.models.goods import Goods

from flask import current_app


@web.route('/')
def index():
    resp_data = {'code': 200, 'msg': '操作成功~~', 'page':{'from':1,'pagelist':[1],'cate':'index'}, 'data': {}}
    addNav(resp_data)
    addBanner(resp_data)
    goods = Goods()
    goodsList = goods.getAllGoodsLimitPerPage()

    canPage(resp_data,goods.getAllGoods,current_app.config['PER_PAGE'],index)               #能分多少页
    if len(request.args)>0:                                                 #处理分页
        goodsList=paging(resp_data, goods.getAllGoodsPaging,index)

    if goodsList==[]:
        resp_data['code'] = -1
        resp_data['msg']='取不到数据库的信息~'
    goodscollection=GoodsCollection(goodsList)
    resp_data['data']=goodscollection.data
    return render_template('index.html',data=resp_data)

@web.route('/goods/<outlook>')
def outlook(outlook):
    resp_data = {'code': 200, 'msg': '操作成功~~', 'page':{'from':1,'pagelist':[1],'cate':'outlook','cate_para':outlook}, 'data': {}}
    addNav(resp_data)
    addBanner(resp_data)
    goods = Goods()
    goodsList = goods.getGoodListByOutlookLimitPerPage(outlook)

    canPage(resp_data, goods.getGoodListByOutlook, current_app.config['PER_PAGE'], outlook)
    if len(request.args) > 0:
        goodsList = paging(resp_data, goods.getGoodListByOutlookPaging, outlook)

    if goodsList==[]:
        resp_data['code'] = -1
        resp_data['msg']='取不到数据库的信息~'
    goodscollection = GoodsCollection(goodsList)
    resp_data['data'] = goodscollection.data
    return render_template('index.html', data=resp_data)

@web.route('/company/<company>')
def company(company):
    resp_data = {'code': 200, 'msg': '操作成功~~','page':{'from':1,'pagelist':[1],'cate':'company','cate_para':company}, 'data': {}}
    addNav(resp_data)
    addBanner(resp_data)
    goods = Goods()
    goodsList = goods.getGoodListByCompanyLimitPerPage(company)

    canPage(resp_data, goods.getGoodListByCompany, current_app.config['PER_PAGE'], company)
    if len(request.args) > 0:
        goodsList = paging(resp_data, goods.getGoodListByCompanyPaging, company)

    if goodsList==[]:
        resp_data['code'] = -1
        resp_data['msg']='取不到数据库的信息~'
    goodscollection = GoodsCollection(goodsList)
    resp_data['data'] = goodscollection.data
    return render_template('index.html', data=resp_data)

@web.route('/goods/search')
def search():
    search_name=request.args['q']
    resp_data = {'code': 200, 'msg': '操作成功~~','page':{'from':1,'pagelist':[1],'cate':'search'}, 'data': {}}
    addNav(resp_data)
    addBanner(resp_data)
    goods = Goods()
    goodsList = goods.getGoodListByNameLimitPerPage(search_name)
    if goodsList == []:
        resp_data['code'] = -1
        resp_data['msg'] = '取不到数据库的信息~'
    goodscollection = GoodsCollection(goodsList)
    resp_data['data'] = goodscollection.data
    return render_template('index.html', data=resp_data)




def addNav(resp_data):
    if current_user.is_active:              #addUserInfo
        userviewmodel=UserViewModel(current_user)
        resp_data['user']=userviewmodel.data
    companys = Goods.getDistinctCompany()   #addCompanyList
    resp_data['companys'] = companys

def addBanner(resp_data):
    bannerList = Goods().getAllGoodsLimit3()
    if bannerList == []:
        return None
    bannerCollection = GoodsCollection(bannerList)
    resp_data['banner'] = bannerCollection.data

def canPage(resp_data,func_all,per_page,url):   #能分多少页
    pagenum = len(func_all(url)) // per_page
    pagelist = [i for i in range(1, pagenum + 2)]
    resp_data['page']['pagelist'] = pagelist

def paging(resp_data,func_paging,url):      #处理分页
    if request.args['paging'] == 'next_page':
        goodsList = func_paging(url,int(request.args['from']) + 1)
        resp_data['page']['from'] = int(request.args['from']) + 1
    elif request.args['paging'] == 'last_page':
        goodsList = func_paging(url,int(request.args['from']) - 1)
        resp_data['page']['from'] = int(request.args['from']) - 1
    else:
        goodsList = func_paging(url,int(request.args['paging']))
        resp_data['page']['from'] = int(request.args['paging'])
    return goodsList