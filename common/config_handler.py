# @Time : 2022/6/12 23:10 
# encoding: utf-8
# @Author : Neil
# @File : config_handler.py 
# @Software: PyCharm

from configparser import ConfigParser
import yaml
"""
获取配置文件
"""

def get_config(filename, encoding='utf-8'):
    # 1，获取文件后缀名
    suffix = filename.split('.')[-1]
    # 2，根据后缀名，获取文件类型
    if suffix in ['yaml', 'yml']:
        # 3，读取yaml文件
        with open(filename, 'r', encoding=encoding) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
       # 4.读取ini
    elif suffix in ['ini','cfg','cnf']:
        config = ConfigParser()
        config.read(filename,encoding=encoding)
        #将ini文件解析为字典
        data = {}
        for section in config.sections():
            data[section] = dict(config.items(section))
    else:
        raise Exception('文件类型不支持')
    return data

if __name__ == '__main__':
    r = get_config('../config.ini')
    print(r)
    l = get_config('../config.yaml')
    print(l)