#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request
from flask_restful.reqparse import RequestParser

from app import api
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from flask_restful import Resource, reqparse


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
            "SELECT Group_content_id,Group_content_content,Group_content_title,Group_id,Group_content_image,Create_time,\
            Is_highlighted,Is_pinned,`User`.User_id,`User`.User_name FROM Group_Contents,`User`\
            WHERE Group_id=%d and Group_Contents.User_id=User.User_id ORDER BY Is_pinned DESC" % (group_id))
        content = cursor.fetchall()
        connection.commit()
        for i in content:
            i['Create_time'] = str(i['Create_time'])
        return {'result': {
            'info': result,
            'contents': content,
        }}


class Get_group_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Groups WHERE Group_name LIKE '%s' OR Group_related LIKE '%s' " % (keywords, keywords))
        result = cursor.fetchall()
        connection.commit()
        return {'result': result}


class Get_group_content_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_content_title LIKE '%s' OR Group_content_content LIKE '%s' " % (keywords, keywords))
        result = cursor.fetchall()
        connection.commit()
        for i in result:
            i['Create_time'] = str(i['Create_time'])
        return {'result': result}


class Add_user_to_group(Resource):
    def post(self, group_id):   # 点击按钮进行参与，post请求
        parser = RequestParser()
        parser.add_argument('token', type=str,
                            location='headers', required=True)
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
            User_id, Group_content_image,Is_highlighted,Is_pinned) \
            values('%s','%s',%d,%d,'%s',0,0)" %
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


class Delete_group_content(Resource):
    def post(self, group_content_id):
        parser = RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        result = cursor.fetchone()
        connection.commit()
        if result is None:
            abort_if_doesnt_exist("Group_content_id")
        group_id = result['Group_id']
        cursor.execute(
            "SELECT * FROM Groups WHERE Group_id like '%s' " % (
                group_id, )
        )
        result = cursor.fetchone()
        if result['User_id'] != user_id:
            return{'message': 'Unauthorized.'}, 401
        cursor.execute(
            "DELETE FROM Group_Contents WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        connection.commit()
        return{'result': {
            'message': 'Delete success.'
        }}


class Highlighted_group_content(Resource):
    def post(self, group_content_id):
        parser = RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        result = cursor.fetchone()
        connection.commit()
        if result is None:
            abort_if_doesnt_exist("Group_content_id")
        group_id = result['Group_id']
        cursor.execute(
            "SELECT * FROM Groups WHERE Group_id like '%s' " % (
                group_id, )
        )
        result = cursor.fetchone()
        if result['User_id'] != user_id:
            return{'message': 'Unauthorized.'}, 401
        cursor.execute(
            "UPDATE Group_Contents SET Is_highlighted=1 \
            WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        connection.commit()
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        result = cursor.fetchone()
        connection.commit()
        result['Create_time'] = str(result['Create_time'])
        return {'result': result}


class Pinned_group_content(Resource):
    def post(self, group_content_id):
        parser = RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        result = cursor.fetchone()
        connection.commit()
        if result is None:
            abort_if_doesnt_exist("Group_content_id")
        group_id = result['Group_id']
        cursor.execute(
            "SELECT * FROM Groups WHERE Group_id like '%s' " % (
                group_id, )
        )
        result = cursor.fetchone()
        if result['User_id'] != user_id:
            return{'message': 'Unauthorized.'}, 401
        cursor.execute(
            "UPDATE Group_Contents SET Is_pinned=1 \
            WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        connection.commit()
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_content_id like '%s' " % (
                group_content_id, )
        )
        result = cursor.fetchone()
        connection.commit()
        result['Create_time'] = str(result['Create_time'])
        return {'result': result}


class Apply_manager(Resource):
    def post(self, group_id):
        parser = RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        parser.add_argument('group_apply_content', type=str, required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        group_apply_content = args['group_apply_content']
        cursor.execute(
            "INSERT into Group_Apply(Group_apply_content,Group_id,User_id)\
            VALUES('%s',%d,%d)" % (group_apply_content, group_id, user_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT LAST_INSERT_ID()"
        )
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Group_Apply where Group_apply_id = %d" % result
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


api.add_resource(Get_all_groups, '/groups')
api.add_resource(Get_groups_by_id, '/groups/<int:group_id>')
api.add_resource(Get_group_by_keywords, '/search/groups')
api.add_resource(Get_group_content_by_keywords, '/search/group_contents')
api.add_resource(Add_user_to_group, '/groups/<int:group_id>/join')
api.add_resource(Post_group_content, '/groups/<int:group_id>/add_content')
api.add_resource(Apply_manager, '/groups/<int:group_id>/apply_manager')
api.add_resource(Delete_group_content,
                 '/groups/delete_content/<int:group_content_id>')
api.add_resource(Highlighted_group_content,
                 '/groups/highlighted_content/<int:group_content_id>')
api.add_resource(Pinned_group_content,
                 '/groups/pinned_content/<int:group_content_id>')
