#!/usr/bin/python3
""" class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances """
import json
import models


class FileStorage:
    """ private class attributes """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        clsname = obj.__class__.__name__
        if obj:
            self.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        d_objs = {}
        for id, objs in self.__objects.items():
            d_objs[id] = objs.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as fn:
            json.dump(d_objs, fn)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, encoding='utf-8') as fn:
                dtmp = json.load(fn)
            for key, value in dtmp.items():
                cls = models.clases[value["__class__"]](**value)
                self.__objects[key] = cls
        except FileNotFoundError:
            pass
