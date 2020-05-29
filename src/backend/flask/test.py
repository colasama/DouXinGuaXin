#!/usr/bin/env python
# -*- coding:utf-8 -*-
from requests import post, get, put

# Register
post('http://localhost:5000/register', data={'name': 'yzy', 'password': 'yzy123456',
                                             'email': '123@qq.com', 'phonenum': '123456789', 'motto': 'balabalabala'}).json()

# Login
post('http://localhost:5000/login',
     data={'name': 'yzy', 'password': 'yzy123456'}).json()

token = post('http://localhost:5000/login',
             data={'name': 'yzy', 'password': 'yzy123456'}).json()['result']['token']
# 添加token到头
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-us",
           "Connection": "keep-alive",
           "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
           "token": token}
#get测试
get('http://localhost:5000/movies/1').json()

#post测试
# 下面我是用 postman测试的，token需要加在 header里
# ModifyPassword + token
post('http://localhost:5000/modify/passwd',
     data={'old_password': 'yzy123456', 'new_password': 'yzygod'}, headers=headers).json()

# Book_Comment + token
post('http://localhost:5000/books/1/comments',
     data={'book_comment_content': 'yzygoddddddddddddddddddddddddd', 'book_comment_title': 'yzygodd'}, headers=headers).json()

# Book_Score + token
post('http://localhost:5000/books/1/scores',
     data={'book_score': '9.0'}, headers=headers).json()

# Movie_Comment + token
post('http://localhost:5000/movies/1/comments',
     data={'movie_comment_content': 'test', 'movie_comment_title': 'test'}, headers=headers).json()

# Movie_Score + token
post('http://localhost:5000/movies/1/scores',
     data={'movie_score': '9.0'}, headers=headers).json()

# AddUserToGroup + token
post('http://localhost:5000/groups/1/join', headers=headers).json()

# AddUserToTopic + token
post('http://localhost:5000/topics/1/join', headers=headers).json()

# Add Group Content + token
post('http://localhost:5000/groups/1/add_content',
     data={'group_content_title': 'test', 'group_content_content': 'testtesttest', 'group_content_image':'/example'}, headers=headers).json()

# Add Topic Content + token
post('http://localhost:5000/topics/1/add_content',
     data={'topic_content_content': 'testtesttest'}, headers=headers).json()