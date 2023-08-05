#!/usr/bin/python3
# review.py
"""Define a class named Review; implementation."""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that inherits from BaseModel and represent
    a review
    """

    place_id = ""
    user_id = ""
    text = ""
