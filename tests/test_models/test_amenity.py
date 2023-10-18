#!/usr/bin/python3
"""Unittest module for Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Amenity class Test Case."""

    def setUp(self):
        """Sets up Test unit methods."""
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

    def test_amenity_instantiation(self):
        """Tests instantiation of Amenity class."""

        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_amenity_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        a = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(a, key))
            self.assertEqual(type(getattr(a, key, None)), value)

if __name__ == "__main__":
    unittest.main()

