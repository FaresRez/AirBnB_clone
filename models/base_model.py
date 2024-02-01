#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self):
        BaseModel.id = str(uuid.uuid4())
        BaseModel.created_at = datetime.now()
        BaseModel.updated_at = datetime.now()
    
    def __str__(self):
        """The representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """Update the object"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        



b= BaseModel()
print(b)

c= BaseModel()
print(c.updated_at)