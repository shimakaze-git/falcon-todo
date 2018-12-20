#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''


class ExampleUser:

    def __init__(self):
        self.username = "example_user"
        self.password = "example_password"

user = ExampleUser()


def user_loader(payload):
    if user.username == payload['user']['username']:
        return user
    return None

SECRET_KEY = "example_secret_key"
