#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """City Class Test Cases."""

    def setUp(self):
        """Sets up Test units methods."""
        pass

    def tearDown(self):
        """Tears down Test unit methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_city_instantiation(self):
        """Tests instantiation of City class."""

        c1 = City()
        self.assertEqual(str(type(c1)), "<class 'models.city.City'>")
        self.assertIsInstance(c1, City)
        self.assertTrue(issubclass(type(c1), BaseModel))

    def test_city_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        c1 = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(c1, key))
            self.assertEqual(type(getattr(c1, key, None)), value)

if __name__ == "__main__":
    unittest.main()

