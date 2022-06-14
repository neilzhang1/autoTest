# @Time : 2022/6/7 22:46 
# encoding: utf-8
# @Author : Neil
# @File : make_requests.py 
# @Software: PyCharm

"""
发送请求

1.根据用例中的请求方法发送http请求
2.能够动态接收请求参数
"""
import requests

def send_http_request(url,method,**kwargs):
    method = method.lower()
    return getattr(requests,method)(url=url,**kwargs)

if __name__ == '__main__':
    case = {
        'id': '1',
        'name': '注册成功-不带昵称和类型',
        'method': 'post',
        'url': 'http://api.lemonban.com/futureloan/member/register',
        'headers': {'X-Lemonban-Media-Type': 'lemonban.v2'},
        'data': {'mobile_phone': '18888888888', 'pwd': '123456'},
        'expect': {'code': '0', 'msg': 'OK'}
    }
    resp = send_http_request(url=case['url'],method=case['method'],json=case['data'])
    r_data = resp.json()
    print(r_data)
    if r_data['code'] == case['expect']['code'] and r_data['msg'] == case['expect']['msg']:
        print('pass')
    else:
        print('fail')