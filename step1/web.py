#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''

import json
import falcon

from logics import get_todo_list
from logics import add_todo

from logics import get_todo
from logics import update_todo
from logics import delete_todo

API_ENDPOINT = "/api"


class UpdateGetDeleteTodo:

    def on_get(self, req, resp, id):
        todo = get_todo(id)

        response = {
            "status": True,
            "todo": todo
        }
        resp.body = json.dumps(
            response
        )

    def on_put(self, req, resp, id):

        body = req.stream.read()
        data = json.loads(body)

        name = data['name']
        text = data['text']
        update_todo(id, name, text)

        response = {
            "status": True
        }
        resp.body = json.dumps(
            response
        )

    def on_delete(self, req, resp, id):
        delete_todo(id)

        response = {
            "status": True
        }
        resp.body = json.dumps(
            response
        )


class AddGetTodo:
    def on_get(self, req, resp):
        todos = get_todo_list()
        response = {
            "status": True,
            "todos": todos
        }
        resp.body = json.dumps(
            response
        )

    def on_post(self, req, resp):
        body = req.stream.read()
        data = json.loads(body)

        name = data['name']
        text = data['text']
        add_todo(name, text)

        response = {
            "status": True
        }
        resp.body = json.dumps(
            response
        )

app = falcon.API()
app.add_route(API_ENDPOINT + "/todo", AddGetTodo())
app.add_route(API_ENDPOINT + "/todo/{id}", UpdateGetDeleteTodo())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
