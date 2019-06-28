#!/usr/bin/python3
''' class BaseModel that defines all
    common attributes/methods for other classes '''
import json
import uuid
from datetime import datetime


class BaseModel:
    '''int common attributes '''
    # uniq_id = uuid.uuid4()
    def __init__(self, *args, **kwargs):
        ''' variables '''
        if kwargs:
            [setattr(self, key, value) for key, value in kwargs.items()]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' str representation '''
        mg = "[BaseModel] ({}) {}"
        return mg.format(self.id, self.__dict__)

    def save(self):
        ''' updates the public instance attribute updated_at '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary with all keys/values
            of __dict__ of the instance '''
        custom_dic = {'__class__': __class__.__name__}
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()
        isos = {'created_at': created_at_iso, 'updated_at': updated_at_iso}
        custom_dic.update(self.__dict__)
        custom_dic.update(isos)
        # self.__dict__.update(custom_dic)
        # dest = {**custom_dic, **self.__dict__}
        return custom_dic
