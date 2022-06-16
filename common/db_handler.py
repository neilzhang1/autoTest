#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 16:36
# @Author  : Neil
# @File    : db_handler.py
# @Software: PyCharm
import pymysql

class DB:

    def __init__(self,db_config):
        #创建连接
        self.conn = pymysql.connect(**db_config)

    def __del__(self):
        #自动关闭连接
        self.conn.close()

    def get_one(self,sql):
        """
        获取一条数据
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()

    def get_many(self,sql,size):
        """
        获取多条数据
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchmany(size)

    def get_all(self,sql):
        """
        获取所有数据
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def exist(self,sql):
        """
        是否存在数据
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            if cursor.fetchone():
                return True
            else:
                return False

if __name__ == '__main__':
    import settings
    db = DB(settings.DB_CONFIG)  #实例化一个数据库连接
    sql = 'select sname from S order by age'
    r = db.exist(sql)
    print(r)