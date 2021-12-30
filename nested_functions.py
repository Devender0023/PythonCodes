from random import choice

def greet(person):
	def message():
		msg = choice(('Hello there ', 'Go away ', 'I love you '))
		return msg

	result = message() + person
	return result

print(greet("Dev"))