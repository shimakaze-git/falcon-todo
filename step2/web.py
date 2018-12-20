#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
import json
import falcon

from auth import user_loader, SECRET_KEY, ExampleUser

from falcon_auth import FalconAuthMiddleware, JWTAuthBackend

API_ENDPOINT = "/api"


auth_backend = JWTAuthBackend(user_loader, SECRET_KEY)
auth_middleware = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=None,
    exempt_methods=None
)
app = falcon.API(
    middleware=[auth_middleware]
)


class TokenAuth:

    auth = {
        'auth_disabled': True,
        # 'exempt_methods': ['POST']
    }

    def on_post(self, req, resp, **params):
        body = req.stream.read()
        data = json.loads(body)

        username = data['username']
        password = data['password']

        user = ExampleUser()

        if ((user.username == username) and (user.password == password)):
            user_payload = {
                'username': user.username
            }
            jwt_token = auth_backend.get_auth_token(
                user_payload
            )
            response = {
                "jwt": jwt_token
            }
        else:
            response = {
                "message": "username or password is incorrect."
            }

        resp.body = json.dumps(
            response
        )

app.add_route(API_ENDPOINT + "/token-auth", TokenAuth())
# app.add_route(API_ENDPOINT + "/todo", AddGetTodo())
# app.add_route(API_ENDPOINT + "/todo/{id}", UpdateGetDeleteTodo())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
