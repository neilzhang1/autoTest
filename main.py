# @Time : 2022/6/8 0:09 
# encoding: utf-8
# @Author : Neil
# @File : main.py 
# @Software: PyCharm
import unittest

from common.config_handler import get_config
from common.report_handler import report
import settings

#收集所有的测试用例
case = unittest.TestLoader().discover('./testcases', pattern='test_*.py')  #第一个参数是路径，第二个参数是匹配规则


#进行报告的输出
report(case, **settings.REPORT_CONFIG)
