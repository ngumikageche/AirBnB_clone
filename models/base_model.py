#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""a class that defines all common attributes/methods for other classes"""


class BaseModel:
    """constructor
    Args:
       *args (int) - number of arguments that can be passed
       **kwargs (any) - allows passing the variable lenght of keyword arguments
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now
        dt_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, dt_fmt)
                    setattr(self, key, value)
                else:
                    models.storage.new(self)
    """print [<class name>} (<self.id>) <self.__dict__>
        """
    def __str__(self):
        class_name = type(self).__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    """func that updates the public instance attribute
    updated_at with the current datetime"""
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    """returns a dictionary containing all the keys/values of __dict__"""
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
