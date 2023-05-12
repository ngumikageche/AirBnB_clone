#!/usr/bin/python3
import json
"""class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""


class FileStorage:

    __file_path = "file.json"
    __objects = {}
    
    @classmethod
    def all(self):
        """func that returns the dict __objects """
        return FileStorage.__objects.copy()

    @classmethod 
    def new(self, obj):
        """func that sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    @classmethod
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            obj_dict = {}
            for key, obj in FileStorage.__objects.items():
                obj_dict[key] = obj.__dict__
            json.dump(obj_dict, f)

    @classmethod
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    """eval function to dynamically create new instance of the 
                    class based on the obects key"""
                    obj = eval(class_name)(**val)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
