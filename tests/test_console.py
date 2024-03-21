#!/usr/bin/python3
"""Test console"""
import os
import uuid
import unittest
import models
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittesting the HBNB command interpreter"""

    @classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(test_cls):
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass
        del test_cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBstorage")
    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create State name="California"')
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create City state_id="{}" name="San_Francisco_is_super_cool"'.format(str(uuid.uuid4())))
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create User email="my@me.com" password="pwd" first_name="FN" last_name="LN"')
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create Place city_id="{}" user_id="{}" name="My_house" description="no_description_yet" number_rooms=4 number_bathrooms=1 max_guest=3 price_by_night=100 latitude=120.12 longitude=101.4'.format(str(uuid.uuid4()), str(uuid.uuid4())))
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('show Place {}'.format(new_place))
            place_output = test.getvalue().strip()
            self.assertIn(new_place, place_output)

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Amenity")
            new_amenity = test.getvalue().strip()

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBstorage")
    def test_create_kwargs(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create User first_name="FN" email="my@me.com" password="pwd"')
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            user_output = test.getvalue()
            self.assertIn(new_user, user_output)
            self.assertIn("'first_name': 'John'", user_output)
            self.assertIn("'email': 'john@example.com'", user_output)
            self.assertNotIn("'last_name': 'Snow'", user_output)
            self.assertIn("'password': '1234'", user_output)


if __name__ == '__main__':
    unittest.main()
