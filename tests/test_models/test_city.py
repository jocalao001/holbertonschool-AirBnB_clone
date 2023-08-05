#!/usr/bin/python3
# test_city.py
"""Define Test for class City."""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suites for class State."""

    def setUp(self):
        """
        Setup resources to be used in the tests
        i) Create a City object
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up resources after the tests
        i) Delete the instance created
        """
        del self.city

    def test_doc_module(self):
        """Test module documentation."""
        actual = City.__module__.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = City.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the city object."""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.city.name) == str)
        self.assertTrue(type(self.city.state_id) == str)


if __name__ == "__main__":
    unittest.main
