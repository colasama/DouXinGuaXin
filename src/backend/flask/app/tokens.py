#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.sql import cursor
from app import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Tokens(object):
    @staticmethod
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

    @staticmethod
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

