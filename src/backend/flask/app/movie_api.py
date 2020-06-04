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
        for i in content:
            i['Create_time'] = str(i['Create_time'])
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
        parser = RequestParser()
        parser.add_argument('token', type=str, location='headers', required=True)
        parser.add_argument('movie_comment_content', type=str, required=True)
        parser.add_argument('movie_comment_title', type=str, required=True)
        args = parser.parse_args(strict=True)
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
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
        connection.commit()
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Movie_Comments where Movie_comment_id = '%d'" % result
        )
        result = cursor.fetchone()
        result['Create_time'] = str(result['Create_time'])
        connection.commit()
        return {'result': result}


class Movie_comment_report(Resource):
    def post(self, movie_comment_id):
        parser = RequestParser()
        parser.add_argument('token', type=str, location='headers', required=True)
        parser.add_argument('movie_report_title', type=str, required=True)
        parser.add_argument('movie_report_reason', type=str, required=True)
        args = parser.parse_args()
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        report_t = args.get('movie_report_title')
        report_r = args.get('movie_report_reason')
        cursor.execute(
            "INSERT INTO Movie_Reports(Movie_report_title, Movie_report_reason, User_id, Movie_comment_id) \
            values('%s', '%s', '%d', '%d')"
            % (report_t, report_r, user_id, movie_comment_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT LAST_INSERT_ID()"
        )
        connection.commit()
        result = cursor.fetchone()['LAST_INSERT_ID()']
        cursor.execute(
            "SELECT * FROM Movie_Reports WHERE Movie_report_id = '%d'" % result
        )
        connection.commit()
        result = cursor.fetchone()
        result['Create_time'] = str(result['Create_time'])
        return {'result': result}


class Movie_score(Resource):
    def post(self, movie_id):
        # 如果用户之前已经评了分，这里默认无法再评分
        parser = RequestParser()
        parser.add_argument('token', type=str, location='headers', required=True)
        parser.add_argument('movie_score', type=float, required=True)
        args = parser.parse_args()
        token = args.get('token')
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
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


class Movie_comment_approve(Resource):
    def post(self,movie_comment_id):
        parser = RequestParser()
        parser.add_argument('token', type=str, location='headers', required=True)
        parser.add_argument('type', type=int, required=True)
        args = parser.parse_args()
        token = args["token"]
        approve_type = args['type']
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        if approve_type !=-1 and approve_type != 1:
            return {'message':'Illegal type(not -1 or 1).'}, 400
        cursor.execute(
            "SELECT Type FROM Movie_Comment_Approvals WHERE Movie_comment_id = %d AND User_id = %d"
            %(movie_comment_id,user_id)
        )
        result = cursor.fetchone()
        if result != None:
            connection.commit()
            return {'message':'duplicate approve or disapprove.'},403
        cursor.execute(
            "INSERT INTO Movie_Comment_Approvals(Movie_comment_id,User_id,type) VALUES(%d,%d,%d)" 
            %(movie_comment_id,user_id,approve_type)
        )
        if approve_type==1:
            temp_str="Movie_comment_approve"
        else:
            temp_str="Movie_comment_disapprove"
        cursor.execute(
            "UPDATE Movie_Comments \
            SET %s = %s + 1 \
            WHERE Movie_comment_id = %d" % (temp_str,temp_str,movie_comment_id,)
        )
        connection.commit()
        cursor.execute(
            "SELECT * FROM Movie_Comments WHERE Movie_comment_id = %d "
            % (movie_comment_id)
        )
        result = cursor.fetchone()
        result['Create_time'] = str(result['Create_time'])
        return {'result': result}
    
    def delete(self,movie_comment_id):
        parser = RequestParser()
        parser.add_argument('token', type=str, location='headers', required=True)
        args = parser.parse_args()
        token = args["token"]
        user_id = verify_token(token)
        if user_id is None:
            return {'message': 'Illegal token.'}, 403
        cursor.execute(
            "SELECT Type FROM Movie_Comment_Approvals WHERE Movie_comment_id = %d AND User_id = %d"
            %(movie_comment_id,user_id)
        )
        result = cursor.fetchone()
        if result == None:
            connection.commit()
            abort_if_doesnt_exist("Movie_comment_id")
        approve_type = result['Type']
        cursor.execute(
            "DELETE FROM Movie_Comment_Approvals WHERE Movie_comment_id = %d AND User_id = %d " 
            %(movie_comment_id,user_id)
        )
        if approve_type==1:
            temp_str="Movie_comment_approve"
        else:
            temp_str="Movie_comment_disapprove"
        cursor.execute(
            "UPDATE Movie_Comments \
            SET %s = %s - 1 \
            WHERE Movie_comment_id = %d" % (temp_str,temp_str,movie_comment_id)
        )
        connection.commit()
        cursor.execute(
            "SELECT * FROM Movie_Comments WHERE Movie_comment_id = %d "
            % (movie_comment_id)
        )
        result = cursor.fetchone()
        result['Create_time'] = str(result['Create_time'])
        connection.commit()
        return {'result': result}

api.add_resource(Get_all_movies, '/movies')
api.add_resource(Get_movies_by_id, '/movies/<movie_id>')
api.add_resource(Movie_comment, '/movies/<int:movie_id>/comments')
api.add_resource(Movie_score, '/movies/<int:movie_id>/scores')
api.add_resource(Get_movies_by_keywords, '/search/movies')
api.add_resource(Movie_comment_report, '/movie_comments/<int:movie_comment_id>/report')
api.add_resource(Movie_comment_approve,'/movie_comments/<int:movie_comment_id>/approve')