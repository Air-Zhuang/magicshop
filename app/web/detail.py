__author__ = 'GitHub:Air-Zhuang'

from flask import render_template,jsonify,request
from flask_login import login_required,current_user

from app.view_models.goods_view_model import GoodsCollection, GoodsViewModel
from app.view_models.user_view_model import UserViewModel
from . import web
from app.models.base import db
from app.models.goods import Goods

@web.route('/detail/<gid>')
def detail(gid):
    resp_data = {'code': 200, 'msg': '查询成功~~', 'data': {}}
    addNav(resp_data)
    goods = Goods()
    goodDetail = goods.getGoodListById(gid)
    if goodDetail == []:
        resp_data['code'] = -1
        resp_data['msg'] = '取不到数据库的信息~'
    goodsviewmodel = GoodsViewModel(goodDetail)
    resp_data['data'] = goodsviewmodel.data
    return render_template('detail.html', data=resp_data)

def addNav(resp_data):
    if current_user.is_active:              #addUserInfo
        userviewmodel=UserViewModel(current_user)
        resp_data['user']=userviewmodel.data
    companys = Goods.getDistinctCompany()   #addCompanyList
    resp_data['companys'] = companys
