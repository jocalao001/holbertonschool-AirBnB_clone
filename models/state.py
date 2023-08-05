#!/usr/bin/python3
# state.py
"""Define a class named state; implementation."""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that inherits from BaseModel and represent
    a state.
    """

    name = ""
