#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request
from app import api
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from flask_restful import Resource


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
            i['Create_time']=str(i['Create_time'])
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


api.add_resource(Get_all_groups, '/groups')
api.add_resource(Get_groups_by_id, '/groups/<int:group_id>')
api.add_resource(Add_user_to_group, '/groups/<int:group_id>/join')