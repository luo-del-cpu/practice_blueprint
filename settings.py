# @Time : 2024/7/22 22:59
# @Author : luoxin

"""
将配置定义成不同的类
"""

class Config:
    DEBUG = False
    TESTING=False
    DATABASE_URI=''

class DevelopmentConfig(Config):
    DEBUG = True
    ENV='development'

class ProductionConfig(Config):
    DATABASE_URI = ''

class TestingConfig(Config):
    TESTING = True