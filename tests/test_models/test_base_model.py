#!/usr/bin/python3
""" Unittest BaseModel """
import unittest
import os
import pep8
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(clase):
        clase.bsm = BaseModel()
        clase.bsm.name = "Holberton"
        clase.bsm.my_num = 89

    @classmethod
    def deleteClase(clase):
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

    def test_CheckFunctions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_Attr(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_Init(self):
        self.assertTrue(isinstance(self.bsm, BaseModel))

    def test_Save(self):
        self.bsm.save()
        self.assertNotEqual(self.bsm.created_at, self.bsm.updated_at)

    def test_ToDict(self):
        bsm_dict = self.bsm.to_dict()
        self.assertEqual(self.bsm.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bsm_dict['created_at'], str)
        self.assertIsInstance(bsm_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
