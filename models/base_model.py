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
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        dt_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, dt_fmt)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """func that updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all the keys/values of __dict__"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """print [<class name>} (<self.id>) <self.__dict__>
        """
        class_name = type(self).__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
