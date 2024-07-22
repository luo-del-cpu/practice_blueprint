# @Time : 2024/7/22 23:05
# @Author : luoxin

"""
需要创建蓝图对象，才能在app上进行注册蓝图的操作
"""
from flask import Blueprint

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')


@blog_bp.route('/')
def blog_index():
    return '博客首页'
