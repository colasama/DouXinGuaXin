#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request
from app import api
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from flask_restful import Resource
from flask_restful.reqparse import RequestParser


class Get_all_groups(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Groups;')
        connection.commit()
        return {'result': cursor.fetchall()}


class Get_groups_by_id(Resource):
    def get(self, group_id):
        cursor.execute(
            "SELECT * FROM Groups WHERE Group_id LIKE '%s'" % (group_id))
        result = cursor.fetchone()
        if result is None:
            abort_if_doesnt_exist("Group_id")
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_id LIKE '%s'" % (group_id))
        content = cursor.fetchall()
        connection.commit()
        for i in content:
            i['Create_time'] = str(i['Create_time'])
        return {'result': {
            'info': result,
            'contents': content,
        }}


class Add_user_to_group(Resource):
    def post(self, group_id):   # 点击按钮进行参与，post请求
        token = request.headers["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM User_Group where User_id = %d and Group_id = %d" % (
                user_id, group_id)
        )
        result = cursor.fetchone()
        connection.commit()
        if result is not None:
            return {'message': 'You have joined the group before.'}, 403
        cursor.execute(
            "INSERT INTO User_Group values('%d', '%d')" % (group_id, user_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT * from User_Group where User_id = '%d' and Group_id = '%d'" % (
                user_id, group_id)
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


class Post_group_content(Resource):
    def post(self, group_id):
        parser = RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        parser.add_argument('group_content_title', type=str, required=True)
        parser.add_argument('group_content_content', type=str, required=True)
        parser.add_argument('group_content_image', type=str)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM User_Group where User_id = %d and Group_id = %d" % (
                user_id, group_id)
        )
        result = cursor.fetchone()
        connection.commit()
        if result is None:
            return {'message': 'You have not joined the group.'}, 403
        group_content_title = args['group_content_title']
        group_content_content = args['group_content_content']
        group_content_image = args['group_content_image']
        cursor.execute(
            "INSERT into Group_Contents(Group_content_title, Group_content_content, Group_id, \
            User_id, Group_content_image) \
            values('%s','%s',%d,%d,'%s')" %
            (group_content_title, group_content_content,
             group_id, user_id, group_content_image)
        )
        connection.commit()
        cursor.execute(
            "SELECT LAST_INSERT_ID()"
        )
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Group_Contents where Group_content_id = %d" % result
        )
        result = cursor.fetchone()
        connection.commit()
        result['Create_time'] = str(result['Create_time'])
        return {'result': result}


api.add_resource(Get_all_groups, '/groups')
api.add_resource(Get_groups_by_id, '/groups/<int:group_id>')
api.add_resource(Add_user_to_group, '/groups/<int:group_id>/join')
api.add_resource(Post_group_content, '/groups/<int:group_id>/add_content')
