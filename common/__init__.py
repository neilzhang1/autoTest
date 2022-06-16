# @Time : 2022/6/10 23:52 
# encoding: utf-8
# @Author : Neil
# @File : __init__.py 
# @Software: PyCharm
import settings
from .log_handler import get_logger
from .config_handler import get_config
from .db_handler import DB


# config = get_config('config.yaml')
# logger = get_logger(name=config['log']['name'], filename=config['log']['filename'], debug=config['log']['debug'])  #获取日志器
# logger = get_logger(**config['log'])  #获取日志器
logger = get_logger(**settings.LOG_CONFIG)  #获取日志器
db = DB(settings.DB_CONFIG)