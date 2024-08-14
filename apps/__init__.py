# @Time : 2024/7/22 23:05
# @Author : luoxin
from flask import Flask

from apps.user.views import user_bp
from apps.views import index_bp
from apps.views.表操作_增删改查 import biao_bp
from exts import init_exts
from  settings import DevelopmentConfig
from apps.views.blog import blog_bp
from apps.views.ent import ent_bp
from apps.views.house import house_bp


def create_app():
    # 在创建app对象的时候，如果需要找模版目录会默认在自己的层级去找，因为templates和当前的app对象不在一个层级，所以需要重新定义
    app = Flask(__name__,template_folder='/Users/luoxin/workspace/practice_blueprint/templates',static_folder='/Users/luoxin/workspace/practice_blueprint/static')
    # 加载配置。通过导入settings文件中不同的类来控制环境变量
    app.config.from_object(DevelopmentConfig)
    # 初始化插件
    init_exts(app=app)
    # 注册蓝图，将不同模块中创建的蓝图对象注册到app上，这样app在启动的时候，就能和不同模块中的视图函数进行关联
    app.register_blueprint(index_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(house_bp)
    app.register_blueprint(ent_bp)
    app.register_blueprint(biao_bp)
    app.register_blueprint(user_bp)
    return app
