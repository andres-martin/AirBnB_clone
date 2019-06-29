#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
print(my_model.id)
print(my_model.created_at)
print(my_model.updated_at)
print(my_model)
