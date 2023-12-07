#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self):
        BaseModel.id = str(uuid.uuid4())
        BaseModel.created_at = datetime.now()
        BaseModel.updated_at = datetime.now()
    


b= BaseModel()
print(b.id)

c= BaseModel()
print(c.id)