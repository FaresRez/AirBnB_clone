#!/usr/bin/python3

import json
import os


class FileStorage:
    """serializes inst to a JSON file and deser JSON file to inst"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serializable_objects = {}

        for key, obj in self.__objects.items():
            serializable_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serializable_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                if os.path.getsize(self.__file_path) > 0:
                    self.__objects = json.load(f)
