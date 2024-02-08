#!/usr/bin/python3
import uuid
from datetime import datetime

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
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--***************")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)