#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 14:30
# @Author  : Neil
# @File    : t_log.py
# @Software: PyCharm
import logging

# 1.创建日志器
logger = logging.getLogger('auto')
#日志器可以设置等级
logger.setLevel(logging.DEBUG)
# 2.创建日志处理器
# 创建一个写到文件中的日志处理器
file_handler = logging.FileHandler(filename='auto.log',encoding='utf-8')
#可以单独设置日志处理器的日志等级
file_handler.setLevel(logging.WARNING)
# 创建一个控制台处理器将日志输出到控制台
console_handler = logging.StreamHandler()
# 3.创建格式化器
formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')
# 4.将格式化器添加到日志处理器
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 5.将日志处理器添加到日志器上
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug('debug')