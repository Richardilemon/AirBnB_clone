#!/usr/bin/python3

"""
This is the base of the project
"""

import models
import uuid
from datetime import datetime
    
class BaseModel():
    """
    Base class
    """
    
    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()    
        
        models.storage.new(self)
        
    
    def __str__(self):
        """
        returns string representation
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )
        
        
    def save(self):
        """
        updates the public instance attribute
        at the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """    
        
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
