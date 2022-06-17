# @Time : 2022/6/7 23:10 
# encoding: utf-8
# @Author : Neil
# @File : test_register.py 
# @Software: PyCharm
import unittest
import json
from ddt import ddt,data
from common.test_data_handler import get_test_data_from_excel,generate_no_use_phone
from common import logger
from common import db
from common.make_requests import send_http_request
import settings

cases = get_test_data_from_excel(settings.TEST_DATA_CONFIG, 'register')

@ddt
class TestRegister(unittest.TestCase):
    """
    测试注册接口
    """
    logger = logger
    db = db

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('----------注册接口测试开始----------')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.info('**********注册接口测试结束**********')

    @data(*cases)
    def test_register(self,case):
        self.logger.info('用例【{}】开始测试'.format(case['title']))

        #测试数据处理

        #判断是否需要生成手机号码
        if '#phone#' in case['request']:
            phone = generate_no_use_phone()
            case['request'] = case['request'].replace('#phone#',phone)
            if '#phone#' in case['sql']:
                case['sql'] = case['sql'].replace('#phone#', phone)

        #将json数据转换为python对象
        case['request'] = json.loads(case['request'])
        case['expect'] = json.loads(case['expect'])

        #拼接url
        case['url'] = settings.PROJECT_HOST + settings.INTERFACES[case['url']]

        #测试步骤
        self.logger.debug('url:{}'.format(case['url']))
        self.logger.debug('method:{}'.format(case['method']))
        self.logger.debug('request:{}'.format(case['request']))


        response = send_http_request(url=case['url'],method=case['method'],**case['request'])
        # 断言
        response_data = response.json()
        # 状态码断言
        try:
            self.assertEqual(200,response.status_code)
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




if __name__ == '__main__':
    print(cases[1]['request'])
