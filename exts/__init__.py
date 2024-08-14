# @Time : 2024/8/11 21:04
# @Author : luoxin
# 第三方插件管理

# 1:导入第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 2:初始化sqlalchemy、migrate对象
db = SQLAlchemy() # 用于数据库映射
migrate = Migrate() # 用与数据迁移

# 3:和app对象绑定
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
