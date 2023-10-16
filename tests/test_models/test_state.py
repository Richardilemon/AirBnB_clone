#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Test Cases for the State class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_state_instantiation(self):
        """Tests instantiation of State class."""

        s1 = State()
        self.assertEqual(str(type(s1)), "<class 'models.state.State'>")
        self.assertIsInstance(s1, State)
        self.assertTrue(issubclass(type(s1), BaseModel))

    def test_state_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        s1 = State()
        for key, value in attributes.items():
            self.assertTrue(hasattr(s1, key))
            self.assertEqual(type(getattr(s1, key, None)), value)

if __name__ == "__main__":
    unittest.main()

