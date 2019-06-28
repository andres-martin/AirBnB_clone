#!/usr/bin/python3
''' class BaseModel that defines all common attributes/methods for other classes '''
import json
import uuid
from datetime import datetime


class BaseModel:
    '''int common attributes '''
    # uniq_id = uuid.uuid4()
    def __init__(self):
        ''' variables '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' str representation '''
        mg = "[BaseModel] ({}) {}"
        return mg.format(self.id, self.__dict__)
