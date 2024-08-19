# @Time : 2024/8/12 21:37
# @Author : luoxin
# @Time : 2024/7/31 21:37
# @Author : luoxin
from datetime import datetime

from exts import db


class User(db.Model):
    # 表名
    __tablename__ = 'tb_user'
    # 字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), unique=True, index=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(30),unique=True)
    rdatetime = db.Column(db.DateTime,default = datetime.now)
    is_delete = db.Column(db.Boolean,default=False)




