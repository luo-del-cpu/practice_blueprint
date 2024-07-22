# @Time : 2024/7/22 22:59
# @Author : luoxin
from apps import create_app

app = create_app()
if __name__ == '__main__':
    print(app.url_map)
    app.run()
