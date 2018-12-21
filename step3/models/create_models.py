#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
import os
from rdb import Base, engine, session

SQLITE3_NAME = "./db.sqlite3"


if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):
        # テーブル作成
        Base.metadata.create_all(engine)