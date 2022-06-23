def my_func(func):
	def wrapper():
		print("Nice to meet you")
		func()
		print("Have a nice day")
	return wrapper

@my_func
def greet():
	print("My name is Dev")

# greet = my_func(greet)

greet()
greet()