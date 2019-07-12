__author__ = 'GitHub:Air-Zhuang'

from flask import render_template, jsonify, request
from flask_login import login_required, current_user

from app.models.cart import Cart
from app.view_models.cart_view_model import CartCollection
from app.view_models.user_view_model import UserViewModel
from . import web
from app.models.base import db
from app.models.goods import Goods


@web.route('/cart/<gid>')
@login_required
def cart(gid):
    resp_data = {'code': 200, 'msg': '查询成功~~', 'data': {}}
    addNav(resp_data)
    uid = current_user.id
    cart = Cart()
    goods = Goods()

    if gid != '0':                                              # gid=0表示从nav跳转过来,不是0表示从详情页跳转过来,git>0表示添加一台,git<0表示减少一台
        abs_gid=abs(int(gid))
        num = cart.getNum(uid, abs_gid)
        goods_info = goods.getCartWantDict(abs_gid)
        if int(gid)>0:
            if num > 0:                                            # 如果存在数量加1，不存在变成1
                total_price = cart.getTotalPrice(uid=uid, gid=gid)  # 得到现在的总价
                with db.auto_commit():
                    cart.query.filter_by(uid=uid, gid=gid).update({'num': num + 1, 'total_price': total_price + goods_info['price']})
            elif num == 0:
                with db.auto_commit():
                    cart.gid = gid
                    cart.uid = uid
                    cart.num = 1
                    cart.goods_name = goods_info['goods_name']
                    cart.goods_img = goods_info['goods_img']
                    cart.price = goods_info['price']
                    cart.cpu = goods_info['cpu']
                    cart.ram = goods_info['ram']
                    cart.memory = goods_info['memory']
                    cart.video_card = goods_info['video_card']
                    cart.size = goods_info['size']
                    cart.cate_company = goods_info['cate_company']
                    cart.total_price = goods_info['price']
                    db.session.add(cart)
        elif int(gid)<0:
            total_price = cart.getTotalPrice(uid=uid, gid=abs_gid)
            with db.auto_commit():
                cart.query.filter_by(uid=uid, gid=abs_gid).update({'num': num - 1, 'total_price': total_price - goods_info['price']})

    userAllCartList = cart.getUserAllCartList(uid)
    cartCollection = CartCollection(userAllCartList)
    resp_data['data'] = cartCollection.data
    return render_template('cart.html', data=resp_data)

@web.route('/cart_delete/<gid>')
@login_required
def cart_delete(gid):
    resp_data = {'code': 200, 'msg': '查询成功~~', 'data': {}}
    addNav(resp_data)
    uid = current_user.id
    cart = Cart()

    if gid=="delete_all":
        with db.auto_commit():
            cart.query.filter_by(uid=uid).delete()
    else:
        with db.auto_commit():
            cart.query.filter_by(uid=uid, gid=gid).delete()

    userAllCartList=cart.getUserAllCartList(uid)
    cartCollection=CartCollection(userAllCartList)
    resp_data['data']=cartCollection.data
    return render_template('cart.html', data=resp_data)


def addNav(resp_data):
    if current_user.is_active:  # addUserInfo
        userviewmodel = UserViewModel(current_user)
        resp_data['user'] = userviewmodel.data
    companys = Goods.getDistinctCompany()  # addCompanyList
    resp_data['companys'] = companys
