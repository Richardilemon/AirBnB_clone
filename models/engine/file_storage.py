#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class.
"""
import os
import json
from models.base_model import BaseModel



class FileStorage():
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def resetStorage(self):
        """Resets FileStorage data."""
        for instance in FileStorage.__objects.values():
            instance.__dict__.clear()  # Clear the attributes of each instance

        FileStorage.__objects = {}  # Clear the class attribute

        if os.path.isfile(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)  # Removes the file if it exists

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, it does nothing
        """

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return