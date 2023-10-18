#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Place Class Test Cases"""

    def setUp(self):
        """Sets up test unit methods."""
        pass

    def tearDown(self):
        """Tears down test unit methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Place class."""

        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(type(p), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        p1 = Place()
        for key, value in attributes.items():
            self.assertTrue(hasattr(p1, key))
            self.assertEqual(type(getattr(p1, key, None)), value)

if __name__ == "__main__":
    unittest.main()

