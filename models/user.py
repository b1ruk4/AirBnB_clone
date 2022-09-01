#!/usr/bin/python3
"""defines class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """defining User attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
