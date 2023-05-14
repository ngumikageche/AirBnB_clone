#!/usr/bin/python3
"""class that defines the state"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of a city
    Attributes:
    state_id (str): The City id.
    name (str): The City name.
    """
    state_id = ""
