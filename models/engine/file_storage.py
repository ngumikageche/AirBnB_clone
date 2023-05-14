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
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            obj_dict = {k: v.to_dict()
                        for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    @classmethod
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    cls_name, obj_id = k.split('.')
                    cls = models.cls_name
                    FileStorage.__objects[k] = cls(**v)
        except FileNotFoundError:
            return
