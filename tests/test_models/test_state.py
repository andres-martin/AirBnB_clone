#!/usr/bin/python3
""" Unittest State """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """ testing State """

    @classmethod
    def setUpClass(clase):
        clase.stt = State()
        clase.stt.name = "Cundinamarca"

    @classmethod
    def deleteClase(clase):
        del clase.stt
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        self.assertTrue(issubclass(self.stt.__class__, BaseModel), True)

    def test_Functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_Attr(self):
        self.assertTrue('name' in self.stt.__dict__)

    def test_Strings(self):
        self.assertEqual(type(self.stt.name), str)

    def test_Save(self):
        self.stt.save()
        self.assertNotEqual(self.stt.created_at, self.stt.updated_at)

    def test_ToDict(self):
        self.assertEqual('to_dict' in dir(self.stt), True)

if __name__ == "__main__":
    unittest.main()
