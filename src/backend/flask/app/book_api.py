#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from app import api
from flask_restful import Resource, reqparse
from flask_restful.reqparse import RequestParser


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
        if result is None:
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
        user_id = verify_token(token)
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


class Book_comment_report(Resource):
    def post(self):
        token = request.headers["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        # 如果用户之前已经评了分，这里默认无法再评分
        parser = RequestParser()


class Book_score(Resource):
    def post(self, book_id):
        token = request.headers["token"]
        user_id = verify_token(token)
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


api.add_resource(Get_all_books, '/books')
api.add_resource(Get_books_by_id, '/books/<books_id>')
api.add_resource(Book_comment, '/books/<int:book_id>/comments')
api.add_resource(Book_score, '/books/<int:book_id>/scores')
api.add_resource(Get_books_by_keywords, '/search/books')