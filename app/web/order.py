__author__ = 'GitHub:Air-Zhuang'

from flask import render_template, jsonify, request
from flask_login import login_required, current_user

from app.models.cart import Cart
from app.view_models.order_view_model import OrderCollection
from app.view_models.user_view_model import UserViewModel
from . import web
from app.models.base import db
from app.models.goods import Goods
from app.models.order import Order

from app.libs.helper import geneOrderNo


@web.route('/order/<order_from>')
@login_required
def order(order_from):
    resp_data = {'code': 200, 'msg': '查询成功~~', 'data': {}}
    addNav(resp_data)
    uid=current_user.id
    cart=Cart()
    order=Order()
    goods=Goods()

    if order_from=="list":
        pass
    elif order_from=="from_cart":
        with db.auto_commit():
            order.uid=uid
            order.order_no=geneOrderNo()
            order.order_status=600
            order.order_address=current_user.address if current_user.address else "不详"
            order.order_detail=cart.getUserCartTotalDetails(uid)
            order.goods_imgs=cart.getUserCartTotalImage(uid)
            order.total_price=cart.getUserCartTotalPrice(uid)
            db.session.add(order)
            cart.deleteUserAllCartList(uid)
    else:
        gid=order_from
        with db.auto_commit():
            order.uid=uid
            order.order_no=geneOrderNo()
            order.order_status=600
            order.order_address=current_user.address if current_user.address else "不详"
            order.order_detail=goods.getName(gid)
            order.goods_imgs=goods.getImage(gid)
            order.total_price=goods.getPrice(gid)
            db.session.add(order)

    userAllOrderList=order.getUserAllOrderList(uid)
    orderCollection=OrderCollection(userAllOrderList)
    resp_data['data']=orderCollection.data
    return render_template('order.html', data=resp_data)

@web.route('/delete_order/<oid>')
@login_required
def delete_order(oid):
    resp_data = {'code': 200, 'msg': '查询成功~~', 'data': {}}
    addNav(resp_data)
    uid=current_user.id
    order=Order()

    with db.auto_commit():
        order.deleteOrderById(oid)

    userAllOrderList = order.getUserAllOrderList(uid)
    orderCollection = OrderCollection(userAllOrderList)
    resp_data['data'] = orderCollection.data
    return render_template('order.html', data=resp_data)

def addNav(resp_data):
    if current_user.is_active:  # addUserInfo
        userviewmodel = UserViewModel(current_user)
        resp_data['user'] = userviewmodel.data
    companys = Goods.getDistinctCompany()  # addCompanyList
    resp_data['companys'] = companys
