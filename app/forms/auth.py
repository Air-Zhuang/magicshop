__author__ = 'GitHub:Air-Zhuang'

from wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length,NumberRange,DataRequired,Email,ValidationError,Regexp

from app.models.user import User

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),Email(message='电子邮箱为空或长度不在8-64之间')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空'), Length(6, 32)])
    # nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称为空或长度不在2-10之间')])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("电子邮件已被注册")

    # def validate_nickname(self, field):
    #     if User.query.filter_by(nickname=field.data).first():
    #         raise ValidationError('昵称已存在')

class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),Email(message='电子邮箱为空或长度不在8-64之间')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

class PersonalCenterForm(Form):
    # nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称为空或长度不在2-10之间')])
    # phone_number = StringField(validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱为空或长度不在8-64之间')])
    # address = StringField(validators=[DataRequired(), Length(min=10, max=70, message='地址还不到10个字吗？尽量写详细一些吧')])