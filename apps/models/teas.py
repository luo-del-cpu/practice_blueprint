# @Time : 2024/7/31 21:37
# @Author : luoxin

from exts import db


class User(db.Model):
    # 表名
    __tablename__ = 'tb_teas'
    # 字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), unique=True, index=True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    salary = db.Column(db.Float, default=1000, nullable=False)
    #salary2 = db.Column(db.Float, default=1000, nullable=False)



