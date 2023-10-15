#!/usr/bin/python3
"""The `amenity` module

It defines the Amenity class,
which is a sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided.

    Attributes:
        name
    """

    name = ""
