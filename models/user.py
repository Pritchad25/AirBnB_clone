#!/usr/bin/python3
""" User model """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
