#!/usr/bin/python3
""" instantiation start file storage system """


from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


clases = {"BaseModel": BaseModel, "FileStorage": FileStorage,
          "User": User, "State": State, "City": City, "Amenity": Amenity,
          "Place": Place, "Review": Review}
storage = FileStorage()
storage.reload()
