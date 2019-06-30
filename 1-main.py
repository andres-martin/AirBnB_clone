#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage


my_model = BaseModel()
my_model.name = "Holberton"
my_model.save()
all_objs = storage.all()
print("-- model str repre --")
print(my_model)
print("-- model.to_dict() --")
print(my_model.to_dict())
print("-- Reloaded objects --")
# print(all_objs)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# print(my_model)
