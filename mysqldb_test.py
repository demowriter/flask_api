# -*- coding:utf-8 -*-
# mysqldb介绍：https://blog.csdn.net/tototuzuoquan/article/details/75263772
# import pymysql
from flask import Flask, request, send_file
import MySQLdb
import json

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST', 'DELETE'])
def test():
    # 打开数据库连接
    db = MySQLdb.connect("127.0.0.1", "root", "123456", "flask_sq_demo", charset="utf8")
    # charset=utf8,解决中文乱码问题
    print(db.character_set_name())
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据库。
    # chaxun=cursor.execute("show tables")
    # print(chaxun)
    data = cursor.fetchone()
    print("Database version : %s " % data)
    cursor.execute("show tables")
    result = cursor.fetchall()
    print(result)
    cursor.execute("select *from users")
    result = cursor.fetchall()
    print(result)
    mysql_list = []
    for i in result:
        # print(i)
        id = i[0]
        name = i[1]
        email = i[2]
        password = i[3]
        role_id = i[4]
        sql_dic = {"id": id, "name": name, "email": email, "password": password, "role_id": role_id}
        # print(sql_json)
        mysql_list.append(sql_dic)
        print(type(sql_dic))
    print(type(mysql_list), mysql_list)
    # 如果不加ensure_ascii=False输出的t如果有汉字的话都默认给转换
    # 成一堆编码如果加上的话 就都能正常显示变成了汉字
    mysql_json = json.dumps(mysql_list, ensure_ascii=False)
    print(type(mysql_json), mysql_json)
    # 关闭数据库连接
    db.close()
    return mysql_json


if __name__ == '__main__':
    app.run(debug=True)
