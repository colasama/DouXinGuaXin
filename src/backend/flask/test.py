#!/usr/bin/env python
# -*- coding:utf-8 -*-
from requests import post, get, put

# Register
post('http://localhost:5000/register', data={'name': 'yzy','password':'yzy123456',
                                             'email':'123@qq.com','phonenum':'123456789','motto':'balabalabala'}).json()

# Login
post('http://localhost:5000/login', data={'name': 'yzy','password':'yzy123456'}).json()

token=post('http://localhost:5000/login', data={'name': 'yzy','password':'yzy123456'}).json()['result']['token']

# 上面是直接用宇神的
# 下面我是用 postman测试的，token需要加在 header里
# ModifyPassword + token
post('http://localhost:5000/modify/passwd', data={'old_password': 'yzy123456','new_password':'yzygod'}).json()

# Book_Comment + token
post('http://localhost:5000/books/1/comments',
     data={'book_comment_content': 'yzygoddddddddddddddddddddddddd','book_comment_title':'yzygodd'}).json()

# Book_Score + token
post('http://localhost:5000/books/1/scores', data={'book_score': '9.0'}).json()

# Movie_Comment + token
post('http://localhost:5000/movies/1/comments',
     data={'movie_comment_content': 'yzygoddddddddddddddddddddddddd','movie_comment_title':'yzygodd'}).json()

# Movie_Score + token
post('http://localhost:5000/movies/1/scores', data={'movie_score': '9.0'}).json()

# AddUserToGroup + token
post('http://localhost:5000/groups/1/join').json()

# AddUserToTopic + token
post('http://localhost:5000/topicss/1/join').json()