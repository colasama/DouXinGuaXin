#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist
from app import api
from flask_restful import Resource, reqparse
from flask_restful.reqparse import RequestParser


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
        if result is None:
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
        user_id = verify_token(token)
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
        user_id = verify_token(token)
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


api.add_resource(Get_all_movies, '/movies')
api.add_resource(Get_movies_by_id, '/movies/<movie_id>')
api.add_resource(Movie_comment, '/movies/<int:movie_id>/comments')
api.add_resource(Movie_score, '/movies/<int:movie_id>/scores')
api.add_resource(Get_movies_by_keywords, '/search/movies')