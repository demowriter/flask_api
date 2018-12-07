# autotrade/__init__.py
# __init__.py 定义全局的app路由
# 然后将其他模块由app装饰后的函数导入，flask即可识别所有的请求入口
import time
from flask import Flask
from multiprocessing import Process
from flask_sqlalchemy import SQLAlchemy

# 配置全局app
app = Flask(__name__)
# 导入index中定义的所有函数
from index import *

def run_index():
    # 启动web服务器，使用多线程方式，接收所有http请求
    app.run(host='127.0.0.1', port=5000, threaded=True)

def run_orders():
    pass
#     # 启动查询交易程序
#     while True:
#         # print('执行相应的交易程序')
#         time.sleep(3)

def main():
    # 主程序
    # 创建子进程
    jobs = []
    jobs.append(Process(target=run_index))
    jobs.append(Process(target=run_orders))
    # 启动子进程
    for job in jobs:
        job.start()

    # 等待子进程结束返回
    for job in jobs:
        job.join()

if __name__ == '__main__':
    main()