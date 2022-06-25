import unittest
from testing_doc import add, return_day, laugh


class ActivityTests(unittest.TestCase):

	def test_add(self):
		"""Testing add function."""
		self.assertEqual(
				add(2,3), 5
			)

	def test_add_int(self):
		with self.assertRaises(ValueError):
			add('dev', 3)

	def test_return_day(self):
		"""Testing return day function."""
		self.assertEqual(
				return_day(1), 'Sunday'
			)
	
	def test_return_day_none(self):
		"""Testing for none in return day"""

		self.assertIsNone(
				return_day(8) 
			)

	def test_laugh(self):
		"""Testing laugh function"""
		self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__=="__main__":
	unittest.main()