# autotrade/server/index.py
# 在这里写对应的http接口函数
import datetime
from flask import Flask, request, send_file
import json
from flask_sqlalchemy import SQLAlchemy
# 引用路由
from __init__ import app

# 链接并配置mysql数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@127.0.0.1:3306/flask_sq_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # repr方法显示一个可读的字符串
    def __repr__(self):
        # 返回一个列表字典
        return '{\'id\':%s,\'name\':%s,\'password\':%s,\'email\':%s,\'role_id\':%s}' % (
        self.id, self.name, self.password, self.email, self.role_id)
    # User希望有role属性，但是这个属性的定义，需要在另一个模型中定义


@app.route('/')
def index():
    """index.html主页返回"""
    return 'I have receive you request !'


@app.route('/music/', methods=['GET', 'POST', 'DELETE'])
def music():
    return send_file("F:\PyCharm 2018.2.2\\flask_api\src\盗将行.mp3")


@app.route('/order/', methods=['GET', 'POST', 'DELETE'])
def order():
    #访问地址为: http://127.0.0.1:5000/order?id=
    """/order.html接口，接收get请求，解析url中的参数"""
    print(request.url)  # 请求的http网址
    data = request.args.to_dict()  # 解析http中的参数
    # print(type(data["id"]), data["id"])
    name = "小画"
    body = [1, 2, 3, 4, 5]
    j = {}
    j["body"] = body

    users = User.query.all()
    print(type(users), users)
    # print(len(users))
    # mysql_json = json.dumps(users, ensure_ascii=False)
    # print(mysql_json)

    user_list = []
    for user in users:
        user_dic = {}
        user_dic['id'] = user.id
        user_dic['name'] = user.name
        user_dic['email'] = user.email
        user_dic['password'] = user.password
        user_dic['role_id'] = user.role_id
        user_list.append(user_dic)
    print(user_list)
    mysql_json = json.dumps(user_list, ensure_ascii=False)
    # mysql_json=eval(mysql_json)
    # mysql_json=mysql_json.replace("\"","")
    print("mysql_json:", type(mysql_json), mysql_json)
    for i in json.loads(mysql_json):
        print(i)
        print(type(i['id']), i['id'])
        # print(users)
        if data['id'] == str(i['id']):
            print(data["id"], str(i['id']))
            # to something here
            mysql_j = json.dumps(i)
            print(mysql_j)
            return mysql_j  # 注意，不管什么问题，一定要返回，就算是返回None
    else:
        return mysql_json
        # return json.dumps("sss")
