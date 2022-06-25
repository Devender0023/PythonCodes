from random import choice

def add(a,b):
	"""
	>>> add(2,3)
	6
	>>> add(100,200)
	20000
	"""
	if not isinstance(a, int) and isinstance(b, int):
		raise ValueError("Both numbers must be integers")
	return a + b


def return_day(num):
	"""
	>>> return_day(1)
	'Sunday'
	>>> return_day(8)
	
	"""

	days=[
		"Sunday",
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
        "Saturday"
	]

	
	if num>0 and num<=len(days):
		return days[num-1]
	return None


def last_element(nums):
	"""
	>>> last_element([1, 2, 3])
	3
	>>> last_element([])
	
	"""

	if len(nums) == 0:
		return None
	return nums[-1]


def number_compare(a, b):
	"""
	>>> number_compare(2, 3)
	'Second is greater'
	>>> number_compare(2, 2)
	'Numbers are equal'
	"""

	if a==b:
		return "Numbers are equal"
	elif a>b:
		return "First is greater"
	return "Second is greater"

def laugh():
	return choice(('lol', 'haha', 'tehehe'))


