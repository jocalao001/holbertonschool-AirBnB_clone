#!/usr/bin/python3
# test_state.py
"""Define Test for class State."""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test suites for class State."""

    def setUp(self):
        """
        Setup resources to be used in the tests
        i) Create a State object
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up resources after the tests
        i) Delete the instance created
        """
        del self.state

    def test_doc_module(self):
        """Test module documentation."""
        actual = State.__module__.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = State.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the state object."""
        self.assertTrue(hasattr(self.state, "name"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.state.name) == str)


if __name__ == "__main__":
    unittest.main
