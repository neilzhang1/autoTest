#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 14:40
# @Author  : Neil
# @File    : report_handler.py
# @Software: PyCharm
import os
from datetime import datetime
from  BeautifulReport import BeautifulReport
from common.HTMLTestRunnerNew import HTMLTestRunner

def report(case, filename, report_dir, title=None, description=None,tester=None, _type='br'):
    """
    执行用例并生成报告
    ：param ts: 测试套件
    :param filename: 报告文件名称
    :param repotr_dir： 报告文件夹，仅支持beaitifulreport
    :param title： 报告主题，仅支持HTMLTesterRunner
    :param description： 报告描述
    :param tester：测试人员，仅支持HTMLTesterRunner
    :param _type：默认值为bs，表示生成beautifulreport格式的报告
    :return:
    """
    #生成时间前缀
    time_prefix = datetime.now().strftime('%Y%m%d%H%M%S')
    #拼接到报告文件名中
    filename = '{}_{}'.format(time_prefix,filename)
    if _type == 'br':
        br = BeautifulReport(case)
        br.report(description=description, filename=filename, report_dir=report_dir)
    else:
        with open(os.path.join(report_dir + '/' + filename), 'wb') as f:
            runner = HTMLTestRunner(f,title=title,description=description,tester=tester)
            runner.run(case)