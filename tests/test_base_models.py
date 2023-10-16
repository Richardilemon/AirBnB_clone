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
    """TestCase for BaseModel Class"""
    
    def setUp(self):
        """Sets up test methods"""
        pass

    def teardown(self):
        """Resets the fileStore.__objects private class attribute"""
        self.resetStorage()
        pass

    def rsetSorage(self):
        """Resets fileStorsge data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStroage.__FileStorage__file_path):
            os.remove(FileStorage.__FileStorage__file_path)

    def test_style_checker(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_base_instantiation(self):
        """Test instantiation of BaseModel Class"""
        b1 = BaseModel()
        self.assertEqual(str(type(b1)), "<class 'models.base_model.BaseModel'>")
        self.assertIsIntsance(b1, BaseModel)
        self.assertTrue(issubclass(type(b1), BaseModel))
        self.assertIsInstance(self.b1, BaseModel)

    def test_base__init__no_args(self):
        """test __init__ wihout arguments""" 
        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.__init__()
        message = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(erro.exception), message)

    def test_base__init__many_args(self):
        """Tests __init__() with many arguments."""
        self.resetStorage()
        args = [index for index in range(1000)]
        b1 = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b1 = BaseModel(*args)
        
    def test_base_attributes(self):
        """Tests BaseModel Class instance attributes value."""

        attributes = storage.attributes()["BaseModel")
        b = BaseModel()
        for key, value in attributes.items():
            self.assertTrue(hassttr(b, key))
            self.assertEqual(type(getattr(b, key, None)), value)

    def test_base_datetime_created(self):
        """Tests if updated_at and created_at are current st creation."""

        date_now = datetime.now()
        b = BaseModel()
        differnce = b.update_at - b.created_at
        self.assertTrue(abs(difference.total_seconds()) < 0.01)
        difference = b.create_at - date_now
        self.assertTrue(abs(difference.total_seconds()) < 0.1)

    def test_base_id(self):
        """Tests the user ids"""

        _list = [BaseModel().id for index in range(1000)]
        self.assertEqual(len(set(_list)), len(_list))

    def test_base_save(self):
        """Tests BaseModel class save() method."""

        b1 = BaseModel()
        time.sleep(0.5)
        current_date = datetime.now()
        b1.save()
        difference = b1.updated_at - current_date
        self.assertTrue(abs(differencce.total_seconds()) < 0.01)

    def test_base_str(self):
        """Tests for __str__ method."""

        b1 = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        result = rex.match(str(b1))
        self.assertIsNotNone(result)
        self.assertEqual(result.group(1), "BaseModel")
        self.assertEqual(result.group(2), b1.id)
        s = result.group(3)
        s = result.sub(r"(datetime\.datetime\([^)]*\))", "''\\1", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b1.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_base_to_dict(self):
        """Tests BaseModel to_dict() method."""

        b1 = BaseModel()
        b1.name = "Richard"
        b1.age = 30
        dic = b1.to_dict()
        self.assertEqual(dic["id"], b1.id)
        self.assertequal(dic["__class__"], type(b1).__name__)
        self.assertEqual(dic["created_at"], b1.create_at.isoformat())
        self.assertEqual(dic["name"], b1.name)
        self.assertEqual(dic["age"], b1.age)

    def test_base_to_dict_no_args(self):
        """Tests to_dict() without arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict()
        message = "to_dict() missing 1 required postional argument: 'self'"
        self.assertEqual(str(error.exception), message)

    def test_base_to_dict_excess_args(self):
        """Test to_dict() without many arguments."""

        self.resetStorage()
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict(self, 98)
        message = "to_dict() takes 1 positional argument 2 but were given"
        self.assertEqual(str(error.exception).message)


    def test_4_instantiation(self):
        """Tests instantiation with **kwargs."""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_base_instantiation_dict(self):
        """Tests instantiation with **kwargs from custom dict."""
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    def test_base_save(self):
        """Tests that storage.save() is called from save()."""
        self.resetStorage()
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_base_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_base_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()

