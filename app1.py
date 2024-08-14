# @Time : 2024/7/28 18:43
# @Author : luoxin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import settings

app = Flask(__name__)
app.config.from_object(settings.DevelopmentConfig)

# 创建sqlalchemy对象
db = SQLAlchemy(app)

# 创建model模型
class User(db.Model):
    # 属性
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(10),nullable=False)
    password = db.Column(db.String(10),nullable=False)
    phone = db.Column(db.String(11),nullable=False,unique=True)


    def __str__(self):
        return self.username

class Goods(db.Model):
    # 属性
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    gname = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Float,nullable=False)


if __name__ == '__main__':
    # 执行创建数据库表的操作
    with app.app_context():
        db.create_all()
    app.run()
