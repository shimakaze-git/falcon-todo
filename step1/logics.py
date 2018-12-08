#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
from models import Task


def add_todo(name, text):
    """ todo listの追加 """
    try:
        task = Task(name, text)
        task.create()
    except Exception as e:
        print(e)


def update_todo(id, name, text):
    """ todo listの更新 """
    try:
        task = Task(name, text)
        task.update(id)
    except Exception as e:
        print(e)


def delete_todo(id):
    """ todo listの削除 """
    try:
        task = Task()
        task.delete(id)
    except Exception as e:
        print(e)


def get_todo_list():
    """ todo listを全て取得 """
    try:
        tasks = Task.read_list()
        return [task.as_dict for task in tasks]
    except Exception as e:
        print(e)


def get_todo(id):
    """ todo listを取得 """
    try:
        task = Task().read(id)
        if task:
            return task.as_dict
    except Exception as e:
        print(e)