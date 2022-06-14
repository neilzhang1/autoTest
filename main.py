# @Time : 2022/6/8 0:09 
# encoding: utf-8
# @Author : Neil
# @File : main.py 
# @Software: PyCharm
import unittest
from common.HTMLTestRunnerNew import HTMLTestRunner
from BeautifulReport import BeautifulReport
from common.config_handler import get_config
import settings

#收集所有的测试用例
case = unittest.TestLoader().discover('./testcases', pattern='test_*.py')  #第一个参数是路径，第二个参数是匹配规则


#使用beautifulreport进行报告的输出
br = BeautifulReport(case)
# br.report('测试报告','testreport/testreport.html')
# config = get_config('config.yaml')
# br.report(**config['report'])
br.report(**settings.REPORT_CONFIG)
