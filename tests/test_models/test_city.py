#!/usr/bin/python3
""" Unittest City """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ testing City """

    @classmethod
    def setUpClass(clase):
        clase.cty = City()
        clase.cty.name = "Bogota"
        clase.cty.state_id = "CUND"

    @classmethod
    def deleteClase(clase):
        del clase.cty
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        self.assertTrue(issubclass(self.cty.__class__, BaseModel), True)

    def test_Functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_Attr(self):
        self.assertTrue('name' in self.cty.__dict__)
        self.assertTrue('id' in self.cty.__dict__)

    def test_Strings(self):
        self.assertEqual(type(self.cty.name), str)
        self.assertEqual(type(self.cty.state_id), str)

    def test_Save(self):
        self.cty.save()
        self.assertNotEqual(self.cty.created_at, self.cty.updated_at)

    def test_ToDict(self):
        self.assertEqual('to_dict' in dir(self.cty), True)

if __name__ == "__main__":
    unittest.main()
