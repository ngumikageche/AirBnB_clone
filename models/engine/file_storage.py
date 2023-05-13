#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""


class FileStorage:
    
    __file_path = "file.json"
    __objects = {}
    
    @classmethod
    def all(self):
        """func that returns the dict __objects """
        return FileStorage.__objects.copy
    
    @classmethod 
    def new(self, obj):
        """func that sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}, {obj.id}"
        FileStorage.__objects[key] = obj
    @classmethod
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    @classmethod
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj_d in obj_dict:
                    cls_name = obj_d["__class__"]
                    obj = eval(class_name)(**obj_d)
                    self.__objects["{}".format(cls_name)] = obj 
        except FileNotFoundError:
            return
