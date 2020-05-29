#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
from flask import request
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from app import api
from flask_restful import Resource, reqparse


class Get_all_topics(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Topics;')
        connection.commit()
        return {'result': cursor.fetchall()}


class Get_topics_by_id(Resource):
    def get(self, topic_id):
        cursor.execute(
            "SELECT * FROM Topics WHERE Topic_id LIKE '%s'" % (topic_id))
        result = cursor.fetchone()
        if result is None:
            abort_if_doesnt_exist("Topic_id")
        cursor.execute(
            "SELECT * FROM Topic_Contents WHERE Topic_id LIKE '%s'" % (topic_id))
        content = cursor.fetchall()
        connection.commit()
        for i in content:
            i['Create_time']=str(i['Create_time'])
        return {'result': {
            'info': result,
            'contents': content,
        }}


class Get_topics_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Topics WHERE Topic_name LIKE '%s' OR Topic_related LIKE '%s' " % (keywords, keywords))
        result = cursor.fetchall()
        connection.commit()
        return {'result': result}


class Add_user_to_topic(Resource):
    def post(self, topic_id):   # 点击按钮进行参与，post请求
        token = request.headers["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM User_Topic where User_id = %d and Topic_id = %d" % (
                user_id, topic_id)
        )
        result = cursor.fetchone()
        connection.commit()
        if result is not None:
            return {'message': 'You have joined the topic before.'}, 403
        # 如果用户之前已经参与过该话题了 就应该无法点击按钮 所以在这里没有处理
        cursor.execute(
            "INSERT INTO User_Topic values('%d', '%d')" % (topic_id, user_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT * from User_Topic where User_id = '%d' and Topic_id = '%d'" % (
                user_id, topic_id)
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


api.add_resource(Get_all_topics, '/topics')
api.add_resource(Get_topics_by_id, '/topics/<topic_id>')
api.add_resource(Add_user_to_topic, '/topics/<int:topic_id>/join')
api.add_resource(Get_topics_by_keywords, '/search/topics')