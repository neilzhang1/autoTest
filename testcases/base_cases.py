import json
import unittest
import jsonpath
from common import logger, db
import settings
from common.make_requests import send_http_request
from common.test_data_handler import generate_no_use_phone, replace_args_by_re


class BaseCase(unittest.TestCase):
    name = 'base用例'
    db = db
    logger = logger
    settings = settings

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('----------{}接口测试开始----------'.format(cls.name))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.info('**********{}接口测试结束**********'.format(cls.name))

    def checkout(self, case):
        self.case = case
        self.logger.info('用例【{}】开始测试'.format(case['title']))
        # 1.测试数据处理
        self.pre_test_data()
        # 2.测试步骤
        response = self.step()
        # 3.状态码断言
        self.assert_status_code()
        # 4.测试数据断言
        self.assert_json_response()
        # 5.数据库断言
        self.assert_db_true()
        # 6.测试数据提取
        self.extract_data()
        self.logger.info('用例【{}】测试结束'.format(case['title']))

    def pre_test_data(self):
        """
        预处理数据
        """
        self.logger.info('用例【{}】开始测试'.format(self.case['title']))
        # 1.测试数据处理
        # 1.1替换数据
        self.case['request'] = replace_args_by_re(self.case['request'], self)
        # 1.2替换sql
        if self.case.get('sql'):
            self.case['sql'] = replace_args_by_re(self.case['sql'], self)
        # 1.3判断是否需要生成手机号码
        if '#phone#' in self.case['request']:
            phone = generate_no_use_phone()
            self.case['request'] = self.case['request'].replace('#phone#', phone)
            if '#phone#' in self.case['sql']:
                self.case['sql'] = self.case['sql'].replace('#phone#', phone)
        # 1.4将json数据转换为python对象
        try:
            self.case['request'] = json.loads(self.case['request'])
            self.case['expect'] = json.loads(self.case['expect'])
        except Exception as e:
            self.logger.error('用例【{}】数据格式有误'.format(self.case['title']))
            self.logger.debug('request:{}'.format(self.case['request']))
            self.logger.debug('expect:{}'.format(self.case['expect']))
            raise ValueError('用例【{}】数据格式有误'.format(self.case['title']))
        # 1.5拼接url
        self.case['url'] = self.settings.PROJECT_HOST + self.settings.INTERFACES[self.case['url']]

    def step(self):
        """
        测试步骤
        """
        try:
            self.response = send_http_request(url=self.case['url'], method=self.case['method'], **self.case['request'])
        except Exception as e:
            self.logger.error('用例【{}】发送请求失败'.format(self.case['title']))
            self.logger.debug('请求参数是{}'.format(self.case['request']))
            self.logger.debug('请求地址是{}'.format(self.case['url']))
            self.logger.debug('请求方法是{}'.format(self.case['method']))
            self.logger.debug('请求头是{}'.format(self.case['headers']))
            raise e

    def assert_status_code(self):
        """
        断言状态码
        """
        try:
            self.assertEqual(self.response.status_code, self.case['status_code'])
        except AssertionError as e:
            self.logger.exception('用例【{}】状态码断言失败'.format(self.case['title']))
            self.logger.debug('实际结果是{}'.format(self.response.status_code))
            self.logger.debug('预期结果是{}'.format(self.case['status_code']))
            raise e
        else:
            self.logger.info('用例【{}】状态码断言成功'.format(self.case['title']))

    def assert_json_response(self):
        """
        断言响应数据
        """
        response_data = self.response.json()
        res = {'code': response_data['code'], 'msg': response_data['msg']}
        try:
            self.assertEqual(self.case['expect'], res)
        except AssertionError as e:
            self.logger.exception('用例【{}】响应数据断言失败'.format(self.case['title']))
            self.logger.debug('实际结果是{}'.format(res))
            self.logger.debug('预期结果是{}'.format(self.case['expect']))
            raise e
        else:
            self.logger.info('用例【{}】响应数据断言成功'.format(self.case['title']))

    def assert_db_true(self):
        """
        断言数据库
        """
        if self.case.get('sql'):
            try:
                db_res = self.db.exist(self.case['sql'])
                self.assertTrue(db_res)
            except Exception as e:
                self.logger.exception('用例【{}】数据库断言失败'.format(self.case['title']))
                self.logger.debug('sql语句是{}'.format(self.case['sql']))
                raise e
            else:
                self.logger.info('用例【{}】数据库断言成功'.format(self.case['title']))

    def extract_data(self):
        """
        提取响应中的数据并保存到用例类属性中
        """
        if self.case.get('extract'):
            for item in json.loads(self.case['extract']):
                name = item['name']
                exp = item['exp']
                res = jsonpath.jsonpath(self.response.json(), exp)
                if res:
                    setattr(self.__class__, name, res[0])
                else:
                    raise ValueError('用例【{}】提取表达式【{}】失败'.format(self.case['title'], exp))
