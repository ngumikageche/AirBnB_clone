#!/usr/bin/python3
"""class to define Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """rep of a review
    Attributes:
        city_id (str): the City id.
        user_id (str): the User id.
        name (str): the name of the Place.
        description (str): the description of the place.
        number_rooms (int): the number of rooms.
        number_bathrooms (int): the number of rooms.
        max_guest (int): the maximum number of guest allowed.
        price_by_night (int): the amount paid each night.
        latitude (float): the latitude of the place.
        longtitude (float): the longtitude of the place.
        description (str): the Ameity id.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitute = 0.0
    longtitude = 0.0
    amenity_ids = ""
