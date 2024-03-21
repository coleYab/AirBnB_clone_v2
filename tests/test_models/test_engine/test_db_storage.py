import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestDBStorage(unittest.TestCase):
	def setUp(self):
		self.storage = DBStorage()

	def tearDown(self):
		self.storage.close()

	def test_all(self):
		# Test if all() returns a dictionary
		result = self.storage.all()
		self.assertIsInstance(result, dict)

	def test_new(self):
		# Test if new() adds an object to the session
		obj = BaseModel()
		self.storage.new(obj)
		self.assertIn(obj, self.storage._DBStorage__session)

	def test_save(self):
		# Test if save() commits the changes to the database
		obj = BaseModel()
		self.storage.new(obj)
		self.storage.save()
		self.assertIn(obj, self.storage._DBStorage__session)

	def test_delete(self):
		# Test if delete() removes an object from the session
		obj = BaseModel()
		self.storage.new(obj)
		self.storage.delete(obj)
		self.assertNotIn(obj, self.storage._DBStorage__session)

	def test_reload(self):
		# Test if reload() reloads the data from the database
		obj = BaseModel()
		self.storage.new(obj)
		self.storage.save()
		self.storage.reload()
		self.assertNotIn(obj, self.storage._DBStorage__session)

	def test_close(self):
		# Test if close() closes the session
		self.storage.close()
		self.assertIsNone(self.storage._DBStorage__session)

if __name__ == '__main__':
	unittest.main()
