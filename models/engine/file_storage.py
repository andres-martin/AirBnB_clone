#!/usr/bin/python3
''' class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances '''
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    ''' private class attributes '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        clsname = obj.__class__.__name__
        FileStorage.__objects.update({clsname + "." + obj.id: obj})
        # FileStorage.__objects.update(obj.__dict__)

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fn:
            # fn.write(json.dumps(self.__objects))
            d_objs = FileStorage.__objects
            d_tmp = {k: o.to_dict() for k, o in d_objs.items()}
            # d_objs.update(d_tmp)
            FileStorage.__objects.update(d_tmp)
            json.dump(FileStorage.__objects, fn)

    def reload(self):
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ; otherwise,
            do nothing. If the file doesn’t exist,
            no exception should be raised) '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fn:
                dictmp = json.load(fn)
                dictmp = {k: BaseModel(**o) for k, o in dictmp.items()}
                # dictmp = map(lambda k: (k[0], f(k[1])), dictmp.items())
                FileStorage.__objects = dictmp
        except FileNotFoundError:
            pass
