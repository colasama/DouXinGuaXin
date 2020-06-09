#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Api
from config import Config
from flask_mail import Mail
from flask_apscheduler import APScheduler
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
app.config.from_object(Config)
mail = Mail(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from app import book_api, movie_api, group_api, topic_api, user_api, task