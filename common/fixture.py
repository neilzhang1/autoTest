#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 11:20
# @Author  : Neil
# @File    : fixture.py
# @Software: PyCharm
import requests

import settings
from common import logger


def register(mobile_phone, pwd, reg_name=None, _type=None):
    """
    注册用户
    """
    data = {
        'mobile_phone': mobile_phone,
        'pwd': pwd
    }
    if reg_name:
        data['reg_name'] = reg_name

    if _type is not None:
        data['type'] = _type

    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }

    url = settings.PROJECT_HOST + settings.INTERFACES['register']

    try:
        res = requests.post(url=url, json=data, headers=headers)
        if res.status_code == 200:
            logger.info('注册成功')
            return True
        return False
    except Exception as e:
        logger.exception('注册失败')
        raise e


def login(mobile_phone, pwd):
    """
    登录
    """
    data = {
        'mobile_phone': mobile_phone,
        'pwd': pwd
    }

    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }

    url = settings.PROJECT_HOST + settings.INTERFACES['login']

    try:
        res = requests.post(url=url, json=data, headers=headers)
        if res.status_code == 200:
            logger.info('登录成功')
            return res.json()['data']
    except Exception as e:
        logger.exception('登录失败')
        raise e


if __name__ == '__main__':
    phone = 15601665488
    register_res = register(mobile_phone=phone, pwd='12345678')
    if register_res:
        login_res = login(mobile_phone=phone, pwd='12345678')
        print(login_res)
    else:
        print('注册失败')
