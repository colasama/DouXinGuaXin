#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sshtunnel import SSHTunnelForwarder
import pymysql

server = SSHTunnelForwarder(
    ssh_address_or_host=('182.92.57.178', 22),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='Buaa1813Se',  # 跳转机的密码
    remote_bind_address=('127.0.0.1', 3306))
server.start()
connection = pymysql.connect(
    user="root",
    passwd="8cn1D89ncac",
    host="127.0.0.1",
    db='platform',
    port=server.local_bind_port)
cursor = connection.cursor(pymysql.cursors.DictCursor)