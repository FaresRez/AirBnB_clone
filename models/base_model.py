#!/usr/bin/python3
import datetime

class BaseModel:
    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = uuid.uuid4()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel object.

        Returns:
            dict: A dictionary representation of the BaseModel object.
        """
        base_model_dict = self.__dict__
        base_model_dict["updated_at"] = self.updated_at.isoformat()
        base_model_dict["created_at"] = self.created_at.isoformat()
        return base_model_dict
