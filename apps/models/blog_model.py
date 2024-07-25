# @Time : 2024/7/25 20:49
# @Author : luoxin
from datetime import datetime
#import datetime


class Blog:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.datetime = datetime.now()
        self.click_num = 0


    def __str__(self):
        return self.title

    def add_click(self):
        self.click_num += 1
