#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 14:03
# @Author  : Neil
# @File    : test_recharge.py
# @Software: PyCharm
import json
import unittest

from ddt import ddt,data

import settings
from common import logger,db
from common.fixture import register,login
from common.test_data_handler import get_test_data_from_excel,generate_no_use_phone
from common.make_requests import send_http_request

cases = get_test_data_from_excel(settings.TEST_DATA_CONFIG,'recharge')

@ddt
class TestRecharge(unittest.TestCase):
    """
    测试充值接口
    """
    logger = logger
    db = db

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('----------充值接口测试开始----------')
        # 类级前置
        # 注册
        mobile_phone = settings.TEST_USER['mobile_phone']
        pwd = settings.TEST_USER['pwd']
        if not register(mobile_phone=mobile_phone,pwd=pwd):
            cls.logger.error('注册用户{}失败'.format(mobile_phone))
            raise ValueError('注册用户{}失败'.format(mobile_phone))
        cls.logger.info('注册用户{}成功'.format(mobile_phone))

        # 登录
        data = login(mobile_phone=mobile_phone,pwd=pwd)
        if data is None:
            cls.logger.error('登录用户{}失败'.format(mobile_phone))
            raise ValueError('登录用户{}失败'.format(mobile_phone))

        # 在用例间传递数据，将数据保存在类属性中
        cls.member_id = data['id']
        cls.token = data['token_info']['token']

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.info('**********充值接口测试结束**********')

    @data(*cases)
    def test_recharge(self,case):
        self.logger.info('用例【{}】开始测试'.format(case['title']))

        # 处理测试数据
        # 替换数据
        case['request'] = case['request'].replace('#member_id#',str(self.member_id))
        case['request'] = case['request'].replace('#token#',self.token)

        # 将字符串转换为json
        case['request'] = json.loads(case['request'])
        case['expect'] = json.loads(case['expect'])

        # 拼接url
        case['url'] = settings.PROJECT_HOST + settings.INTERFACES[case['url']]

        # 测试步骤
        self.logger.debug('url:{}'.format(case['url']))
        self.logger.debug('method:{}'.format(case['method']))
        self.logger.debug('request:{}'.format(case['request']))

        response = send_http_request(url=case['url'], method=case['method'], **case['request'])
        # 断言
        response_data = response.json()

        # 状态码断言
        try:
            self.assertEqual(200, response.status_code)
        except AssertionError as e:
            self.logger.exception('状态码断言失败')
            raise e

        # 请求结果断言
        res = {'code': response_data['code'], 'msg': response_data['msg']}
        try:
            self.assertEqual(case['expect'], res)
        except AssertionError as e:
            self.logger.exception('请求结果断言失败')
            self.logger.debug('期望数据:{}'.format(case['expect']))
            self.logger.debug('实际结果:{}'.format(res))
            self.logger.debug('响应结果:{}'.format(response_data))