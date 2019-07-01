#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models import storage

print("-- Create a new User --")
my_place = Place()
my_place.name = "Betty"
my_place.description = "Holberton"
my_place.number_rooms = 3
my_place.number_bathrooms = 2
my_place.max_guest = 2
my_place.price_by_night = 200
my_place.latitude = 2.5
my_place.longitude = 2.44
my_place.save()
print(my_place)

print("-- Create a new User 2 --")
my_place2 = Place()
my_place2.name = "Medellin"
my_place2.description = "Good"
my_place2.number_rooms = 4
my_place2.number_bathrooms = 2
my_place2.max_guest = 3
my_place2.price_by_night = 300
my_place2.latitude = 2.6
my_place2.longitude = 4.44
my_place2.save()
print(my_place2)
