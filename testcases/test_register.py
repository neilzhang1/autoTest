# @Time : 2022/6/7 23:10 
# encoding: utf-8
# @Author : Neil
# @File : test_register.py 
# @Software: PyCharm
from common.make_requests import send_http_request

case = {
    'id': '1',
    'name': '注册成功-不带昵称和类型',
    'method': 'post',
    'url': 'http://api.lemonban.com/futureloan/member/register',
    'headers': {'X-Lemonban-Media-Type': 'lemonban.v2'},
    'data': {'mobile_phone': '18888888888', 'pwd': '123456'},
    'expect': {'code': '0', 'msg': 'OK'}
}

try:
    res = send_http_request(url=case['url'],method=case['method'],json=case['data'])
    print(res)
except Exception as e:
    print(e)
    print('fail')
