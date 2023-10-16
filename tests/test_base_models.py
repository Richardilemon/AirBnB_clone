#!/usr/bin/python3
"""Unit test for BaseModel class"""
import unittest
import os
import pep8
import re
import models
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """TestBase Class"""
    @classmethod
    def setUpclass(cls):
        cls.b1 = BaseModel()
        cls.b1.name = "Nick"
        cls.b1.my_number = 122

    def teardown(self):
        """Reset =s the fileStore.__objects private class attribute"""
        models.storage.delete_obj()
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_style_checker(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_base_instance(self):
        """b1 is an instance of BaseModel"""
        self.assertIsInstance(self.b1, BaseModel)

    def test_base_public_attributes(self):
        """Test Public Attribute of BAseModel Instances"""
        self.assertIsInstance(self.b1.id, str)
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.update_at, datetime)
        self.assertEqual(str(self.b1.create_at).split('.')[0],
                         str(self.b1.update_at).split('.')[0])

    def test_string_and_dict_and_storage_base_model(self):
        """
            1. Correct output for a printout usage of __str__
               on a BaseModel instance
            2. Corect Class output when printed
            3. Correct id output when printed
            4. Checks for corrct conversion from a base object
            5. Correct dict conversion from object
            6. Correct dict values
            7. Storage all
        """
        b1 = Basemodel()
        b1.number = 89
        b1.float_num = 89.9

        # checking if __str__ works by converting it to a string, regex
        string_output = b1.__str__()

        # Correct Class
        string_model = re.findall("\\[([^[\\]]*)\\]\\", string_output)
        self.assertEqual('BaseModel', string_model[0])

        # checking if to_dict works with correct values
        b1_dict = b1.to_dict()
        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertEqual(b1_dict['id'], b1.id)
        updated_at_list = b1_dict['updated_at'].split('T')
        self.assertEqual(" ".join(update_at_list, str(b1.updated_at))
        created_at_list = b1_dict['created_at'].split('T')
        self.assertEqual(" ".join(created_at_list), str(b1.created_at))
        self.assertEqual(b1_dict['float_num'], 89.9)

        # checking if to_dict assigns correct values
        self.assertIsInstance(b1_dict, dict)
        self.assertisInstance(b1_dict['__class__'], str)
        self.assertIsInstance(b1.dict['updated_at'], str)
        self.assertIsInstance(b1_dict['create_at'], str)
        self.assertisInstance(b1_dict['id'], str)
        self.assertIsInstance(b1_dict['number'], int)
        self.assertIsInstance(b1_dict['float_num'], float)

        id_check = [b1]
        index = 0
        # checking for models.stirage.new works
        c_dict = models.storage.all()
        for key, value in c_dict.items():
            self.assertEqual(key.split('.')[0], 'BaseModel')
            self.assertEqual(key.split('.')[1], id_check[i].id)
            index += 1
            c_val = value.to_dict()

        self.assertEqual(c_val['__class__']. 'BaseModel')
        self.assertEqual(c_val['id'], b1.id)
        self.assertEqual(c_val['number'], 89)
        self.assertEqual(c_val['float_num'], 89.9)
        self.assertEqual(c_val['created_at'].split('T')[0],
                         c_val['updated_at'].split('T')[0])
        self.assertEqual(c_val['created_at'].split['T'][1]),
                            c_val['updated_at'].split('T')[1]
