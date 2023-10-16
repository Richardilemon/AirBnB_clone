#!/usr/bin/python3
"""The `state` module

It defines the State class,
which is a sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.

    Attributes:
        name
    """
    name = ""
