#!/usr/bin/python3
# user.py
"""Define a class user implementation that
inherits from BaseModel class."""


from models.base_model import BaseModel


class User(BaseModel):
    """Implementing the class User and its attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
