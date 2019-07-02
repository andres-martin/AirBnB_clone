#!/usr/bin/python3
""" Unittest Place """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """ testing Place """

    @classmethod
    def setUpClass(clase):
        clase.plc = Place()
        clase.plc.name = "Hotel"
        clase.plc.description = "El mejor lugar"

    @classmethod
    def deleteClase(clase):
        del clase.plc
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        self.assertTrue(issubclass(self.plc.__class__, BaseModel), True)

    def test_Functions(self):
        self.assertIsNotNone(Place.__doc__)

    def test_Attr(self):
        self.assertTrue('name' in self.plc.__dict__)
        self.assertTrue('description' in self.plc.__dict__)

    def test_Strings(self):
        self.assertEqual(type(self.plc.name), str)
        self.assertEqual(type(self.plc.description), str)

    def test_Save(self):
        self.plc.save()
        self.assertNotEqual(self.plc.created_at, self.plc.updated_at)

    def test_ToDict(self):
        self.assertEqual('to_dict' in dir(self.plc), True)

if __name__ == "__main__":
    unittest.main()
