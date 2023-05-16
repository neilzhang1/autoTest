# @Time : 2022/6/13 0:10 
# encoding: utf-8
# @Author : Neil
# @File : settings.py 
# @Software: PyCharm
import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获取项目根目录

# 项目域名
PROJECT_HOST = 'http://api.lemonban.com/futureloan'

# 接口路径
INTERFACES = {
    'register': '/member/register',
    'login': '/member/login',
    'recharge': '/member/recharge'
}

# 日志配置
LOG_CONFIG = {
    'name': 'Abs测试报告',
    'filename': os.path.join(BASE_DIR, 'logs/abs.log'),  # 拼接绝对路径
    'debug': True
}

# 测试数据配置
TEST_DATA_CONFIG = os.path.join(BASE_DIR, 'testdata/testcases.xlsx')

# 测试报告配置
REPORT_CONFIG = {
    'description': 'Abs测试报告',
    'filename': 'testreport.html',
    'report_dir': os.path.join(BASE_DIR, 'testreport'),
    '_type': 'br'
}

# 数据库配置
DB_CONFIG = {
    'user': 'root',
    'password': 'Zwk3230972@',
    'host': '43.143.80.154',
    'port': 3306,
    'database': 'test',
    'charset': 'utf8',
    'autocommit': True  # 自动提交事务，防止重复读
}

# 用户数据
TEST_USER = {
    'mobile_phone': '15601665487',
    'pwd': '12345678'
}

# 服务器公钥
SERVER_RSA_PUB_KEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
kKlZFc8Br7SHtbL2tQIDAQAB
-----END PUBLIC KEY-----
"""