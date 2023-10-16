#!/usr/bin/python3
"""Unittest module for User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

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

    def test_user_instantiation(self):
        """Tests instantiation of User Class."""

        u1 = User()
        self.assertEqual(str(type(u1)), "<class 'models.user.User'>")
        self.assertIsInstance(u1, User)
        self.assertTrue(issubclass(type(u1), BaseModel))

    def test_user_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        u1 = User()
        for key, value in attributes.items():
            self.assertTrue(hasattr(u1, key))
            self.assertEqual(type(getattr(u1, key, None)), value)

if __name__ == "__main__":
    unittest.main()
