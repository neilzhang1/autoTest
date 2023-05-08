import unittest
from ddt import ddt, data
from common.test_data_handler import get_test_data_from_excel
from common import logger
from calculate import cal
import settings

cases = get_test_data_from_excel(settings.TEST_DATA_CONFIG, 'cal')


@ddt
class testCal(unittest.TestCase):
    logger = logger

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('==========start==========')  # 在所有用例执行前执行一次

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.info('**********end**********')  # 打印结束日志

    @data(*cases)
    def test_cal(self, case):
        # 输出日志
        self.logger.info('用例{}开始测试'.format(case['title']))
        """测试calculate函数"""
        # 1.获取测试数据
        # 2.执行测试
        res = cal(case['a'], case['b'], case['c'])
        try:
            self.assertEqual(res, case['expect'])  # 断言
        except AssertionError as e:
            self.logger.exception('用例{}测试失败'.format(case['title']))  # 输出异常信息
            raise e  # 抛出异常
        else:
            self.logger.info('用例{}测试通过'.format(case['title']))  # 输出正常日志


if __name__ == '__main__':
    unittest.main()
