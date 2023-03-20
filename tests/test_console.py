#!/usr/bin/python3
"""
Test for the console.py
"""

import os
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest
import json


class test_console(unittest.TestCase):
    """ UnitTests for the console's functions"""

    def test_create(self):
        """Test the updated create function"""
        
