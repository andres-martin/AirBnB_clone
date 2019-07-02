#!/usr/bin/python3
""" Unittest FileStorage """
import unittest
import os
import pep8
import json
from models.base_model import BaseModel
from models.engine import file_storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """ testing filestorage """

    @classmethod
    def setUpClass(clase):
        clase.usr = User()
        clase.usr.first_name = "Jessica"
        clase.usr.last_name = "Sandoval"
        clase.usr.email = "alexafdeveloper@gmail.com"
        clase.storage = file_storage.FileStorage()

    @classmethod
    def deleteClase(clase):
        del clase.clase

    def deleteClase(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
