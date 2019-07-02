#!/usr/bin/python3
""" Unittest User """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """ testing User """

    @classmethod
    def setUpClass(clase):
        clase.usr = User()
        clase.usr.first_name = "Jessica"
        clase.usr.last_name = "Sandoval"
        clase.usr.email = "alexafdeveloper@gmail.com"
        clase.usr.password = "1234"

    @classmethod
    def deleteClase(clase):
        del clase.usr
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        self.assertTrue(issubclass(self.usr.__class__, BaseModel), True)

    def test_Functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_Attr(self):
        self.assertTrue('email' in self.usr.__dict__)
        self.assertTrue('id' in self.usr.__dict__)
        self.assertTrue('created_at' in self.usr.__dict__)
        self.assertTrue('updated_at' in self.usr.__dict__)
        self.assertTrue('password' in self.usr.__dict__)
        self.assertTrue('first_name' in self.usr.__dict__)
        self.assertTrue('last_name' in self.usr.__dict__)

    def test_Strings(self):
        self.assertEqual(type(self.usr.email), str)
        self.assertEqual(type(self.usr.password), str)
        self.assertEqual(type(self.usr.first_name), str)
        self.assertEqual(type(self.usr.first_name), str)

    def test_Save(self):
        self.usr.save()
        self.assertNotEqual(self.usr.created_at, self.usr.updated_at)

    def test_ToDict(self):
        self.assertEqual('to_dict' in dir(self.usr), True)

if __name__ == "__main__":
    unittest.main()
