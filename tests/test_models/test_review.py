#!/usr/bin/python3
"""Unit tests for Review Class"""
import unittest
import os
import pep8
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    """Review Class Test Cases."""

    def setUp(self):
        """Sets up Test Unit methods."""
        pass

    def tearDown(self):
        """Tears down Testunit  methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_review_instantiation(self):
        """Tests instantiation of Review class."""

        r1 = Review()
        self.assertEqual(str(type(r1)), "<class 'models.review.Review'>")
        self.assertIsInstance(r1, Review)
        self.assertTrue(issubclass(type(r1), BaseModel))

    def test_review_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        r1 = Review()
        for key, value in attributes.items():
            self.assertTrue(hasattr(r1, key))
            self.assertEqual(type(getattr(r1, key, None)), value)

if __name__ == "__main__":
    unittest.main()
