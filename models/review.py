#!/usr/bin/python3
''' class Review that inherits from BaseModel '''
from .base_model import BaseModel


class Review(BaseModel):
    ''' class Review for Review model
    Args:
        place_id (str): empty string: it will be the Place.id
        user_id (str): empty string: it will be the User.id
        text (str): empty string
    '''
    place_id = ""
    user_id = ""
    text = ""
