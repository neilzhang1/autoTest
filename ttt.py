# @Time : 2022/6/10 0:00 
# encoding: utf-8
# @Author : Neil
# @File : ttt.py 
# @Software: PyCharm

import yaml
with open('config.yaml','r',encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config)