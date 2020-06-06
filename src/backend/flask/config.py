#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


class Config(object):
    #私钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
    TOKEN_EXPIRATION = 3600
    # 配置邮箱
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = '465'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "394739138@qq.com"
    MAIL_PASSWORD = "fzbasfokqcnhbjhh"
    MAIL_DEBUG = True
    ADMINS = ['394739138@qq.com']
    #定时任务
    SCHEDULER_API_ENABLED = True
    #
    accesslog = "log/access.log"
    errorlog = "log/debug.log"



