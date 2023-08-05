#!/usr/bin/python3
# file_storage.py
"""Define a class FileStorage that serializes instances.
"""

import json
import os
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent a file storage of instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of the class attribute(__objects)."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key (<obj class name>.id)."""
        k_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[k_obj] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)."""
        f_in = FileStorage.__file_path
        d = {}
        for k, v in self.__class__.__objects.items():
            d[k] = v.to_dict()
        with open(f_in, "w", encoding="utf-8") as f_out:
            json.dump(d, f_out)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        f_in = FileStorage.__file_path
        if os.path.exists(f_in):
            with open(f_in, "r", encoding="utf-8") as f_out:
                obj_dict = json.load(f_out)
                for k, v in obj_dict.items():
                    base = models.models_classes[v["__class__"]](**v)
                    FileStorage.__objects[k] = base
