#!/usr/bin/python3
""" Unittest Review """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """ testing Review """

    @classmethod
    def setUpClass(clase):
        clase.rvw = Review()
        clase.rvw.text = "Excelente"

    @classmethod
    def deleteClase(clase):
        del clase.rvw
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        self.assertTrue(issubclass(self.rvw.__class__, BaseModel), True)

    def test_Functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_Attr(self):
        self.assertTrue('text' in self.rvw.__dict__)

    def test_Strings(self):
        self.assertEqual(type(self.rvw.text), str)

    def test_Save(self):
        self.rvw.save()
        self.assertNotEqual(self.rvw.created_at, self.rvw.updated_at)

    def test_ToDict(self):
        self.assertEqual('to_dict' in dir(self.rvw), True)

if __name__ == "__main__":
    unittest.main()
