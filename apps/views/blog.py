# @Time : 2024/7/22 23:05
# @Author : luoxin

"""
需要创建蓝图对象，才能在app上进行注册蓝图的操作
"""
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from apps.models.blog_model import Blog

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

blogs = []


# 首页
@blog_bp.route('/', endpoint='index')
def blog_index():
    # blog = Blog('创业者个人故事片要怎么策划拍摄?',
    #             '在当今这个充满机遇与挑战的时代，创业者们的故事总能引起人们的共鸣。他们或从零开始，历经艰辛，最终成就一番事业；或不断创新，引领行业潮流，成为行业...',
    #             '卢不斯导演')
    # blogs.append(blog)
    return render_template('blog/index.html', blogs=blogs)


# 添加操作
@blog_bp.route('add', endpoint='add', methods=['GET', 'POST'])
def blog_add():
    if request.method == 'POST':
        # 作为服务端来说，需要取post请求中的数据
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        print(f'标题:{title};作者:{author};内容:{content}')
        # 创建blog对象,注意此处创建对象时放入的顺序需要按照class定义时的顺序，否则可能会渲染错误
        blog = Blog(title, content, author)
        # 添加到blogs中
        blogs.append(blog)
        return redirect(url_for('blog.index'))
    return render_template('blog/add_blog_1.html')


# 删除操作
@blog_bp.route('/delete/<int:id>', endpoint='delete')
def blog_delete(id):
    value = blogs.pop(id)
    if value:
        return redirect(url_for('blog.index'))
