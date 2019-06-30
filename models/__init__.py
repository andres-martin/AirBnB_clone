#!/usr/bin/python3
""" instantiation start file storage system """


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
clases = {"BaseModel": BaseModel, "FileStorage": FileStorage}
