#!/usr/bin/python3
''' class City that inherits from BaseModel '''
from .base_model import BaseModel


class City(BaseModel):
    ''' class City for City model
    Args:
        state_id (str): empty string: it will be the State.id
        name (str): empty string
    '''
    state_id = ""
    name = ""
