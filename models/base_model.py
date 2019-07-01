#!/usr/bin/python3
''' class BaseModel that defines all
    common attributes/methods for other classes '''
import json
import uuid
from datetime import datetime
import models


class BaseModel:
    '''int common attributes '''
    # uniq_id = uuid.uuid4()
    def __init__(self, *args, **kwargs):
        ''' variables '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' str representation '''
        clsname = self.__class__.__name__
        mg = "[{}] ({}) {}"
        return mg.format(clsname, self.id, self.__dict__)

    def save(self):
        ''' updates the public instance attribute updated_at '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' returns a dictionary with all keys/values
            of __dict__ of the instance '''
        custom_dic = {'__class__': self.__class__.__name__}
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()
        isos = {'created_at': created_at_iso, 'updated_at': updated_at_iso}
        custom_dic.update(self.__dict__)
        custom_dic.update(isos)
        # self.__dict__.update(custom_dic)
        # dest = {**custom_dic, **self.__dict__}
        return custom_dic
