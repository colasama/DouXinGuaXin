#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Api
from config import Config
from flask_mail import Mail


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
mail = Mail(app)


from app import book_api, movie_api, group_api, topic_api, user_api

