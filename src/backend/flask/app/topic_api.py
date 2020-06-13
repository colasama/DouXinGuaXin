#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
from flask import request,Response
from flask_restful.reqparse import RequestParser

from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from app import api
from flask_restful import Resource, reqparse
import time
import os

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
            "SELECT Topic_content_id,Topic_content_content,Topic_content_image,Topic_id,Create_time,`User`.User_id,`User`.User_name FROM Topic_Contents,`User`\
            WHERE Topic_id = %d AND Topic_Contents.User_id=`User`.User_id" % (topic_id))
        content = cursor.fetchall()
        connection.commit()
        for i in content:
            i['Create_time'] = str(i['Create_time'])
        return {'result': {
            'info': result,
            'contents': content,
        }}


class Get_topic_by_keywords(Resource):
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


class Get_topic_content_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Topic_Contents WHERE Topic_content_content LIKE '%s' " % (keywords))
        result = cursor.fetchall()
        connection.commit()
        for i in result:
            i['Create_time'] = str(i['Create_time'])
        return {'result': result}


class Add_user_to_topic(Resource):
    def post(self, topic_id):   # 点击按钮进行参与，post请求
        parser = RequestParser()
        parser.add_argument('token', type=str, location='headers', required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
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


class Post_topic_content(Resource):
    def post(self, topic_id):
        parser = RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        parser.add_argument('topic_content_content', type=str, required=True)
        parser.add_argument('topic_content_image', type=str)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM User_Topic where User_id = %d and Topic_id = %d" % (
                user_id, topic_id)
        )
        result = cursor.fetchone()
        connection.commit()
        if result is None:
            return {'message': 'You have not joined the topic.'}, 403
        topic_content_content = args['topic_content_content']
        topic_content_image = args['topic_content_image']
        cursor.execute(
            "INSERT into Topic_Contents( Topic_content_content, Topic_id, \
            User_id, Topic_content_image) \
            values('%s',%d,%d,'%s')" %
            (topic_content_content,topic_id, user_id, topic_content_image)
        )
        connection.commit()
        cursor.execute(
            "SELECT LAST_INSERT_ID()"
        )
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Topic_Contents where Topic_content_id = %d" % result
        )
        result = cursor.fetchone()
        connection.commit()
        result['Create_time'] = str(result['Create_time'])
        return {'result': result}


class Get_hot_topic(Resource):
    def get(self):
        cursor.execute(
            "SELECT Topic_id FROM Topic_Contents GROUP BY Topic_id ORDER BY COUNT(Topic_Content_id) DESC"
        )
        result = cursor.fetchmany(2)
        connection.commit()
        cursor.execute(
            "SELECT * FROM Topics WHERE Topic_id = '%d' or Topic_id = '%d'"
            % (result[0]['Topic_id'], result[1]['Topic_id'])
        )
        result = cursor.fetchall()
        connection.commit()
        return {'result': result}


class Add_pic(Resource):
    def post(self):
        img = request.files.get('file')
        millis = int(round(time.time() * 1000))
        ext = os.path.splitext(img.filename)[-1]
        filename = str(millis)+ext
        img.save('../pic/'+filename)
        return{'url':'http://182.92.57.178:5000/pictures/'+filename}


class Get_pic(Resource):
    def get(self,pic_name):
        try:
            file = open('../pic/'+pic_name, 'rb')
            img = file.read()
            resp = Response(img, mimetype="image")
            return resp
        except FileNotFoundError :
            abort_if_doesnt_exist("pictrue not found")

api.add_resource(Get_all_topics, '/topics')
api.add_resource(Get_topics_by_id, '/topics/<int:topic_id>')
api.add_resource(Add_user_to_topic, '/topics/<int:topic_id>/join')
api.add_resource(Get_topic_by_keywords, '/search/topics')
api.add_resource(Get_topic_content_by_keywords, '/search/topic_contents')
api.add_resource(Post_topic_content, '/topics/<int:topic_id>/add_content')
api.add_resource(Get_hot_topic, '/topics/hot')
api.add_resource(Add_pic,'/pictures/add')
api.add_resource(Get_pic,'/pictures/<pic_name>')