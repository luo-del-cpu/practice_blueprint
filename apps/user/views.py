# @Time : 2024/8/12 21:37
# @Author : luoxin
import hashlib

from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy import or_

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


# 用户注册
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


# 用户信息展示
@user_bp.route('/')
def content():
    # 查询数据库中的信息
    users = User.query.filter(User.is_delete == False).all()
    print(users)
    # return render_template('user/center.html',users=users)
    return render_template('user/content.html', users=users)


# 用户检索
@user_bp.route('/search')
def search():
    keyword = request.args.get('search')
    user_list = User.query.filter(or_(User.name.contains(keyword), User.email.contains(keyword))).all()
    return render_template('user/content.html', users=user_list)


# 用户删除
@user_bp.route('/delete', endpoint='delete')
def user_delete():
    # 1：逻辑删除
    # # 获取用户id
    # id = request.args.get('id')
    # # 获取该id的用户
    # user=User.query.get(id)
    # # 逻辑删除
    # user.is_delete = True
    # # 提交
    # db.session.commit()

    # 2：物理删除
    # 获取用户id
    id = request.args.get('id')
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.content'))


# 用户登录
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        inppassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # filter_by(条件)实际相当于sql的where语句
        user_list = User.query.filter_by(name=username)
        for u in user_list:
            if inppassword == u.password:
                return '用户登录成功！'
        else:
            return render_template('user/login.html', msg='用户名或密码有误！！！')
    else:
        return render_template('user/login.html')


# 用户信息更新
@user_bp.route('/update', endpoint='update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        # 取到html的数据
        username = request.form.get('username')
        email = request.form.get('email')
        userId = request.form.get('userId')
        # 取到数据库中对应的数据
        user = User.query.get(userId)
        # 改用户信息
        user.name = username
        user.email = email
        # 提交
        db.session.commit()
        return redirect(url_for('user.content'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)
