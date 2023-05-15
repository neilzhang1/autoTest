"""
贷款主流程测试--抽取数据
"""
from common.test_data_handler import get_test_data_from_excel
from ddt import ddt, data
from testcases.base_cases import BaseCase

cases = get_test_data_from_excel(BaseCase.settings.TEST_DATA_CONFIG, 'loan_info')


@ddt
class TestLoanInfo(BaseCase):
    name = "贷款主流程"

    @data(*cases)
    def test_loan_info(self, case):
        self.checkout(case)
