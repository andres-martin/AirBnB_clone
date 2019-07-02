#!/usr/bin/python3
""" Unittest Amenity """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ testing Amenity """

    @classmethod
    def setUpClass(clase):
        clase.amt = Amenity()
        clase.amt.name = "Buena"

    @classmethod
    def deleteClase(clase):
        del clase.amt
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        self.assertTrue(issubclass(self.amt.__class__, BaseModel), True)

    def test_Functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_Attr(self):
        self.assertTrue('name' in self.amt.__dict__)

    def test_Strings(self):
        self.assertEqual(type(self.amt.name), str)

    def test_Save(self):
        self.amt.save()
        self.assertNotEqual(self.amt.created_at, self.amt.updated_at)

    def test_ToDict(self):
        self.assertEqual('to_dict' in dir(self.amt), True)

if __name__ == "__main__":
    unittest.main()
