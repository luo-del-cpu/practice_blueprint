# @Time : 2024/8/12 21:37
# @Author : luoxin
import hashlib

from flask import Blueprint, request, render_template, redirect, url_for

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        if password == confirm_password:
            # 与模型结合，进行数据的添加
            # 1：找到模型创建对象
            user = User()
            # 2：给对象的属性赋值
            user.name = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.email = email
            # 添加
            # 3:将user对象添加到session中
            db.session.add(user)
            # 4：进行提交
            db.session.commit()
            return redirect(url_for('user.content'))
    return render_template('user/register.html')


@user_bp.route('/content')
def content():
    # 查询数据库中的信息
    users=User.query.all()
    print(users)
    #return render_template('user/center.html',users=users)
    return render_template('user/content.html',users=users)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        inppassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # filter_by(条件)实际相当于sql的where语句
        user_list = User.query.filter_by(name=username)
        for u in user_list:
            if inppassword==u.password:
                return '用户登录成功！'
        else:
            return render_template('user/login.html',msg='用户名或密码有误！！！')
    else:
        return render_template('user/login.html')
