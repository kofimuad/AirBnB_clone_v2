#!/usr/bin/python3
"""Defines unittest for console.py"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage

class TestHBNBCommand(unittest.TestCase):
    """Unittest for testing the HBNB Command Interpreter"""

    @classmethod
    def setUpClass(cls):
        """
        Temp rename any existing file.json
        Reset file storage object dict
        create an instance of the command interpreter
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        # Create an instance of HBNB class
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        Restore original file.json
        Delete test HBNBCommand instance
        """
        try:
            os.rename("tmp","file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        """Resets FileStorage object dict"""
        FileStorage.__FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create_for_errors(self):
        """Test create command errors"""
        # Test if create command is missing
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('create')
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        # Test if class doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('create asdfasdf')
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
        """Test create command"""
        # Create BaseModel instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create BaseModel')
            bm = f.getvalue().strip()
        # Create User instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create User')
            us = f.getvalue().strip()
        # Create State instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create State')
            st = f.getvalue().strip()
        # Create Place instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create Place')
            pl = f.getvalue().strip()
        # Create City instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create City')
            ct = f.getvalue().strip()
        # Create Review instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create Review')
            rv = f.getvalue().strip()
        # Create Amenity instance and capture ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd('create Amenity')
            am = f.getvalue().strip()
        # Test if all created instances are in output of "all" command
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all BaseModel')
            self.assertIn(bm, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all User')
            self.assertIn(us, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all Place')
            self.assertIn(pl, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all State')
            self.assertIn(st, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all Review')
            self.assertIn(rv, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all City')
            self.assertIn(ct, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all Amenity')
            self.assertIn(am, f.getvalue())

    def test_create_command_with_kwargs(self):
        """Test create command with kwargs"""
        # Test create command with additional key value pairs
        with patch('sys.stdout', new=StringIO()) as f:
            call = (f'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            self.HBNB.onecmd('call')
            pl = f.getvalue().strip()

        # check if created instance and kwargs are in output of "all" command
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd('all Place')
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'user_id': '0001'", output)
            self.assertIn("'name': 'My_little_house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'number_bathrooms': 2", output)
            self.assertIn("'max_guest': 10", output)
            self.assertIn("'price_by_night': 300", output)
            self.assertIn("'latitude': 37.773972", output)
            self.assertIn("'longitude': -122.431297", output)

if __name__ == "__main__":
    unittest.main()
