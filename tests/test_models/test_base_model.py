#!/usr/bin/python3
""" Unittest BaseModel """
import unittest
import os
import pep8
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(clase):
        clase.base12 = BaseModel()
        clase.base12.name = "Holberton"
        clase.base12.my_num = 89

    @classmethod
    def deleteClase(clase):
        del clase.base12
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
        self.assertTrue(isinstance(self.base12, BaseModel))

    def test_Save(self):
        self.base12.save()
        self.assertNotEqual(self.base12.created_at, self.base12.updated_at)

    def test_ToDict(self):
        base12_dict = self.base12.to_dict()
        self.assertEqual(self.base12.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base12_dict['created_at'], str)
        self.assertIsInstance(base12_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
