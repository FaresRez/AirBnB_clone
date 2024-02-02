#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """The representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """Update the object"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        return  new_dict
