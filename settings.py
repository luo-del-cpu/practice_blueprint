# @Time : 2024/7/22 22:59
# @Author : luoxin

"""
将配置定义成不同的类
"""

class Config:
    DEBUG = False
    TESTING=False
    # mysql+pymysql://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://hhpmmxobithcux:12345678@db4free.net:3306/study_tester'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV='development'

class ProductionConfig(Config):
    DATABASE_URI = ''

class TestingConfig(Config):
    TESTING = True