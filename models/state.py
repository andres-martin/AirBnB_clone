#!/usr/bin/python3
''' class State that inherits from BaseModel '''
from .base_model import BaseModel


class State(BaseModel):
    ''' class State for state model
    Args:
        name (str): empty string
    '''
    name = ""
