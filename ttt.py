# @Time : 2022/6/10 0:00 
# encoding: utf-8
# @Author : Neil
# @File : ttt.py 
# @Software: PyCharm
import random
from faker import Faker

fk = Faker(locale='zh_CN') # 实例化，设置地区为中国

name = fk.name() # 生成姓名
id = fk.ssn() # 生成身份证
card = fk.credit_card_number() # 生成卡号
phone = fk.phone_number() # 生成手机号
mail = fk.email() # 生成邮箱



i = random.randint(1,100) # 生成1-100之间的随机整数，包含1和100

f = random.random() # 生成0-1之间的浮点数

j = random.randrange(1,100) # 生成1-100之间的随机整数，不包含100

ls = list('abcdefg')
s = random.choice(ls) # 从对象中随机挑选元素
