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
            # FileStorage.__objects.update({clsname + "." + obj.id: obj})
        # FileStorage.__objects.update(obj.__dict__)

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fn:
            # fn.write(json.dumps(.__objects))
            d_objs = FileStorage.__objects.copy()
            d_tmp = {k: o.to_dict() for k, o in d_objs.items()}
            d_objs.update(d_tmp)
            json.dump(d_objs, fn)

    def reload(self):
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ; otherwise,
            do nothing. If the file doesn’t exist,
            no exception should be raised) '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fn:
                dtmp = json.load(fn)
                # get the key from dictmp slice it and pass it to
                # dictionary comprehension
                cls = models.clases
                dtmp = {k: cls[k.split('.')[0]](**o) for k, o in dtmp.items()}
                FileStorage.__objects = dtmp
        except FileNotFoundError:
            pass
