# @Time : 2022/6/13 0:10 
# encoding: utf-8
# @Author : Neil
# @File : settings.py 
# @Software: PyCharm
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #获取项目根目录


# 日志配置
LOG_CONFIG= {
    'name': 'Abs测试报告',
    'filename': os.path.join(BASE_DIR, 'logs/abs.log'), #拼接绝对路径
    'debug': True
}

# 测试数据配置
TEST_DATA_CONFIG = os.path.join(BASE_DIR, 'testdata/absdata.xlsx')

# 测试报告配置
REPORT_CONFIG = {
    'description': 'Abs测试报告',
    'filename': 'testreport.html',
    'report_dir': os.path.join(BASE_DIR,'testreport'),
    '_type': 'br'
}

# 数据库配置
DB_CONFIG = {
    'user':'root',
    'password':'Zwk3230972@',
    'host':'1.117.98.202',
    'port':3306,
    'database':'test',
    'charset':'utf8',
    'autocommit':True  #自动提交事务，防止重复读
}

