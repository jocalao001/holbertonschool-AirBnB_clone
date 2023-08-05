#!/usr/bin/python3
# city.py
"""Define a class named City; implementation."""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that inherits from BaseModel and represent
    a City
    """

    state_id = ""
    name = ""
