#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
import os
from datetime import datetime

from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.functions import current_timestamp

from rdb import Base, engine, session

SQLITE3_NAME = "./db.sqlite3"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(256))
    text = Column(String(256))
    created_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp()
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
        onupdate=datetime.now()
    )

    def __init__(self, name=None, text=None):
        self.name = name
        self.text = text

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text
        }

    @classmethod
    def read_list(cls):
        try:
            models = []
            with session.begin():
                query = session.query(cls)
                models = query.all()
            return models
        except SQLAlchemyError as e:
            print(e)

    @classmethod
    def read(cls, id):
        try:
            with session.begin():
                task = session.query(
                    cls
                ).filter(
                    cls.id == id
                ).first()
                return task
        except SQLAlchemyError as e:
            print(e)

    def create(self):
        try:
            with session.begin():
                session.add(self)
        except SQLAlchemyError as e:
            print(e)

    def update(self, id):
        try:
            task = self.read(id)
            if task:
                with session.begin():
                    task.name = self.name
                    task.text = self.text
        except SQLAlchemyError as e:
            print(e)

    def delete(self, id):
        try:
            task = self.read(id)
            if task:
                with session.begin():
                    session.delete(task)
        except SQLAlchemyError as e:
            print(e)


if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):
        # テーブル作成
        Base.metadata.create_all(engine)
