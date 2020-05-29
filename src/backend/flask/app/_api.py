#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_restful import abort
from app import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sshtunnel import SSHTunnelForwarder
import pymysql

server = SSHTunnelForwarder(
    ssh_address_or_host=('182.92.57.178', 22),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='Buaa1813Se',  # 跳转机的密码
    remote_bind_address=('127.0.0.1', 3306))
server.start()
connection = pymysql.connect(
    user="root",
    passwd="8cn1D89ncac",
    host="127.0.0.1",
    db='platform',
    port=server.local_bind_port)
cursor = connection.cursor(pymysql.cursors.DictCursor)


def abort_if_doesnt_exist(string):
    abort(404, message=string + " doesn't exist")


def create_token(user_id):
    """
    生成token
    :param user_id: 用户id
    :return:
    """

    # 第一个参数是内部的私钥，这里写在配置信息里，如果只是测试可以写死
    # 第二个参数是有效期（秒）
    s = Serializer(app.config['SECRET_KEY'], expires_in=app.config['TOKEN_EXPIRATION'])
    # 接收用户id转换与编码
    token = s.dumps({"id": user_id}).decode('ascii')
    return token


def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''

    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(app.config['SECRET_KEY'])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据
    return data["id"]


# 验证 token的装饰器 现在未采用
# def login_required(view_func):
#     @functools.wraps(view_func)
#     def verify_token(*args, **kwargs):
#         try:
#             # 在请求头上拿到token
#             token = request.headers["token"]
#         except Exception:
#             # 没接收的到token,给前端抛出错误
#             # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
#             return jsonify(code=4103, msg='缺少参数token')
#
#         s = Serializer(app.config["SECRET_KEY"])
#         try:
#             s.loads(token)
#         except Exception:
#             return jsonify(code=4101, msg="登录已过期")
#
#         return view_func(*args, **kwargs)
#
#     return verify_token


