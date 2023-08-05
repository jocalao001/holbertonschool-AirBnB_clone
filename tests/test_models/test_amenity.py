#!/usr/bin/python3
# test_amenity.py
"""Define Test for class Amenity."""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suites for class Amenity."""

    def setUp(self):
        """
        Setup resources to be used in the tests
        i) Create a Amenity object
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up resources after the tests
        i) Delete the instance created
        """
        del self.amenity

    def test_doc_module(self):
        """Test module documentation."""
        actual = Amenity.__module__.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = Amenity.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the amenity object."""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.amenity.name) == str)


if __name__ == "__main__":
    unittest.main
