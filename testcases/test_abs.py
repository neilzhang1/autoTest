# @Time : 2022/6/7 23:42 
# encoding: utf-8
# @Author : Neil
# @File : test_abs.py 
# @Software: PyCharm
import unittest
from ddt import ddt,data
from common.test_data_handler import get_test_data_from_excel
from common import logger
from common import db

import settings

cases = get_test_data_from_excel(settings.TEST_DATA_CONFIG, 'Sheet1')

@ddt
class TestAbs(unittest.TestCase):
    logger = logger  #获取日志器
    db = db

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('==========start==========')  # 在所有用例执行前执行一次

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.info('**********end**********')  # 打印结束日志

    @data(*cases)
    def test_abs(self,case):
        #输出日志
        self.logger.info('用例{}开始测试'.format(case['title']))
        """测试abs函数"""
        #1.获取测试数据
        #2.执行测试
        res = abs(case['data'])
        #3.断言
        # self.assertEqual(res, case['expect'], msg='测试失败')
        try:
            self.assertEqual(res, case['expect'])  #断言
        except AssertionError as e:
            self.logger.exception('用例{}测试失败'.format(case['title']))  #输出异常信息
            raise e #抛出异常
        else:
            self.logger.info('用例{}测试通过'.format(case['title']))  #输出日志


        if case['sql']:
            try:
                db_res = self.db.exist(case['sql'])
                self.assertTrue(db_res)
            except Exception as e:
                self.logger.exception('数据库断言失败')
                self.logger.debug('执行的SQL是{}'.format(case['sql']))
                raise e
            else:
                self.logger.info('数据库断言成功')



#执行脚本中所有test开头的用例
if __name__ == '__main__':
    unittest.main()