import pymysql

db_config = {
    'user':'root',
    'password':'Zwk3230972@',
    'host':'1.117.98.202',
    'port':3306,
    'database':'test',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor  #输出结果为字典
}


with pymysql.connect(**db_config) as conn:  #这么写可以自动关闭
    with conn.cursor() as cursor:
        sql = 'select sno from S order by age limit 10'
        cursor.execute(sql)
        r1 = cursor.fetchone()  #获取一条
        r2 = cursor.fetchmany(3)  #获取接下来的三条
        r3 = cursor.fetchall()  #获取剩下所有
        print(r1)
        print(r2)
        print(r3)