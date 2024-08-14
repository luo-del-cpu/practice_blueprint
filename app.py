# @Time : 2024/7/22 22:59
# @Author : luoxin
# from flask_script import Manager

from apps import create_app
from apps.models import teas
from apps.user.models import *
from apps.models.goods import *
app = create_app()

# 创建manager对象与app关联
# manager = Manager(app)


if __name__ == '__main__':
    print(app.url_map)
    app.run()
    # 通过flask-script脚本启动服务
    # manager.run()
