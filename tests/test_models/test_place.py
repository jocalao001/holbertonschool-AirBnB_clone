#!/usr/bin/python3
# test_place.py
"""Define Test for class Place."""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test suites for class Place."""

    def setUp(self):
        """
        Setup resources to be used in the tests
        i) Create a Place object
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up resources after the tests
        i) Delete the instance created
        """
        del self.place

    def test_doc_module(self):
        """Test module documentation."""
        actual = Place.__module__.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = Place.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the place object."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.place.city_id) == str)
        self.assertTrue(type(self.place.user_id) == str)
        self.assertTrue(type(self.place.name) == str)
        self.assertTrue(type(self.place.description) == str)
        self.assertTrue(type(self.place.number_rooms) == int)
        self.assertTrue(type(self.place.number_bathrooms) == int)
        self.assertTrue(type(self.place.max_guest) == int)
        self.assertTrue(type(self.place.price_by_night) == int)
        self.assertTrue(type(self.place.latitude) == float)
        self.assertTrue(type(self.place.longitude) == float)
        self.assertTrue(type(self.place.amenity_ids) == list)


if __name__ == "__main__":
    unittest.main
