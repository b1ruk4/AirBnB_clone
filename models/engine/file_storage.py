#!/bin/bash/python3
"""file storage"""
import json
from models import base_model
import models


class FileStorage:
    """serializes instances to a JSON file and
    de-serializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
            )

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as fh:
            json_objects = {}  # creating an empty dictionary
            json_objects.update(self.__objects)
            for key, value in json_objects.items():
                json_objects[key] = value.to_dict()
            json.dump(json_objects, fh)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception
        should be raised)
        """
        from models.base_model import BaseModel
        try:
            tmp = {}
            with open(self.__file_path, 'r', encoding="UTF8") as file_name:
                tmp = json.load(file_name)
                for key, value in tmp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
