#!/usr/bin/python3
''' class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances '''
import json
import uuid
from datetime import datetime


class FileStorage:
    ''' init attributes '''
    def __init__(self):
        ''' variables '''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        self.__objects = setattr(self, obj.__class__.__name__ + obj.id, obj)

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(self.__file_path, 'w', encoding='utf-8') as fn:
            # fn.write(json.dumps(self.__objects))
            json.dump(self.__objects, fn)

    def reload(self):
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ; otherwise,
            do nothing. If the file doesn’t exist,
            no exception should be raised) '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fn:
                json.load(fn)
        except FileNotFoundError:
            pass
