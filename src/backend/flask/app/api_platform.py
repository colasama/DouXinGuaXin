#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.sql import cursor, connection
from app import api, app
from flask_restful import Resource, abort, reqparse
from flask_restful.reqparse import RequestParser
from werkzeug.security import generate_password_hash, check_password_hash
from app.tokens import Tokens


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers["token"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            return jsonify(code=4103, msg='缺少参数token')

        s = Serializer(app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token


def abort_if_doesnt_exist(string):
    abort(404, message=string + " doesn't exist")


# 用户
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
        token = Tokens.create_token(result['User_id'])
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
        print(name)
        print(password)
        cursor.execute(
            "SELECT * FROM User WHERE User_name LIKE '%s'" % name
        )
        result = cursor.fetchone()
        connection.commit()
        if result == None:
            return {'message': 'Login error, incorrect password or username.'}, 403
        if check_password_hash(result['User_password'], password):
            token = Tokens.create_token(result['User_id'])
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
        user_id = Tokens.verify_token(token)
        if user_id != None:
            cursor.execute(
                "SELECT User_id,User_name,User_email,User_phonenum,User_authority,User_motto FROM User WHERE User_id LIKE '%s'" %
                (user_id))
            result = cursor.fetchone()
            connection.commit()
            return{'result': result}
        else:
            return {'message': 'Illegal token.'}, 403


class Modify_password(Resource):
    def post(self):
        token = request.headers["token"]
        user_id = Tokens.verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        parser = RequestParser()
        parser.add_argument('old_password', type=str, required=True)
        parser.add_argument('new_password', type=str, required=True)
        args = parser.parse_args(strict=True)
        # 前端记得验证两次密码不同
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


# 电影
class Get_all_movies(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Movies;')
        connection.commit()
        return {'result': cursor.fetchall()}


class Get_movies_by_id(Resource):
    def get(self, movie_id):
        cursor.execute(
            "SELECT * FROM Movies WHERE Movie_id LIKE '%s'" % (movie_id))
        result = cursor.fetchone()
        if result == None:
            abort_if_doesnt_exist("Movie_id")
        cursor.execute(
            "SELECT * FROM Movie_Comments WHERE Movie_id LIKE '%s'" % (movie_id))
        content = cursor.fetchall()
        connection.commit()
        return {'result': {
            'info': result,
            'comments': content,
        }}


class Get_movies_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Movies WHERE Movie_name LIKE '%s' " % (keywords))
        result = cursor.fetchall()
        connection.commit()
        return {'result': result}


class Movie_comment(Resource):
    def post(self, movie_id):
        token = request.headers["token"]
        user_id = Tokens.verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        parser = RequestParser()
        parser.add_argument('movie_comment_content', type=str, required=True)
        parser.add_argument('movie_comment_title', type=str, required=True)
        args = parser.parse_args(strict=True)
        movie_com = args.get('movie_comment_content')
        movie_com_t = args.get('movie_comment_title')
        cursor.execute(
            "INSERT into Movie_Comments(Movie_comment_title, Movie_comment_approve, Movie_comment_disapprove, \
            Movie_comment_content, User_id, Movie_id) \
            values('%s','%d','%d','%s','%d','%d')" %
            (movie_com_t, 0, 0, movie_com, user_id, movie_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT LAST_INSERT_ID()"
        )
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Movie_Comments where Movie_comment_id = '%d'" % result
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


class Movie_score(Resource):
    def post(self, movie_id):
        token = request.headers["token"]
        user_id = Tokens.verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        # 如果用户之前已经评了分，这里默认无法再评分
        parser = RequestParser()
        parser.add_argument('movie_score', type=float, required=True)
        args = parser.parse_args()
        movie_score = float(args.get('movie_score'))
        cursor.execute(
            "SELECT Movie_score, Movie_score_num from Movies where Movie_id = '%d'" % movie_id
        )
        result = cursor.fetchone()
        movie_s = result['Movie_score']
        movie_s_n = result['Movie_score_num']
        new_movie_s = (movie_s * movie_s_n + movie_score) / (movie_s_n + 1.0)
        cursor.execute(
            "UPDATE Movies set Movie_score_num = Movie_score_num + 1, Movie_score = '%f' where Movie_id = '%d'"
            % (new_movie_s, movie_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT Movie_score from Movies where Movie_id = '%d'" % movie_id
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


# 书籍
class Get_all_books(Resource):
    def get(self):
        cursor.execute('SELECT * FROM Books;')
        connection.commit()
        return {'result': cursor.fetchall()}


class Get_books_by_id(Resource):
    def get(self, book_id):
        cursor.execute(
            "SELECT * FROM Books WHERE Book_id LIKE '%s'" % (book_id))
        result = cursor.fetchone()
        if result == None:
            abort_if_doesnt_exist("Book_id")
        cursor.execute(
            "SELECT * FROM Book_Comments WHERE Book_id LIKE '%s'" % (book_id))
        content = cursor.fetchall()
        connection.commit()
        return {'result': {
            'info': result,
            'comments': content,
        }}


class Get_books_by_keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keywords", type=str,
                            location="args", required=True)
        req = parser.parse_args(strict=True)
        keywords = '%'+req.get("keywords")+'%'
        cursor.execute(
            "SELECT * FROM Books WHERE Book_name LIKE '%s' " % (keywords))
        result = cursor.fetchall()
        connection.commit()
        return {'result': result}


class Book_comment(Resource):
    def post(self, book_id):
        token = request.headers["token"]
        user_id = Tokens.verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        # cursor.execute(   # 可能没有必要
        #     "SELECT * from User where User_id = '%d'" % (user_id)
        # )
        # if cursor.fetchone() is None:
        #     return {'message': 'User does not exist.'}, 403
        parser = RequestParser()
        parser.add_argument('book_comment_content', type=str, required=True)
        parser.add_argument('book_comment_title', type=str, required=True)
        args = parser.parse_args(strict=True)
        book_com = args.get('book_comment_content')
        book_com_t = args.get('book_comment_title')
        # if len(book_com) < 25:    # 验证评论字符数 前端可搞定
        #     return {'message': 'Comment should be longer.'}, 403
        cursor.execute(
            "INSERT into Book_Comments(Book_comment_title, Book_comment_approve, Book_comment_disapprove, \
            Book_comment_content, User_id, Book_id) \
            values('%s','%d','%d','%s','%d','%d')" %
            (book_com_t, 0, 0, book_com, user_id, book_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT LAST_INSERT_ID()"
        )
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Book_Comments where Book_comment_id = '%d'" % result
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


class Book_score(Resource):
    def post(self, book_id):
        token = request.headers["token"]
        user_id = Tokens.verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        # 如果用户之前已经评了分，这里默认无法再评分
        parser = RequestParser()
        parser.add_argument('book_score', type=float, required=True)
        args = parser.parse_args()
        book_score = float(args.get('book_score'))
        cursor.execute(
            "SELECT Book_score, Book_score_num from Books where book_id = '%d'" % book_id
        )
        result = cursor.fetchone()
        book_s = result['Book_score']
        book_s_n = result['Book_score_num']
        new_book_s = (book_s * book_s_n + book_score) / (book_s_n + 1.0)
        cursor.execute(
            "UPDATE Books set Book_score_num = Book_score_num + 1, Book_score = '%f' where Book_id = '%d'"
            % (new_book_s, book_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT Book_score from Books where Book_id = '%d'" % book_id
        )
        result = cursor.fetchone()
        connection.commit()
        return {'result': result}


# 话题
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
        if result == None:
            abort_if_doesnt_exist("Topic_id")
        cursor.execute(
            "SELECT * FROM Topic_Contents WHERE Topic_id LIKE '%s'" % (topic_id))
        content = cursor.fetchall()
        connection.commit()
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
        user_id = Tokens.verify_token(token)
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


# 小组
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
        if result == None:
            abort_if_doesnt_exist("Group_id")
        cursor.execute(
            "SELECT * FROM Group_Contents WHERE Group_id LIKE '%s'" % (group_id))
        content = cursor.fetchall()
        connection.commit()
        return {'result': {
            'info': result,
            'contents': content,
        }}


class Add_user_to_group(Resource):
    def post(self, group_id):   # 点击按钮进行参与，post请求
        token = request.headers["token"]
        user_id = Tokens.verify_token(token)
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


# 添加API路由
# 用户
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Get_user_info, '/users/info')
api.add_resource(Modify_password, '/users/modify_password')


# 电影
api.add_resource(Get_all_movies, '/movies')
api.add_resource(Get_movies_by_id, '/movies/<movie_id>')
api.add_resource(Movie_comment, '/movies/<int:movie_id>/comments')
api.add_resource(Movie_score, '/movies/<int:movie_id>/scores')

# 书籍
api.add_resource(Get_all_books, '/books')
api.add_resource(Get_books_by_id, '/books/<books_id>')
api.add_resource(Book_comment, '/books/<int:book_id>/comments')
api.add_resource(Book_score, '/books/<int:book_id>/scores')

# 话题
api.add_resource(Get_all_topics, '/topics')
api.add_resource(Get_topics_by_id, '/topics/<topic_id>')
api.add_resource(Add_user_to_topic, '/topics/<int:topic_id>/join')

# 小组
api.add_resource(Get_all_groups, '/groups')
api.add_resource(Get_groups_by_id, '/groups/<int:group_id>')
api.add_resource(Add_user_to_group, '/groups/<int:group_id>/join')

# 检索
api.add_resource(Get_movies_by_keywords, '/search/movies')
api.add_resource(Get_topics_by_keywords, '/search/books')
