#!/usr/bin/python3
"""The `city` module

It defines the city class
which is a sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes are:
        name
        state_id
    """
    name = ""
    state_id = ""
