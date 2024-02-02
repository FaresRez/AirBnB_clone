#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now().isoformat(timespec='microseconds'))
        self.updated_at = str(datetime.now().isoformat(timespec='microseconds'))
    
    def __str__(self):
        """The representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """Update the object"""
        self.updated_at = str(datetime.now().isoformat(timespec='microseconds'))

    def to_dict(self):
        """Return a dictionary representation of the object"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        return  new_dict

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))