#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from app import scheduler
from app._api import cursor, connection, verify_token, abort_if_doesnt_exist

def alive():
    cursor.execute(
            "SELECT * FROM phones")
    cursor.fetchone()
    connection.commit()
    print('interval execute.')


job = {
    'id': 'alive',  # 任务的唯一ID，不要冲突
    'func': 'alive',   # 执行任务的function名称
    'args': "",  # 如果function需要参数，就在这里添加
}
result = scheduler.add_job(
    func=__name__+':'+job['func'], id=job['id'], trigger='interval', hours=2)
print(result)

