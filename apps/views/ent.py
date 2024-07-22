# @Time : 2024/7/22 23:06
# @Author : luoxin
from flask import Blueprint

ent_bp = Blueprint('ent', __name__, url_prefix='/ent')


@ent_bp.route('/')
def ent_index():
    return '娱乐首页'
