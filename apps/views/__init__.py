# @Time : 2024/7/22 23:05
# @Author : luoxin
"""
因为首页可以说是所有模块共有的，所以可以将它放在模块包的__init__文件中
"""
from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index.html')
