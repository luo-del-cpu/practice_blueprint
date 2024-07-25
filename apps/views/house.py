# @Time : 2024/7/22 23:05
# @Author : luoxin
from flask import Blueprint

# 使用url_prefix=''可以定义路由的前缀，用于区分不同的模块，同样，也可以在蓝图注册的时候加，二选一
house_bp = Blueprint('house', __name__, url_prefix='/house')


@house_bp.route('/',endpoint='index')
def house_index():
    return '房产首页'

@house_bp.route('/test',endpoint='test')
def house_test():
    return '房产测试'