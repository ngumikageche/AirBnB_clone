#!/usr/bin/python3
"""class that defines a Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Rep a review
    Attributes:
       place (str): The Place id.
       user_id (str): The User id.
       text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
