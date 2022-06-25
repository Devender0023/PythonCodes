import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
	"""docstring for RobotTests"""

	def setUp(self):
		self.spot = Robot("Spot", battery=50)


	def test_charge(self):
		self.spot.charge()
		self.assertEqual(self.spot.battery, 100)

	def test_say_name(self):
		self.spot.say_name()
		self.assertEqual(self.spot.battery, 49)

	def test_learn_skill(self):
		self.spot.learn_skill()
		self.assertEqual(self.spot.battery, 40)

if __name__ == "__main__":
	unittest.main()
