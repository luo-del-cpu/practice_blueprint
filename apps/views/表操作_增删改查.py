# @Time : 2024/8/5 21:15
# @Author : luoxin
from flask import Blueprint
from sqlalchemy import or_
from sqlalchemy.testing import in_

from apps.user.models import User
from exts import db
from apps.user import *

biao_bp = Blueprint('biao', __name__, url_prefix='/biao')


# 增加数据
@biao_bp.route('/biaoadd', endpoint='biaoadd')
def biao_add():
    # 单表操作
    # 添加一条数据
    # u = User()
    # u.name='luoxin'
    # u.age=24
    # u.sex=False
    # u.salary=2000
    # db.session.add(u)
    # db.session.commit()
    # return 'success'

    # 添加多条数据
    users = []
    for i in range(10, 20):
        u = User()
        u.name = 'luoxin' + str(i)
        u.age = i
        u.salary = i + 1000
        users.append(u)
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return 'ADD Fail:' + str(e)
    return 'ADD Success!'


# 删除数据，找到要删的数据，删除
@biao_bp.route('/biaodelete', endpoint='biaodelete')
def biao_delete():
    u = User.query.first()  # 查询第一条数据
    db.session.delete(u)
    db.session.commit()
    return 'Delete Success'


# 修改数据，找到要修改的数据，修改
@biao_bp.route('/biaoupdate', endpoint='biaoupadte')
def biao_update():
    u = User.query.first()
    u.name = 'test'
    db.session.commit()
    return 'Update Success'


# 查询数据
@biao_bp.route('/biaoget', endpoint='biaoget')
def biao_get():
    u = User.query.all()
    # 此处u实际返回的就是一个列表里查询出来的所有对象数据，是一个list类型
    print(u, type(u))
    # 此处User.query实际就是一个sql查询语句，是一个自定义类型： <class 'flask_sqlalchemy.query.Query'>
    print(User.query, type(User.query))
    return 'Get Success'


@biao_bp.route('/biaoget1', endpoint='biaoget1')
def biao_get1():
    # filter()过滤:类似于数据库的where等值操作,如果是等值，必须是两个==，且带模型类名
    # u=User.query.filter(User.age==13)

    # 也可以模糊查询，以l开头(startswith())；或以l结尾(endswith());或包含(contains)
    # u=User.query.filter(User.name.startswith('l')).all()
    # u=User.query.filter(User.name.endswith('l')).all()
    # u=User.query.filter(User.name.contains('l')).all()

    # 也可以使用like模糊查询，需要带%
    # u=User.query.filter(User.name.like('l%')).all()

    # 也可以使用>(__gt__())或<(__lt__())查询,一般用于日期或者整型
    # u=User.query.filter(User.age > 12).all()
    # u=User.query.filter(User.age.__gt__(12)).all()

    # 也可以使用or_ 或 and_ 或not_ 多条件查询
    # u = User.query.filter(or_(User.name.startswith('l'), User.name.endswith('l'))).all()
    # 查询不包含i的对象
    # u=User.query.filter(not_(User.name.contains('l'))).all()

    # 也可以使用in_ 查询多个符合的字符串
    # u = User.query.filter(in_([xxx'','xxx'])).all()

    # 也可以使用order_by() 进行排序，默认升序；使用desc()降序
    #u = User.query.filter(User.name.in_(['test4','test5'])).order_by('name').all()
    #u = User.query.order_by(User.name.desc()).all()

    # limit限制取的数量
    # 取前两条
    # u = User.query.limit(2).all()
    # 跳过两条，在取两条
    u = User.query.offset(2).limit(2).all()

    # filter_by()过滤:类似于数据库的where等值操作，不用两个==
    # u=User.query.filter_by(age=13)

    # 此处u实际返回的就是一个查询集
    print(u, '--->', type(u))
    # 可以进行强转来查看内容
    print(list(u))
    return 'Get Success'


@biao_bp.route('/biaoget2', endpoint='biaoget2')
def biao_get2():
    # 需要传入一个主键值
    u = User.query.get(8)
    # 此处u实际返回的就是一个对象<class 'apps.models.user.User'>
    print(u, type(u))
    # 可以通过u.name,u.age的方式取值
    print(u.name, u.age)
    return 'Get Success'
