#!/usr/bin/env python
# -*- coding:utf-8 -*-
from requests import post, get, put, delete


# Register
post('http://182.92.57.178:5000/register', data={'name': 'yzy', 'password': 'yzy123456',
                                             'email': '123@qq.com', 'phonenum': '123456789', 'motto': 'balabalabala'}).json()

# Login
post('http://localhost:5000/login',
     data={'name': 'yzy', 'password': 'yzy123456'}).json()

token = post('http://localhost:5000/login',
             data={'name': 'yzy', 'password': 'yzy123456'}).json()['result']['token']
# 添加 token到头
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-us",
           "Connection": "keep-alive",
           "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
           "token": token}
# get测试
get('http://localhost:5000/movies/1').json()
get('http://127.0.0.1:5000/search/group_contents?keywords=testtesttest').json()
get('http://localhost:5000/users/book_approvals',headers = headers).json()
# post测试
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

# Comment_Approve
post('http://localhost:5000/book_comments/6/approve',
     data={'type': 1}, headers=headers).json()
delete('http://localhost:5000/movie_comments/1/approve',headers = headers).json()

# Movie_Comment + token
post('http://localhost:5000/movies/1/comments',
     data={'movie_comment_content': 'test', 'movie_comment_title': 'test'}, headers=headers).json()

# Movie_Score + token
post('http://localhost:5000/movies/1/scores',
     data={'movie_score': '9.0'}, headers=headers).json()

# AddUserToGroup + token
post('http://localhost:5000/groups/1/join', headers=headers).json()

# AddUserToTopic + token
post('http://localhost:5000/topicss/1/join', headers=headers).json()
post('http://localhost:5000/topics/1/join', headers=headers).json()

# Add Group Content + token
post('http://localhost:5000/groups/1/add_content',
     data={'group_content_title': 'test123', 'group_content_content': 'testtesttest123', 'group_content_image': '/example'}, headers=headers).json()
# 删除，加精，置顶
post('http://localhost:5000/groups/delete_content/3', headers=headers).json()
post('http://localhost:5000/groups/highlighted_content/5', headers=headers).json()
post('http://localhost:5000/groups/pinned_content/5', headers=headers).json()
post('http://localhost:5000/groups/2/apply_manager',data={'group_apply_content': 'test'},headers=headers).json()

# Add Topic Content + token
post('http://localhost:5000/topics/1/add_content',
     data={'topic_content_content': 'testtesttest'}, headers=headers).json()

# Send_email
post('http://localhost:5000/users/reset_password/send_email', data={'user_email': '394739138@qq.com'}
     ).json()

# Reset_password + token
post('http://localhost:5000/users/reset_password',
     data={'new_password': 'zhk12345678'}, headers=headers).json()

# Book_comment_report + token
post('http://localhost:5000/report/books/1', data={'book_report_title': 'yzygod', 'book_report_reason':
                                                   'yzygoddddddddddddd'}, headers=headers).json()

# Movie_comment_report + token
post('http://localhost:5000/report/movies/1', data={'movie_report_title': 'yzygod', 'movie_report_reason':
                                                    'yzygoddddddddddddd'}, headers=headers).json()
