#!/usr/bin/python3
""" class User that inherits from BaseModel """
from .base_model import BaseModel


class User(BaseModel):
    """ class User for user model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
