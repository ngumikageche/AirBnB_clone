#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances"""


class FileStorage:
    """representation of  FileStorage
    Args:
        __file_path(str): json file to store data
        __objects(dict) dictionary
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(self):
        """func that returns the dict __objects """
        if FileStorage is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items()
                if type(v) == FileStorage}

    @classmethod
    def new(self, obj):
        """func that sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    @classmethod
    def save(self):
        """Serializes __objects to the JSON
        file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, mode="w") as f:
                obj_dict = {}
                for k, v in FileStorage.__objects.items():
                    obj_dict[k] = v.to_dict()
                json.dump(obj_dict, f)
        except FileNotFoundError:
            return

    @classmethod
    def reload(self):
        """deserializes the JSON file to __objects
        Raises:
            FileNotFoundError: If the JSON file specified by
             FileStorage.__file_path does not exist."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
