# @Time : 2024/7/31 21:37
# @Author : luoxin
from exts import db


class Goods(db.Model):
    # 表名
    __tablename__ = 'tb_goods'
    # 字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), unique=True, index=True)
    price = db.Column(db.Integer, default=1)
