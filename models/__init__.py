#!/usr/bin/python3
""" instantiation start file storage system """


from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


clases = {"BaseModel": BaseModel, "FileStorage": FileStorage, "User": User}
storage = FileStorage()
storage.reload()
