#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get("id")
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.name = kwargs.get("name")
            self.my_number = kwargs.get("my_number")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The representation of the object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the object"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
