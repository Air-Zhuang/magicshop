__author__ = 'GitHub:Air-Zhuang'

from flask import render_template,jsonify,request,url_for,redirect
from flask_login import login_user, logout_user, current_user, login_required

from app.forms.auth import RegisterForm, LoginForm, PersonalCenterForm
from app.libs.helper import allowed_file,geneGoodsImgName
from app.models.goods import Goods
from app.view_models.user_view_model import UserViewModel
from . import web
from app.models.base import db
from app.models.user import User

import os,decimal

@web.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    resp_data = {'code': 200, 'data': {}}
    addNav(resp_data)
    goods=Goods()
    if request.method=='POST':
        randomImgName=geneGoodsImgName()

        try:
            img = request.files['goods_img']
            end = img.filename.split('.')[1]
            path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/static/img/goods"

            if allowed_file(img.filename):
                with db.auto_commit():
                    goods.goods_img='../static/img/goods/'+randomImgName+'.'+end
                    goods.goods_name=request.values['goods_name']
                    goods.stock = int(request.values['stock'])
                    goods.price=decimal.Decimal(request.values['price'])
                    goods.goods_detail=request.values['goods_detail']
                    goods.cpu=request.values['cpu']
                    goods.ram=request.values['ram']
                    goods.memory=request.values['memory']
                    goods.video_card=request.values['video_card']
                    goods.size=request.values['size']
                    goods.cate_company=request.values['cate_company']
                    goods.cate_outlook=request.values['cate_outlook']
                    db.session.add(goods)
                    resp_data['msg'] = "保存成功！"
                img.save(path + '/' + randomImgName + '.' + end)
            else:
                resp_data['img_error'] = '上传图片格式不正确，支持png,jpg,gif,jpeg'
        except Exception as e:
            resp_data['msg'] = "保存失败，请检查是否有字段或图片空缺并检查字段格式！"

        if resp_data['msg'] == "保存失败，请检查是否有字段或图片空缺并检查字段格式！":       #如果填错了，将上次填的信息返回去，不用再一次输入
            last_fill={
                'goods_name':request.values['goods_name'],
                'stock':request.values['stock'],
                'price':request.values['price'],
                'goods_detail':request.values['goods_detail'],
                'cpu':request.values['cpu'],
                'ram':request.values['ram'],
                'memory':request.values['memory'],
                'video_card':request.values['video_card'],
                'size':request.values['size'],
                'cate_company':request.values['cate_company'],
                'cate_outlook':request.values['cate_outlook'],
            }
            resp_data['last_fill'] = last_fill
            return render_template('upload.html', data=resp_data)
    return render_template('upload.html',data=resp_data)




def addNav(resp_data):
    if current_user.is_active:              #addUserInfo
        userviewmodel=UserViewModel(current_user)
        resp_data['user']=userviewmodel.data
    companys = Goods.getDistinctCompany()   #addCompanyList
    resp_data['companys'] = companys