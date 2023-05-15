"""
贷款主流程测试
"""

from testcases.base_cases import BaseCase


class TestLoanFlow(BaseCase):
    name = "贷款主流程"

    # 1.注册
    def test_01register(self):
        case = {
            'title': '用户注册',
            'url': 'register',
            'method': 'post',
            'request': '{"headers": {"X-Lemonban-Media-Type": "lemonban.v1"},'
                       '"json": {"mobile_phone": "18888888888", "pwd": "12345678"}}',
            'status_code': 200,
            'expect': '{"code": 0, "msg": "OK"}'
        }
        self.checkout(case)

    # 2.登录
    def test_02login(self):
        case = {
            'title': '用户登录',
            'url': 'login',
            'method': 'post',
            'request': '{"headers": {"X-Lemonban-Media-Type": "lemonban.v2"},'
                       '"json": {"mobile_phone": "18888888888", "pwd": "12345678"}}',
            'status_code': 200,
            'expect': '{"code": 0, "msg": "OK"}'
        }
        self.checkout(case)
        # 测试成功需要将返回的Auth绑定到类属性中给下面的函数使用
        self.__class__.token = self.response.json()['data']['token_info']['token']
        self.__class__.member_id = self.response.json()['data']['id']


        # 3.充值

    def test_03recharge(self):
        case = {
            'title': '用户充值',
            'url': 'recharge',
            'method': 'post',
            'request': '{"headers": {"X-Lemonban-Media-Type": "lemonban.v2","Authorization":"Bearer #token#"},'
                       '"json": {"member_id":#member_id#,"amount":666}}',
            'status_code': 200,
            'expect': '{"code": 0, "msg": "OK"}'
        }
        self.checkout(case)



