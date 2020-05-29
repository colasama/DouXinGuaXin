#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread
from flask_mail import Message
from app import mail, app


def send_async_email(app, msg):
    """发送异步邮件"""
    with app.app_context():     # 调用上下文
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()