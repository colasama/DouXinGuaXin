#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Api
from config import Config


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)


from app import api_platform, tokens, sql

