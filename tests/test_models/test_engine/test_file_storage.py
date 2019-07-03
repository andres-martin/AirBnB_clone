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
        del clase.usr

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

    def test_All(self):
        """ test all """
        astorage = file_storage.FileStorage()
        instances_dic = astorage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, astorage._FileStorage__objects)

    def test_New(self):
        """ test new """
        nstorage = file_storage.FileStorage()
        dic = nstorage.all()
        rev = User()
        rev.id = 1121
        rev.name = "Alexander"
        nstorage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_Reload(self):
        """ test reload """
        self.storage.save()
        pthi = os.path.dirname(os.path.abspath("console.py"))
        pti = os.path.join(pthi, "file.json")
        with open(pti, 'r') as fi:
            lines = fi.readlines()

        try:
            os.remove(pti)
        except BaseException:
            pass

        self.storage.save()

        with open(pti, 'r') as fi:
            lines2 = fi.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(pt)
        except BaseException:
            pass

        with open(pti, "w") as fi:
            fi.write("{}")
        with open(pti, "r") as ri:
            for line in ri:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

if __name__ == "__main__":
    unittest.main()
