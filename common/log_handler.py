# @Time : 2022/6/10 0:16 
# encoding: utf-8
# @Author : Neil
# @File : log_handler.py 
# @Software: PyCharm
"""
日志处理模块
"""
import logging


def get_logger(name, filename, fmt=None, debug=False):
    """
    获取日志对象
    :param name: 日志名称
    :param filename: 日志文件名
    :param fmt: 日志格式
    :param debug: 是否开启debug模式
    :return:
    """
    # 创建日志器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 日志器可以设置等级,文件处理器的等级一般要高于控制处理器的等级
    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.WARNING
    # 设置日志的默认格式
    if fmt is None:
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    file_handler = logging.FileHandler(filename=filename, encoding='utf-8')
    file_handler.setLevel(file_level)

    console_handler = logging.StreamHandler()  # 控制台处理器
    console_handler.setLevel(console_level)  # 设置控制台处理器的等级

    # 设置日志的格式
    formatter = logging.Formatter(fmt=fmt)
    file_handler.setFormatter(formatter)  # 设置文件处理器的格式
    console_handler.setFormatter(formatter)  # 设置控制台处理器的格式

    # 将日志处理器添加到日志器上
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
