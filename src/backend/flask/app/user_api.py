#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request, render_template
from app._api import cursor, connection, verify_token, create_token
from app import api, app
from flask_restful import Resource, reqparse
from flask_restful.reqparse import RequestParser
from werkzeug.security import generate_password_hash, check_password_hash
from app.email import send_email


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("phonenum", type=str, required=True)
        parser.add_argument("motto", type=str)
        req = parser.parse_args(strict=True)
        name = req['name']
        password = req['password']
        pwhash = generate_password_hash(
            password, method='pbkdf2:sha1', salt_length=8)
        email = req['email']
        phonenum = req['phonenum']
        motto = req['motto']
        cursor.execute(
            "INSERT INTO `User` (User_password,User_name,User_email,User_phonenum,User_authority,User_motto) VALUES ('%s','%s','%s','%s',1,'%s')" %
            (pwhash, name, email, phonenum, motto))
        connection.commit()
        cursor.execute(
            "SELECT User_id FROM User WHERE User_name LIKE '%s'" %
            (name)
        )
        result = cursor.fetchone()
        token = create_token(result['User_id'])
        connection.commit()
        return {'result': {
                'token': token
                }}


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        req = parser.parse_args(strict=True)
        name = req['name']
        password = req['password']
        cursor.execute(
            "SELECT * FROM User WHERE User_name LIKE '%s'" % name
        )
        result = cursor.fetchone()
        connection.commit()
        if result is None:
            return {'message': 'Login error, incorrect password or username.'}, 403
        if check_password_hash(result['User_password'], password):
            token = create_token(result['User_id'])
            return {'result': {
                'token': token
            }}
        else:
            return {'message': 'Login error, incorrect password or username.'}, 403


class Get_user_info(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str,
                            location="headers", required=True)
        req = parser.parse_args(strict=True)
        token = req['token']
        user_id = verify_token(token)
        if user_id is not None:
            cursor.execute(
                "SELECT User_id,User_name,User_email,User_phonenum,User_authority,User_motto FROM User WHERE User_id LIKE '%s'" %
                (user_id))
            result = cursor.fetchone()
            connection.commit()
            return{'result': result}
        else:
            return {'message': 'Illegal token.'}, 403


class Get_user_movie_approvals(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('token', type=str,
                            location='headers', required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Movie_Comment_Approvals WHERE User_id = %d" %
            (user_id))
        result = cursor.fetchall()
        connection.commit()
        return {"result": result}


class Get_user_book_approvals(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('token', type=str,
                            location='headers', required=True)
        args = parser.parse_args(strict=True)
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Book_Comment_Approvals WHERE User_id = %d" %
            (user_id))
        result = cursor.fetchall()
        connection.commit()
        return {"result": result}


class Modify_password(Resource):
    def post(self):
        parser = RequestParser()
        parser.add_argument('token', type=str,
                            location='headers', required=True)
        parser.add_argument('old_password', type=str, required=True)
        parser.add_argument('new_password', type=str, required=True)
        args = parser.parse_args(strict=True)
        # 前端记得验证两次密码不同
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        old_p = args.get('old_password')
        new_p = args['new_password']
        new_p_hash = generate_password_hash(
            new_p, method='pbkdf2:sha1', salt_length=8)
        cursor.execute(
            "SELECT User_password FROM User WHERE User_id = '%d' " % user_id
        )
        result = cursor.fetchone()['User_password']
        connection.commit()
        if result is None:
            return {'message': 'User does not exist.'}, 403
        if check_password_hash(result, old_p):
            cursor.execute(
                "UPDATE User set User_password = '%s' WHERE User_id = '%d' " % (
                    new_p_hash, user_id)
            )
            connection.commit()
            return {'result': {
                'message': 'Modify successfully.'
            }}
        else:
            return {'message': 'The old password is wrong.'}, 403


class Send_email(Resource):
    '''发送重设密码邮件'''

    def post(self):
        parser = RequestParser()
        parser.add_argument('user_email', type=str, required=True)
        args = parser.parse_args(strict=True)
        email = args.get('user_email')
        cursor.execute(
            "SELECT * FROM User WHERE User_email = '%s'" % email
        )
        connection.commit()
        result = cursor.fetchone()
        if result is None:
            return {'message': 'Wrong email.'}, 403
        send_email('[豆辛瓜辛] Reset Your Password',
                   sender=app.config['ADMINS'][0],
                   recipients=[email],  # templates中内容暂时用于测试
                   text_body=render_template(
                       'reset_password.txt', user=result),
                   html_body=render_template('reset_password.html', user=result))


class Reset_password(Resource):
    def post(self):
        parser = RequestParser()
        parser.add_argument('new_password', type=str, required=True)
        parser.add_argument('token', type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        n_pw = args.get('new_password')
        n_pwhash = generate_password_hash(n_pw)
        cursor.execute(
            "UPDATE User set User_password = '%s' where User_id = '%d'"
            % (n_pwhash, user_id)
        )
        connection.commit()
        return {'message': 'Reset successfully.'}


class Get_my_group(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('new_password', type=str, required=True)
        parser.add_argument('token', type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM User_Group WHERE User_id = %d" %
            (user_id))
        result = cursor.fetchall()
        connection.commit()
        return {"result": result}


class Get_my_topic(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('new_password', type=str, required=True)
        parser.add_argument('token', type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM User_Topic WHERE User_id = %d" %
            (user_id))
        result = cursor.fetchall()
        connection.commit()
        return {"result": result}


class Get_my_book_comment(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('new_password', type=str, required=True)
        parser.add_argument('token', type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Book_Comments WHERE User_id = %d" %
            (user_id))
        result = cursor.fetchall()
        connection.commit()
        return {"result": result}


class Get_my_movie_comment(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('new_password', type=str, required=True)
        parser.add_argument('token', type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Movie_Comments WHERE User_id = %d" %
            (user_id))
        result = cursor.fetchall()
        connection.commit()
        return {"result": result}


class Get_my_report(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('new_password', type=str, required=True)
        parser.add_argument('token', type=str,
                            location="headers", required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT * FROM Movie_Reports WHERE User_id = %d" %
            (user_id))
        result_m = cursor.fetchall()
        cursor.execute(
            "SELECT * FROM Book_Reports WHERE User_id = %d" %
            (user_id))
        result_b = cursor.fetchall()
        connection.commit()
        return {"result": {"books": result_b, "movies": result_m}}


api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Get_user_info, '/users/info')
api.add_resource(Modify_password, '/users/modify_password')
api.add_resource(Send_email, '/users/reset_password/send_email')
api.add_resource(Reset_password, '/users/reset_password')
api.add_resource(Get_user_movie_approvals, '/users/movie_approvals')
api.add_resource(Get_user_book_approvals, '/users/book_approvals')
api.add_resource(Get_my_group, '/users/groups')
api.add_resource(Get_my_topic, '/users/topics')
api.add_resource(Get_my_book_comment, '/users/book_comments')
api.add_resource(Get_my_movie_comment, '/users/movie_comments')
api.add_resource(Get_my_report,'/users/reports')
