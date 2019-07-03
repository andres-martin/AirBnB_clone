#!/usr/bin/python3
""" Unittest BaseModel """
import unittest
import os
import pep8
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ testing BaseModel """

    @classmethod
    def setUpClass(clase):
        """ first setup """
        clase.bsm = BaseModel()
        clase.bsm.name = "Holberton"
        clase.bsm.my_num = 89

    @classmethod
    def deleteClase(clase):
        """ final option """
        del clase.bsm
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_Functions(self):
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_Attr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.bsm, "id"), True)
        self.assertEqual(hasattr(self.bsm, "created_at"), True)
        self.assertEqual(hasattr(self.bsm, "updated_at"), True)

    def test_init(self):
        self.assertTrue(isinstance(self.bsm, BaseModel))

    def test_Save(self):
        self.bsm.save()
        self.assertNotEqual(self.bsm.created_at, self.bsm.updated_at)

    def test_ToDict(self):
        bsm_dict = self.bsm.to_dict()
        self.assertTrue(bsm_dict.get("__class__"))
        self.assertTrue(type(bsm_dict) is dict)
        self.assertTrue("to_dict" in dir(self.bsm))

if __name__ == "__main__":
    unittest.main()
