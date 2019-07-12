__author__ = 'GitHub:Air-Zhuang'

from flask import render_template,jsonify,request,url_for,redirect
from flask_login import login_user, logout_user, current_user, login_required

from app.forms.auth import RegisterForm, LoginForm, PersonalCenterForm
from app.libs.helper import allowed_file
from app.models.goods import Goods
from app.view_models.user_view_model import UserViewModel
from . import web
from app.models.base import db
from app.models.user import User

import os


@web.route('/register', methods=['GET', 'POST'])
def register():
    resp_data = {'code': 200, 'msg': '注册成功~~', 'data': {}}
    form = RegisterForm(request.form)
    if request.method=='POST':
        if form.validate():
            with db.auto_commit():
                user=User()
                # nickname=user.nickname=request.values['nickname']
                email=user.email=request.values['email']
                user.password=request.values['password']
                db.session.add(user)
            # resp_data['data']['nickname']=nickname
            resp_data['data']['email'] = email
            return redirect(url_for('web.login'))   #跳转到login()视图函数
        else:
            resp_data['code'] = -1
            resp_data['msg'] = ','.join([v[0] for k,v in form.errors.items()])
            return render_template('register.html',register_data=resp_data)
    return render_template('register.html')

@web.route('/login', methods=['GET', 'POST'])
def login():
    resp_data = {'code': 200, 'msg': '登录成功~~', 'data': {}}
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')         #http://127.0.0.1:5000/login?next=/cart/0
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            resp_data['code']=-1
            resp_data['msg']='密码或账号错误~~'
            return render_template('login.html',login_data=resp_data)
    return render_template('login.html')

@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))

@web.route('/personal_center', methods=['GET', 'POST'])
@login_required
def personal_center():
    resp_data = {'code': 200, 'data': {}}
    addNav(resp_data)
    if request.method=='POST':

        try:
            img = request.files['user_img']
            end = img.filename.split('.')[1]
            path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/static/img/user"

            if allowed_file(img.filename):
                img.save(path+'/user_img'+str(current_user.id)+'.'+end)
                with db.auto_commit():
                    current_user.user_img='../static/img/user/user_img'+str(current_user.id)+'.'+end
                    db.session.add(current_user)
            else:
                resp_data['img_error'] = '上传图片格式不正确，支持png,jpg,gif,jpeg'
        except Exception as e:
            pass


        form = PersonalCenterForm(request.form)
        if form.validate():
            with db.auto_commit():
                current_user.nickname=request.values['nickname']
                current_user.phone_number=str(request.values['phone_number'])
                current_user.email=request.values['email']
                current_user.address=request.values['address']
                db.session.add(current_user)
            addNav(resp_data)
            resp_data['msg'] = "保存成功！"
            return render_template('personal_center.html', data=resp_data)
        else:
            resp_data['code'] = -1
            resp_data['msg'] = ','.join([v[0] for k,v in form.errors.items()])
            return render_template('personal_center.html',data=resp_data)
    return render_template('personal_center.html',data=resp_data)




def addNav(resp_data):
    if current_user.is_active:              #addUserInfo
        userviewmodel=UserViewModel(current_user)
        resp_data['user']=userviewmodel.data
    companys = Goods.getDistinctCompany()   #addCompanyList
    resp_data['companys'] = companys