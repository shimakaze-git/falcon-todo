#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
import os
from datetime import datetime

from sqlalchemy import Column, DateTime, String, text, Boolean
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.functions import current_timestamp

from rdb import Base, engine, session

# SQLITE3_NAME = "./db.sqlite3"




class User(Base):
    __tablename__ = 'users'

    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True
    )
    username = Column(
        String(150),
        unique=True
    )
    password = Column(
        String(30),
        nullable=True
    )    
    first_name = Column(
        String(30),
        nullable=True
    )
    last_name = Column(
        String(150),
        nullable=True
    )
    email = Column(
        String(254),
        nullable=True
    )
    is_superuser = Column(
        Boolean,
        default=False
    )
    is_staff = Column(
        Boolean,
        default=True
    )
    is_active = Column(
        Boolean,
        default=True
    )
    date_joined = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp()
    )
    last_login = Column(
        DateTime,
        default=datetime.now(),
        nullable=True
    )

    def __init__(
        self,
        username,
        password,
        first_name=None,
        last_name=None,
        email=None,
        is_superuser=False,
        is_staff=False,
        is_active=True
    ):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_superuser = is_superuser
        self.is_staff = is_staff
        self.is_active = is_active

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
