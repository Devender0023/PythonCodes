def be_polite(fn):
	def wrapper(*args, **kwargs):
		print("What a pleasure to meet you!")
		fn(*args, **kwargs)
		print("Have a great day!")
	return wrapper

def shout(fn):
	def caps(*args, **kwargs):
		return fn(*args, **kwargs).upper()
	return caps

@shout
def order(main, side):
	return f"Hi, I'd like the {main}, with a side of {side}, please!"

@be_polite # This the syntactic sugar of decorator
def greet(name):
	print(f"My name is {name}.")

person = input("Enter your name: ")
greet(person)
print(order("burger", "fries"))
